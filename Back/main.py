import machinehackafe as mh
from enum_format import *
import os
import time
import threading
#EXEMPLE

#youtube_url = "https://www.youtube.com/watch?v=frUwcVqN0Vc"

url = input("URL : ")
my_downloader = mh.Downloader(url)
path = my_downloader.download()
#path = os.path.abspath(path).replace("\\","/")

#print(threading.enumerate()) 
if path != False: #False = Error
	#my_sizing = mh.Sizing(path, Dimension.FACEBOOK_CARRE.value)
	#my_sizing.resize(output_name="RESIZED FILE 2")


	data = mh.Data(path)
	print(data.genre)