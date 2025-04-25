import yt_dlp
import os
import speech_recognition as sr
from pydub import AudioSegment
from deep_translator import GoogleTranslator
from gtts import gTTS


def download_youtube_audio(video_url, output_file="audio.mp3"):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'extract_audio': True,
            'audio_format': 'mp3',
            'outtmpl': output_file
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download successful!")  # Debugging log
    except Exception as e:
        print(f"Error downloading audio: {e}")  
        return None
    else:
        return output_file  # Runs only if no exception occurs


def speech_to_text(audio_file):
    try:
        recognizer = sr.Recognizer()

        # Convert MP3 to WAV
        audio = AudioSegment.from_mp3(audio_file)
        wav_file = "converted_audio.wav"
        audio.export(wav_file, format="wav")

        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    except Exception as e:
        print(f"Error in STT: {e}")
        return None
    else:
        return text

# ranslate Text (Tamil, English, Hindi Only)
def translate_text(text, target_lang):
    try:
        language_mapping = {"Tamil": "ta", "English": "en", "Hindi": "hi"}
        target_code = language_mapping.get(target_lang, "en")  # Default to English
        translated_text = GoogleTranslator(source='auto', target=target_code).translate(text)
    except Exception as e:
        print(f"Error in translation: {e}")
        return None
    else:
        return translated_text

# Convert Translated Text to Speech (TTS)
def text_to_speech(text, lang="English", output_file="translated_audio.mp3"):
    try:
        language_mapping = {"Tamil": "ta", "English": "en", "Hindi": "hi"}
        lang_code = language_mapping.get(lang, "en")  # Default to English
        tts = gTTS(text=text, lang=lang_code)
        tts.save(output_file)
    except Exception as e:
        print(f"Error in TTS: {e}")
        return None
    else:
        return output_file  # Runs only if no exception occurs