import pytube


def youtube_download(url:str):
	"""
			Donwload une vidéo youtube dans la résolution la plus haute.
			return : True quand c'est ok
			return : False quand erreur
	"""
	try:
		yt = pytube.YouTube(url)
		yt.streams.get_highest_resolution().download('Video')
	except:
		print("Youtube_Download error")
		return False

	return "Video/" + yt.title + ".mp4"