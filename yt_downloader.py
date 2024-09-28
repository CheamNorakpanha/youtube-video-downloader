import yt_dlp as youtube_dl  # Use yt-dlp instead of youtube_dl
import os

def get_video_details(video_url):
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(video_url, download=False)  # Get info without downloading
        title = info_dict.get('title', 'Unknown Title')
        uploader = info_dict.get('uploader', 'Unknown Uploader')
        upload_year = info_dict.get('release_year', 'Unknown Year')
        
        return title, uploader, upload_year

def download_video(video_url):
    # Create the "video" folder if it doesn't exist
    if not os.path.exists("video"):
        os.makedirs("video")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video/%(title)s.%(ext)s',  # Specify the folder path here
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Downloading video from URL:", video_url)
            ydl.download([video_url])
            print("Download completed successfully!")
        except Exception as e:
            print("Error downloading video:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    
    # Get video details
    title, uploader, upload_year = get_video_details(video_url)
    
    print(f"Title: {title}")
    print(f"Uploader: {uploader}")
    print(f"Year of Upload: {upload_year}")

    # Automatically download the video without asking the user
    download_video(video_url)