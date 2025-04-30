import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Pexels API
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
headers = {"Authorization": PEXELS_API_KEY}
url = "https://api.pexels.com/videos/search?query=nature&per_page=1"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    if not data["videos"]:
        raise ValueError("No videos found for query")
    video_url = data["videos"][0]["video_files"][0]["link"]
    video_response = requests.get(video_url)
    with open("stock_video.mp4", "wb") as f:
        f.write(video_response.content)
    print("Video de stock descargado y guardado en stock_video.mp4")
except Exception as e:
    print(f"Error descargando video de stock: {e}")
    exit(1)
