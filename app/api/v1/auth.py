from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import authenticate_user, create_access_token, create_user, get_current_user
from app.models import User, UserWord, UserSituation, Conversation
from app.schemas import LoginRequest, LoginResponse, RegisterRequest, UserProfileResponse, CatalanModeRequest

router = APIRouter()


@router.post("/register", response_model=LoginResponse)
async def register(credentials: RegisterRequest, db: Session = Depends(get_db)):
    """Register a new user and return JWT token"""
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"Registration attempt for email: {credentials.email}")

        # Validate invite token
        from app.config import settings
        valid_tokens = {t.strip().lower() for t in settings.whitelist_tokens.split(",") if t.strip()}
        if valid_tokens and credentials.invite_token.strip().lower() not in valid_tokens:
            logger.warning(f"Registration failed: invalid invite token for {credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid invite token"
            )

        # Validate passwords match
        if credentials.password != credentials.confirm_password:
            logger.warning(f"Registration failed: passwords do not match for {credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        
        # Validate password length
        if len(credentials.password) < 8:
            logger.warning(f"Registration failed: password too short for {credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 8 characters"
            )
        
        # Create user
        user = create_user(db, credentials.email, credentials.password)
        logger.info(f"User created successfully: {user.id} ({user.email})")
        
        # Generate token
        access_token = create_access_token(data={"sub": str(user.id)})
        logger.info(f"Registration successful for user: {user.id}")
        return LoginResponse(access_token=access_token, user_id=user.id, is_admin=user.is_admin, catalan_mode=user.catalan_mode, email=user.email)
    except HTTPException:
        # Re-raise HTTP exceptions (validation errors)
        raise
    except Exception as e:
        logger.error(f"Registration error for {credentials.email}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration. Please try again."
        )


@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token"""
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info(f"Login attempt for email: {credentials.email}")
    user = authenticate_user(db, credentials.email, credentials.password)
    if not user:
        logger.warning(f"Login failed for email: {credentials.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    logger.info(f"Login successful for user: {user.id}")
    access_token = create_access_token(data={"sub": str(user.id)})
    return LoginResponse(access_token=access_token, user_id=user.id, is_admin=user.is_admin, catalan_mode=user.catalan_mode, email=user.email)


@router.get("/me", response_model=UserProfileResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get the current user's profile"""
    return UserProfileResponse(
        email=current_user.email,
        created_at=current_user.created_at,
        is_admin=current_user.is_admin,
        catalan_mode=current_user.catalan_mode,
    )


@router.patch("/catalan-mode")
async def set_catalan_mode(
    request: CatalanModeRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Toggle Catalan mode (admin only)."""
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    current_user.catalan_mode = request.enabled
    db.commit()
    return {"catalan_mode": current_user.catalan_mode}


@router.post("/reset-progress")
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

    return {
        "reset": True,
        "deleted_words": deleted_words,
        "deleted_situations": deleted_situations,
        "deleted_conversations": deleted_conversations,
    }
