from gtts import gTTS
import os

# Cargar el guion
try:
    with open("script.txt", "r", encoding="utf-8") as f:
        script = f.read()
except FileNotFoundError:
    print("Error: script.txt no encontrado")
    exit(1)

# Generar audio con gTTS
try:
    tts = gTTS(text=script, lang="es", slow=False)
    tts.save("narration.mp3")
    print("Audio generado y guardado en narration.mp3")
except Exception as e:
    print(f"Error generando audio: {e}")
    exit(1)
