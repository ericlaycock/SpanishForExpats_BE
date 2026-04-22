#!/usr/bin/env python3
"""Startup script that reads PORT from environment"""
import os
import sys
import subprocess
import uvicorn

# Ensure the app directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Run migrations before anything else if AUTO_MIGRATE is enabled
    if os.environ.get("AUTO_MIGRATE", "false").lower() == "true":
        print("Running database migrations...")
        subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"], check=True)

    # Run seed script only when explicitly requested (RUN_SEED=true)
    if os.environ.get("RUN_SEED", "").lower() == "true":
        print("Running seed script (RUN_SEED=true)...")
        subprocess.run([sys.executable, "scripts/seed_qa.py"], check=True)

    # Start wav2vec2 sidecar in background — model loads once, stays warm.
    # FastAPI /phones proxies to it at localhost:8001.
    sidecar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phones_sidecar.py")
    if os.path.exists(sidecar_path):
        subprocess.Popen([sys.executable, sidecar_path])
        print("🎙️  phones_sidecar.py started (loading model in background on port 8001)")
    else:
        print("⚠️  phones_sidecar.py not found — /phones endpoint will be unavailable")

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port
    )
