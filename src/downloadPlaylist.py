from pytube import YouTube, Playlist

url = input(str("\n\nEnter the link of the playlist :: "))

p = Playlist(url)

target_path = input(str("\n\nEnter the target path : "))

print("\n\nTotal number of videos : %s", len(p.video_urls))

for video in p.videos:
	print("\n\nDownloading :: " + video.title)
	vid = video.streams.filter(file_extension='mp4', adaptive=True).first().download(output_path=target_path)
