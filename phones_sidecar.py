"""wav2vec2 phoneme-recognition sidecar.

Loads facebook/wav2vec2-lv-60-espeak-cv-ft once at startup.
POST /phones  — raw audio bytes (webm/wav/ogg) → {"ipa": "..."}
GET  /health  — {"status": "ready"} when model is loaded
"""
import subprocess
import sys

import numpy as np
import torch
from flask import Flask, jsonify, request
from transformers import AutoProcessor, Wav2Vec2ForCTC

MODEL_ID = "facebook/wav2vec2-lv-60-espeak-cv-ft"
SAMPLE_RATE = 16_000

print(f"[Sidecar] Loading {MODEL_ID}...", file=sys.stderr, flush=True)
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print(f"[Sidecar] Model ready on {device}.", file=sys.stderr, flush=True)

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ready")


@app.post("/phones")
def phones():
    raw = request.get_data()
    if not raw:
        return jsonify(error="empty body"), 400
    try:
        proc = subprocess.run(
            [
                "ffmpeg", "-nostdin", "-loglevel", "error",
                "-i", "pipe:0",
                "-ac", "1", "-ar", str(SAMPLE_RATE), "-f", "f32le", "pipe:1",
            ],
            input=raw, capture_output=True, check=True,
        )
        audio = np.frombuffer(proc.stdout, dtype=np.float32).copy()
    except subprocess.CalledProcessError as e:
        return jsonify(error="ffmpeg failed", stderr=e.stderr.decode("utf-8", "replace")), 400

    if audio.size < SAMPLE_RATE // 10:
        return jsonify(ipa="", note="too short"), 200

    inputs = processor(audio, sampling_rate=SAMPLE_RATE, return_tensors="pt")
    with torch.no_grad():
        logits = model(inputs.input_values.to(device)).logits
    pred = torch.argmax(logits, dim=-1)
    return jsonify(ipa=processor.batch_decode(pred)[0].strip())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, threaded=False)
