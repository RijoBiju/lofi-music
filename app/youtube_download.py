from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(url):
    url = f'https://www.youtube.com{url}'

    yt = YouTube(url)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download()