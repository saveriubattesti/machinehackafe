#from exif_from_file import *
import resize as rs
import crop as cp

from enum_format import *
import youtube_download as ytd
import facebook_download as fbd
import tiktok_download as ttd
from tinytag import TinyTag
from preview import *
import cv2

class Sizing():

	def __init__(self, path:str, dimension:(int,int)):
		"""
			On peut utiliser l'enumeration de format pour les dimensions :
			INSTAGRAM_CARRE = (600,600)
			INSTAGRAM_VERTICAL = (600,750)
			INSTAGRAM_HORIZONTAL = (600,315)
			INSTAGRAM_STORY = (1080,1920)
			TIKTOK = (1080,1920)
			YOUTUBE_HORIZONTAL = (1280,720)
			FACEBOOK_HORIZONTAL = (1280,720)
			FACEBOOK_CARRE = (640,640)
		"""
		self.path = path
		self.dimension = dimension

	def resize(self, output_name:str="output"):
		return rs.resize(self.path, self.dimension, output_name)

	def crop(self, position:(int,int)=(0,0), output_name:str="output"):
		return cp.crop(self.path, self.dimension, position, output_name)


class Downloader():

	def __init__(self, url:str):
		self.url = url
		self.youtube_download_check = False
		self.facebook_download_check = False
		self.tiktok_download_check = False
		#List of possible name domain

		fb_name_domain = ["facebook", "fb"]
		tiktok_name_domain = ["tiktok"]
		youtube_name_domain = ["youtube", "youtu"]

		url_splited = url.split(".")
		current_name_domain = url_splited[1]

		#check link source
		if current_name_domain in fb_name_domain:
			self.facebook_download_check = True
		elif current_name_domain in tiktok_name_domain:
			self.tiktok_download_check = True
		elif current_name_domain in youtube_name_domain:
			self.youtube_download_check = True
		else:
			print("Error Link")
			return False

	def download(self, name:str="download"):
		if self.facebook_download_check:
			return self.facebook_download(name)
		elif self.tiktok_download_check:
			return self.tiktok_download(name)
		elif self.youtube_download_check:
			return self.youtube_download()
		else:
			print("Can't download")
			return False

	def youtube_download(self):
		if self.youtube_download:
			return ytd.youtube_download(self.url)
		else:
			return False

	def facebook_download(self, name:str="download"):
		if self.facebook_download:
			return fbd.facebook_download(self.url, name)
		else:
			return False

	def tiktok_download(self, name:str="download"):
		if self.tiktok_download:
			return ttd.tiktok_download(self.url, name)
		else:
			return False


class Data():

	def __init__(self, path:str):
		video = TinyTag.get(path)
		self.title = str(video.title) 
		self.artist = str(video.artist) 
		self.genre = str(video.genre) 
		self.year = str(video.year) 
		self.bitrate = str(video.bitrate) 
		self.composer = str(video.composer) 
		self.filesize = str(video.filesize) 
		self.albumartist = str(video.albumartist) 
		self.duration = str(video.duration) 
		self.track_total = str(video.track_total) 

		#dimension
		cap = cv2.VideoCapture(path)
		succes, frame = cap.read()
		(h, w, pixel_size) = frame.shape

		self.dimension = (h,w)
		cap.release()

		#preview
		self.preview = get_preview(path, self.title)
