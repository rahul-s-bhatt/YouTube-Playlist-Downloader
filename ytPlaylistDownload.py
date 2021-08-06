from pytube import Playlist

playlistLink = "https://www.youtube.com/playlist?list=PL-LQrA2yKSaSdrYe7TU_8LPKSGXzmbH6b"
playlist = Playlist(playlistLink)   

downloadDirectory = "C:\\Users\\rahul\\Python"

print("Total video to download: ", len(playlist.video_urls))    

print("\n\n Links of the youtube videos\n")

for url in playlist.video_urls:
    print(url)    

# For mp4
for video in playlist.videos:
    print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(downloadDirectory)

# For mp3
import ffmpy

for video in playlist.videos:

    audio = video.streams.get_audio_only()
    
    audio.download(downloadDirectory)

    videoTitle = video.title
    
    new_filename = videoTitle + '.mp3'
    default_filename = videoTitle + '.mp4'
    
    print(default_filename+'\n\n'+new_filename)

    ff = ffmpy.FFmpeg(
        inputs={default_filename : None},
        outputs={new_filename : None}
    )
    ff.run()
