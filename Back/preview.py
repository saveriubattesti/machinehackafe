import cv2

def get_preview(image_link:str):
	try:
		cap = cv2.VideoCapture(image_link)
		succes, frame = cap.read()
	except:
		succes = False
		raise

	if succes:
		cv2.imwrite('Image/preview.png', frame)
	else:
		print("Error")
		return False

	cv2.destroyAllWindows()


link = input("image link : ")
get_preview(link)