from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import os

# Verificar archivos
for file in ["stock_video.mp4", "narration.mp3", "script.txt"]:
    if not os.path.exists(file):
        print(f"Error: {file} no encontrado")
        exit(1)

try:
    # Cargar video de stock
    video_clip = VideoFileClip("stock_video.mp4")

    # Cargar audio
    audio_clip = AudioFileClip("narration.mp3")

    # Duración objetivo: 60 segundos
    duration = 60

    # Ajustar el video
    if video_clip.duration > duration:
        video_clip = video_clip.subclip(0, duration)
    else:
        video_clip = video_clip.loop(duration=duration)

    # Ajustar el audio
    if audio_clip.duration > duration:
        audio_clip = audio_clip.subclip(0, duration)
    video_clip = video_clip.set_audio(audio_clip)

    # Cargar el guion
    with open("script.txt", "r", encoding="utf-8") as f:
        script = f.read()

    # Crear texto superpuesto
    text_clip = TextClip(
        script,
        fontsize=30,
        color="white",
        bg_color="black",
        size=(video_clip.w - 50, None),
        method="caption",
    ).set_position(("center", "bottom")).set_duration(duration)

    # Combinar video y texto
    final_clip = CompositeVideoClip([video_clip, text_clip])

    # Guardar el video final
    final_clip.write_videofile(
        "final_video.mp4",
        codec="libx264",
        audio_codec="aac",
        fps=24
    )

    print("Video final generado y guardado en final_video.mp4")
except Exception as e:
    print(f"Error creando video: {e}")
    exit(1)
