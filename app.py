from flask import Flask, render_template, request, send_file
import os
import youtube_dl

app = Flask(__name__)


downloads_path = os.path.join(os.getcwd(), 'Download')

@app.route('/')
def route():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        url = request.form['url']

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', '')

        video_path = os.path.join(downloads_path, f'{video_title}.mp4')
        return send_file(video_path, as_attachment=True)

@app.route('/send2', methods=['POST'])
def send2():
    if request.method == 'POST':
        url = request.form['url']

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', '')

        audio_path = os.path.join(downloads_path, f'{video_title}.mp3')
        return send_file(audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='localhost')