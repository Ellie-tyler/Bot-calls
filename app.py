from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from gpt_handler import get_gpt_response
from transcriber import transcribe_audio

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    recording_url = request.form.get("RecordingUrl")
    user_text = transcribe_audio(recording_url)
    gpt_reply = get_gpt_response(user_text)
    
    response = VoiceResponse()
    response.say(gpt_reply)
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
