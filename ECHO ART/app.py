from flask import Flask, render_template, request, jsonify
import sys, types
import speech_recognition as sr

# --- Patch for Python 3.13 where aifc/audioop are removed ---
if 'aifc' not in sys.modules:
    sys.modules['aifc'] = types.ModuleType('aifc')
if 'audioop' not in sys.modules:
    sys.modules['audioop'] = types.ModuleType('audioop')

# --- Initialize Flask app ---
app = Flask(__name__)

# --- Home route ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Voice-to-text route ---
@app.route("/voice-to-text", methods=["POST"])
def voice_to_text():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files["file"]
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Dummy image generation route (placeholder) ---
@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.get_json()
    text_input = data.get("text", "")
    # For now, just return the text back
    return jsonify({"message": f"Generated image for: {text_input}"})

# --- Run the app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
