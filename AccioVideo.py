import yt_dlp as youtube_dl

def download_video(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)
    print("Download completed!")
