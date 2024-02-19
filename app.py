from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def translate_text_to_speech(text, dest_lang):
    audio_file = f'static/{str(uuid.uuid4())}.mp3'
    tts = gTTS(text, lang=dest_lang)
    tts.save(audio_file)
    return audio_file

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        dest_lang = request.form['dest_lang']
        translated_text = translate_text(text, dest_lang)
        audio_file = translate_text_to_speech(translated_text, dest_lang)
        return jsonify({'audio_file': audio_file, 'translated_text': translated_text})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
