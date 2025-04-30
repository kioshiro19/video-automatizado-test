from TTS.api import TTS
import os

# Cargar el guion
with open("script.txt", "r", encoding="utf-8") as f:
    script = f.read()

# Inicializar Coqui TTS con un modelo en español
tts = TTS(model_name="tts_models/es/css10/vits", progress_bar=True)

# Generar audio
tts.tts_to_file(text=script, file_path="narration.wav")

print("Audio generado y guardado en narration.wav")
