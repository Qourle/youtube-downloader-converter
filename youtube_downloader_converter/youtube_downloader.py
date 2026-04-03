import yt_dlp
import os

def download_video(url, resolution, output_dir=None):
    try:
        print(f"Attempting to download: {url}")
        
        # Ensure output directory exists
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            outtmpl = os.path.join(output_dir, '%(title)s.%(ext)s')
        else:
            outtmpl = '%(title)s.%(ext)s'
            
        ydl_opts = {
            'format': choose_format(resolution),
            'outtmpl': outtmpl,
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Video title: {info['title']}")
            ydl.download([url])
            filename = ydl.prepare_filename(info)
            print(f"Downloaded: {filename}")
            return filename
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def download_videos(urls, resolution, output_dir=None):
    for url in urls:
        download_video(url, resolution, output_dir)

def download_playlist(url, resolution, output_dir=None):
    try:
        print(f"Attempting to download playlist: {url}")
        
        # Ensure output directory exists
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            outtmpl = os.path.join(output_dir, '%(title)s.%(ext)s')
        else:
            outtmpl = '%(title)s.%(ext)s'
            
        ydl_opts = {
            'format': choose_format(resolution),
            'outtmpl': outtmpl,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Playlist title: {info.get('title', 'Unknown')}")
            print(f"Number of videos: {len(info['entries'])}")
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def choose_format(resolution):
    if resolution in ["low", "360", "360p"]:
        return 'best[height<=360]'
    elif resolution in ["medium", "720", "720p", "hd"]:
        return 'best[height<=720]'
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        return 'best[height<=1080]'
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        return 'best[height<=2160]'
    else:
        return 'best[height<=360]'


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links