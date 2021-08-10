from pytube import Playlist

playlistLink = "https://www.youtube.com/playlist?list=PL-LQrA2yKSaSdrYe7TU_8LPKSGXzmbH6b"
videoLink = "https://www.youtube.com/watch?v=XbhecuoEgxs"

import pytube
link = "https://www.youtube.com/watch?v=Pyur54JceKo"
yt = pytube.YouTube(link)
stream = yt.streams.filter(res="1080p").first()
stream.download()