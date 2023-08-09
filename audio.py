import os
import youtube_dl

# URL del video de YouTube
video_url = input("Ingrese la URL del video:")

# Ruta de la carpeta de descarga
download_folder = "/home/isaacalvarez/workspace/Download_app"

# Asegurarse de que la carpeta de descarga exista
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Opciones de configuración para la descarga del audio
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Ruta de descarga
}

# Crea un objeto youtube_dl.YoutubeDL con las opciones
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_url])
