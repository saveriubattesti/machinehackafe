from moviepy.editor import *

def resize_movie(path:str, dimensions:(int,int)):
	"""
		Permet de resize les vidéos aux dimensions donnée (height, width)
		return : False pour erreur
		return : True quand c'est ok
	"""
	try:
		clip = VideoFileClip(path)
		#print(clip.size)
		clip_resized = clip.resize(dimensions)
		clip_resized.write_videofile("Video/movie_resized.mp4") #thread doesn't works
	except:
		print("Error resize_movie")
		return False
	
	return True