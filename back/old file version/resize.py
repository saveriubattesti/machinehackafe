import cv2
import numpy as np
from PIL import Image
import imutils
from moviepy.editor import *
import os

def resize(path:str, size:(int,int), output_name:str):
	"""
		resize une vidéo
		return false => erreur
		return "le chemin de la vidéo resize" => pas erreur
	"""
	cap = cv2.VideoCapture(path)

	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	fps = cap.get(cv2.CAP_PROP_FPS)
	#size = (800,500) #largeur hauteur
	out = cv2.VideoWriter('output/' + output_name + '_temp.mp4',fourcc, fps, size)
	succes, frame = cap.read()
	while succes:
		succes, frame = cap.read()
		try:
			if size[0] >= size[1]:
				newImage = imutils.resize(frame, height=(size[1]))
				if newImage.shape[1] > size[0]:
					newImage = imutils.resize(frame, width=(size[0]))
					if newImage.shape[0] > size[1]:
						print("Error Shape")
						return False
			else:
				newImage = imutils.resize(frame, width=(size[0]))

			#Getting the bigger side of the image
			#s = max(newImage.shape[0:2])
			#Creating a dark square with NUMPY  
			f = np.zeros((size[1],size[0],3),np.uint8)

			#Getting the centering position
			ax,ay = (size[0] - newImage.shape[1])//2,(size[1] - newImage.shape[0])//2

			#Pasting the 'image' in a centering position
			f[ay:newImage.shape[0]+ay,ax:ax+newImage.shape[1]] = newImage
			#print(type(f))
			#cv2.imshow("IMG",f)
			#input()
			#b = cv2.resize(newImg, size)
			#print(type(f))
			out.write(f)
		except:
			pass

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
		raise
		print("Erreur audio")
		return False

	#On retourne le path
	return "output/" + output_name + ".mp4"
