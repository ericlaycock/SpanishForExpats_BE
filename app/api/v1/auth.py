import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import authenticate_user, create_access_token, create_user, get_current_user
from app.models import User, UserWord, UserSituation, Conversation
from app.schemas import (
    AltLanguageRequest,
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    ResetPasswordResponse,
    ResetProgressResponse,
    UserProfileResponse,
)

router = APIRouter()


@router.post("/register", response_model=LoginResponse)
async def register(credentials: RegisterRequest, db: Session = Depends(get_db)):
    """Register a new user and return JWT token"""
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        email = credentials.email.strip().lower()
        logger.info(f"Registration attempt for email: {email}")

        # Validate invite token and determine plan
        import json
        from app.config import settings

        # Build combined token→plan map
        token_plan_map: dict[str, str] = {}
        if settings.plan_tokens.strip():
            try:
                token_plan_map = {k.strip().lower(): v for k, v in json.loads(settings.plan_tokens).items()}
            except (json.JSONDecodeError, AttributeError):
                logger.error("PLAN_TOKENS env var is not valid JSON — ignoring")
        # Backward compat: whitelist_tokens all grant 'app'
        for t in settings.whitelist_tokens.split(","):
            t = t.strip().lower()
            if t and t not in token_plan_map:
                token_plan_map[t] = "app"

        invite = credentials.invite_token.strip().lower()
        if token_plan_map and invite not in token_plan_map:
            logger.warning(f"Registration failed: invalid invite token for {email}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid invite token"
            )
        plan = token_plan_map.get(invite, "free")

        # Validate passwords match
        if credentials.password != credentials.confirm_password:
            logger.warning(f"Registration failed: passwords do not match for {email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )

        # Validate password length
        if len(credentials.password) < 8:
            logger.warning(f"Registration failed: password too short for {email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 8 characters"
            )

        # Create user and set subscription plan
        user = create_user(db, email, credentials.password)
        logger.info(f"User created successfully: {user.id} ({user.email}), plan={plan}")

        from app.models import Subscription
        sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
        if sub:
            sub.tier = plan if plan != "free" else None
            sub.active = plan in ("app", "app_pronounce")
            db.commit()

        # Generate token with plan claim
        access_token = create_access_token(data={"sub": str(user.id), "plan": plan})
        logger.info(f"Registration successful for user: {user.id}")
        return LoginResponse(access_token=access_token, user_id=user.id, is_admin=user.is_admin, alt_language=user.alt_language, email=user.email, plan=plan)
    except HTTPException:
        # Re-raise HTTP exceptions (validation errors)
        raise
    except Exception as e:
        logger.error(f"Registration error for {email}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration. Please try again."
        )


@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token"""
    import logging
    logger = logging.getLogger(__name__)
    
    email = credentials.email.strip().lower()
    logger.info(f"Login attempt for email: {email}")
    user = authenticate_user(db, email, credentials.password)
    if not user:
        logger.warning(f"Login failed for email: {email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    logger.info(f"Login successful for user: {user.id}")
    from app.models import Subscription
    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    plan = (sub.tier if sub and sub.tier else "free")
    access_token = create_access_token(data={"sub": str(user.id), "plan": plan})
    return LoginResponse(access_token=access_token, user_id=user.id, is_admin=user.is_admin, alt_language=user.alt_language, email=user.email, plan=plan)


@router.post("/refresh", response_model=LoginResponse)
async def refresh_token(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Return a fresh JWT token for an already-authenticated user"""
    from app.models import Subscription
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    plan = (sub.tier if sub and sub.tier else "free")
    access_token = create_access_token(data={"sub": str(current_user.id), "plan": plan})
    return LoginResponse(
        access_token=access_token,
        user_id=current_user.id,
        is_admin=current_user.is_admin,
        alt_language=current_user.alt_language,
        email=current_user.email,
        plan=plan,
    )


@router.get("/me", response_model=UserProfileResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get the current user's profile"""
    return UserProfileResponse(
        email=current_user.email,
        created_at=current_user.created_at,
        is_admin=current_user.is_admin,
        alt_language=current_user.alt_language,
    )


@router.patch("/alt-language")
async def set_alt_language(
    request: AltLanguageRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Set the user's alt language (catalan | swedish | null). Admin only."""
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    if request.language not in (None, "catalan", "swedish"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid alt language")
    current_user.alt_language = request.language
    db.commit()
    return {"alt_language": current_user.alt_language}


@router.post("/forgot-password")
async def forgot_password(request: dict, db: Session = Depends(get_db)):
    """Send a password reset email with a time-limited JWT link."""
    import logging
    logger = logging.getLogger(__name__)

    email = request.get("email", "").strip().lower()
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        # Don't reveal whether the email exists
        return {"sent": True}

    # Generate a 1-hour reset token
    from app.config import settings
    from jose import jwt
    from datetime import datetime, timedelta, timezone
    token = jwt.encode(
        {"sub": str(user.id), "purpose": "reset", "exp": datetime.now(timezone.utc) + timedelta(hours=1)},
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )

    # Determine frontend URL based on environment
    frontend_url = os.environ.get("FRONTEND_URL", "https://www.spanishforexpats.com")
    reset_url = f"{frontend_url}/reset-password?token={token}"

    from app.services.email_service import send_reset_email
    sent = send_reset_email(email, reset_url)
    if not sent:
        logger.error(f"[Auth] Failed to send reset email to {email}")

    return {"sent": True}


@router.post("/reset-password")
async def reset_password(request: dict, db: Session = Depends(get_db)):
    """Reset password using a valid reset token."""
    import logging
    logger = logging.getLogger(__name__)

    token = request.get("token", "")
    new_password = request.get("new_password", "")

    if not token or not new_password:
        raise HTTPException(status_code=400, detail="Token and new_password are required")

    if len(new_password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")

    from app.config import settings
    from jose import jwt, JWTError
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        logger.info(f"[Auth] Reset token decoded: purpose={payload.get('purpose')}, sub={payload.get('sub')}")
        if payload.get("purpose") != "reset":
            logger.warning(f"[Auth] Reset token has wrong purpose: {payload.get('purpose')}")
            raise HTTPException(status_code=400, detail="Invalid reset token")
        user_id = payload.get("sub")
    except JWTError as e:
        logger.warning(f"[Auth] Reset token decode failed: {e}, token_length={len(token)}")
        raise HTTPException(status_code=400, detail="Invalid or expired reset token")

    from app.auth import get_password_hash
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"[Auth] Reset token user not found: {user_id}")
        raise HTTPException(status_code=400, detail="Invalid reset token")

    user.password_hash = get_password_hash(new_password)
    db.commit()

    return {"reset": True}


@router.post("/admin-reset-password", response_model=ResetPasswordResponse)
async def admin_reset_password(
    request: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Admin only: reset a user's password."""
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")

    email = (request.get("email") or "").strip().lower()
    new_password = request.get("new_password")
    if not email or not new_password:
        raise HTTPException(status_code=400, detail="email and new_password required")

    from app.auth import get_password_hash
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password_hash = get_password_hash(new_password)
    db.commit()
    return ResetPasswordResponse(reset=True, email=email)


@router.post("/reset-progress", response_model=ResetProgressResponse)
async def reset_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete all learning progress for the current user (admin only).

    Removes UserWord, UserSituation, and Conversation rows.
    Keeps account, subscription, and onboarding settings intact.
    """
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")

    deleted_words = db.query(UserWord).filter(UserWord.user_id == current_user.id).delete()
    deleted_situations = db.query(UserSituation).filter(UserSituation.user_id == current_user.id).delete()
    deleted_conversations = db.query(Conversation).filter(Conversation.user_id == current_user.id).delete()
    db.commit()

    return ResetProgressResponse(
        reset=True,
        deleted_words=deleted_words,
        deleted_situations=deleted_situations,
        deleted_conversations=deleted_conversations,
    )
