import sys
import os
import re
import requests as r
import wget

def facebook_download(url:str, name:str):
    """Download a facebook video
        return path when it's ok
        return False when error
    """
    ERASE_LINE = '\x1b[2K'
    try:
        html = r.get(url)
        hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
        hd_url = hdvideo_url.replace('hd_src:"', '')
        wget.download(hd_url, "Video/" + name + ".mp4")
        sys.stdout.write(ERASE_LINE)
    except:
        print("Error facebook download")
        return False
    
    return "Video/" + name + ".mp4"