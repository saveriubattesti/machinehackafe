import cv2
import numpy as np
from PIL import Image
import imutils
from moviepy.editor import *
import os

def crop(path:str, size:(int,int), position:(int,int), output_name:str):
	"""
		crop une vidéo
		return false => erreur
		return "le chemin de la vidéo crop" => pas erreur
	"""
	cap = cv2.VideoCapture(path)

	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	fps = cap.get(cv2.CAP_PROP_FPS)

	out = cv2.VideoWriter('output/' + output_name + '_temp.mp4',fourcc, fps, size)

	print(path, os.path.exists(path))
	succes, frame = cap.read()
	(height, width, pixel_size) = frame.shape

	ay = position[0] #largeur
	ax = position[1] #hauteur

	#pixel restant check
	if (width - size[0] - ay < 0) or (height - size[1] - ax < 0):
		print("Error size")
		return False

	while succes:
		succes, frame = cap.read()
		try:
			#Select only the good part
			newImage = frame[ax:ax+size[1], ay:ay+size[0]]

			out.write(newImage)
		except:
			pass

	#cv2.imwrite('test.png', newImage)
	cap.release()
	out.release()
	cv2.destroyAllWindows()

	#Ajout de l'audio
	try:
		audio = VideoFileClip(path).audio
		video = VideoFileClip('output/' + output_name + '_temp.mp4')
		final = video.set_audio(audio)
		final.write_videofile("output/" + output_name + ".mp4")
	except:
		print("Erreur audio")
		return False

	#On retourne le path
	return "output/" + output_name + ".mp4"