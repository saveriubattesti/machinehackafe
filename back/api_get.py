from flask import Flask, url_for, send_from_directory, request, send_file
import logging, os
from werkzeug.utils import secure_filename

import machinehackafe as mh
from enum_format import *


app = Flask(__name__)

old_fileName = ""

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


file_path = ""

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route('/')
def helloworld():
    return "API HACKAFE"

@app.route('/api/resize', methods=['GET'])
def resizefromurl():
    #args : url, format
    url = request.args.get('url')
    myformat = int(request.args.get('format'))

    my_downloader = mh.Downloader(url)
    path = my_downloader.download()

    if path != False:
        #file dl here
        list_format = {1: Dimension.INSTAGRAM_CARRE.value, 
                        2: Dimension.INSTAGRAM_VERTICAL.value,
                        3: Dimension.INSTAGRAM_HORIZONTAL.value,
                        4: Dimension.INSTAGRAM_STORY.value,
                        5: Dimension.TIKTOK.value,
                        6: Dimension.YOUTUBE_HORIZONTAL.value,
                        7: Dimension.FACEBOOK_HORIZONTAL.value,
                        8: Dimension.FACEBOOK_CARRE.value}

        print(myformat, type(myformat), list(list_format.keys()))
        if myformat not in list(list_format.keys()):
            return "Bad Format"

        my_sizing = mh.Sizing(path, list_format[myformat])
        final_path = my_sizing.resize(output_name="demo") #faire un nom qui se génère automatiquement

        if final_path != False:
            return send_file(final_path)
        else:
            return "Conversion Failed" #plus de données dans la console

        #myPreview = mh.Data(path).preview
        #return myPreview #path of preview
    else:
        return "Bad URL"

@app.route('/api/crop', methods=['GET'])
def cropfromurl():
    #args : url, format
    url = request.args.get('url')
    myformat = request.args.get('format')
    cropPos = (int(request.args.get('pos_x')),int(request.args.get('pos_y')))

    my_downloader = mh.Downloader(url)
    path = my_downloader.download()

    if myformat == None:
        myformat = (int(request.args.get('format_x')),int(request.args.get('format_y')))
    else:
        myformat = int(myformat)

    if path != False:
        #file dl here
        list_format = {1: Dimension.INSTAGRAM_CARRE.value, 
                        2: Dimension.INSTAGRAM_VERTICAL.value,
                        3: Dimension.INSTAGRAM_HORIZONTAL.value,
                        4: Dimension.INSTAGRAM_STORY.value,
                        5: Dimension.TIKTOK.value,
                        6: Dimension.YOUTUBE_HORIZONTAL.value,
                        7: Dimension.FACEBOOK_HORIZONTAL.value,
                        8: Dimension.FACEBOOK_CARRE.value}

        print(myformat, type(myformat), list(list_format.keys()))
        if myformat not in list(list_format.keys()) and type(myformat) == int:
            return "Bad Format"
        if type(myformat) == int:
            my_sizing = mh.Sizing(path, list_format[myformat])
        else:
            my_sizing = mh.Sizing(path, myformat)
        final_path = my_sizing.crop(cropPos, output_name="demo") #faire un nom qui se génère automatiquement

        if final_path != False:
            return send_file(final_path)
        else:
            return "Conversion Failed" #plus de données dans la console

        #myPreview = mh.Data(path).preview
        #return myPreview #path of preview
    else:
        return "Bad URL"
@app.route('/api/preview', methods=['GET'])
def getPreview():
    url = request.args.get('url')
    my_downloader = mh.Downloader(url)
    path = my_downloader.download()
    if path != False:
        data = mh.Data(path)
        return send_file(data.preview)

@app.route('/api/meta', methods=['GET'])
def getMeta():
    url = request.args.get('url')
    my_downloader = mh.Downloader(url)
    path = my_downloader.download()

    if path != False:
        meta = mh.Data(path)
        json = {"title": meta.title,
                "artist": meta.artist,
                "genre": meta.genre,
                "year": meta.year,
                "bitrate": meta.bitrate,
                "composer": meta.composer,
                "filesize": meta.filesize,
                "albumartist": meta.albumartist,
                "duration": meta.duration,
                "track_total": meta.track_total,
                "albumartist": meta.albumartist,
                "dimension": meta.dimension,
                "preview": meta.preview
                }
        return json


if __name__ == "__main__":
    app.run('0.0.0.0')
