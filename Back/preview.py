import cv2

def get_preview(video_link:str, name:str):
	try:
		cap = cv2.VideoCapture(video_link)
		succes, frame = cap.read()
	except:
		succes = False
		raise

	if succes:
		cv2.imwrite('Image/' + name + '.png', frame)
	else:
		print("Error")
		return False

	cv2.destroyAllWindows()

	return 'Image/' + name + '.png'
