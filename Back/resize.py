import cv2
import numpy as np
from PIL import Image
import imutils


cap = cv2.VideoCapture('Video/b.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
size = (300,700) #largeur hauteur
out = cv2.VideoWriter('output.mp4',fourcc, fps, size)
succes, frame = cap.read()
while succes:
	succes, frame = cap.read()
	try:
		if size[0] > size[1]:
			newImage = imutils.resize(frame, height=(size[1]))
			if newImage.shape[1] > size[0]:
				newImage = imutils.resize(frame, width=(size[0]))
				if newImage.shape[0] > size[1]:
					print("Impossible")
					break
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
		out.write(f)
	except:
		pass

cap.release()
out.release()
cv2.destroyAllWindows()
#print(s, ax, ay)
cv2.imwrite('test.png', newImage)