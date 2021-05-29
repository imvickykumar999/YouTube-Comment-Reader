
# youtube_video_url = 'https://youtu.be/GbqGmNsWDaE?list=RDMM'

from pytube import YouTube

def yt_audio(youtube_video_url = 'https://youtu.be/KBtk5FUeJbk'):
    try:
        yt_obj = YouTube(youtube_video_url)
        yt_obj.streams.get_audio_only().download(filename='audio')
        print('YouTube video audio downloaded successfully')

    except Exception as e:
        print(e)

def yt_video(vid = 'KBtk5FUeJbk'):
    try:
        youtube_video_url = 'https://youtu.be/' + vid
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        filters.get_highest_resolution().download()
        print('Video Downloaded Successfully')

    except Exception as e:
        print(e)
