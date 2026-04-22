FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    ffmpeg \
    espeak-ng \
    libespeak-ng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download wav2vec2 model so it's baked into the image (avoids runtime HF download)
RUN python -c "\
from transformers import AutoProcessor, Wav2Vec2ForCTC; \
AutoProcessor.from_pretrained('facebook/wav2vec2-lv-60-espeak-cv-ft'); \
Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-lv-60-espeak-cv-ft')"

# Copy application code
COPY . .

# Create audio directory for TTS files
RUN mkdir -p /tmp/audio

# Expose port
EXPOSE 8000

# Copy startup script
COPY start.py start.py
RUN chmod +x start.py

# Run the application
CMD ["python", "start.py"]



