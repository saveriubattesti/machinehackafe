from TikTokApi import TikTokApi

def tiktok_download(url:str):
	""" Download a tiktok video
		return False when error
		return True when succes
	"""
	api = TikTokApi.get_instance()
	try:
		my_tiktok = api.get_Video_By_Url(url, return_bytes=0, custom_verifyFp="")
	except:
		print("Error tiktok download")
		return False

	with open("Video/tiktok_download.mp4", "wb") as file:
		file.write(my_tiktok)

	return True