import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Crear el modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Generar un guion corto
prompt = """
Escribe un guion breve (máximo 100 palabras) para un video de 1 minuto sobre un dato curioso de la naturaleza. Usa un tono informativo y amigable, adecuado para un video narrado en YouTube. Incluye solo el texto del guion, sin títulos ni instrucciones adicionales.
"""
try:
    response = model.generate_content(prompt)
    script = response.text.strip()
except Exception as e:
    print(f"Error generando guion: {e}")
    exit(1)

# Guardar el guion
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("Guion generado y guardado en script.txt")
