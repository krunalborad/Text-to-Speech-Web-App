import os
import requests
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# 🔐 Load ElevenLabs API key
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# ✅ Default free-tier voice
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

# ElevenLabs API URL
API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Audio output path
AUDIO_PATH = "static/audio/output.mp3"


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    audio = False

    if request.method == "POST":
        text = request.form.get("text")

        # 🔴 Validate text
        if not text:
            error = "Please enter some text."
            return render_template("index.html", audio=False, error=error)

        # 🔴 Validate API key
        if not ELEVENLABS_API_KEY:
            error = "ElevenLabs API key not found. Check your .env file."
            print("❌ API KEY NOT LOADED")
            return render_template("index.html", audio=False, error=error)

        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }

        # ✅ FREE-TIER SUPPORTED MODEL
        payload = {
            "text": text,
            "model_id": "eleven_turbo_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        try:
            response = requests.post(API_URL, json=payload, headers=headers)

            # 🔍 Debug logs
            print("STATUS CODE:", response.status_code)
            if response.status_code != 200:
                print("ERROR RESPONSE:", response.text)

            if response.status_code == 200:
                os.makedirs("static/audio", exist_ok=True)
                with open(AUDIO_PATH, "wb") as f:
                    f.write(response.content)
                audio = True
            else:
                error = f"Audio generation failed (Status {response.status_code})"

        except Exception as e:
            error = f"Request failed: {str(e)}"
            print("❌ EXCEPTION:", e)

    return render_template("index.html", audio=audio, error=error)


@app.route("/download")
def download():
    if os.path.exists(AUDIO_PATH):
        return send_file(AUDIO_PATH, as_attachment=True)
    return "Audio file not found", 404

if __name__ == "__main__":
    app.run(debug=True)