from enum import Enum


class Dimension(Enum):
	"""Enumeration des dimensions propre a chaque réseau social."""
	INSTAGRAM_CARRE = (600,600)
	INSTAGRAM_VERTICAL = (600,750)
	INSTAGRAM_HORIZONTAL = (600,315)
	INSTAGRAM_STORY = (1080,1920)
	TIKTOK = (1080,1920)
	YOUTUBE_HORIZONTAL = (1280,720)
	FACEBOOK_HORIZONTAL = (1280,720)
	FACEBOOK_CARRE = (640,640)


#resizing interpolation
#resizing processing without écrasment