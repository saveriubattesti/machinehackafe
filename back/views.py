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
def my_api():
    return "Test Ma mère"

@app.route('/crop/', methods = ['POST']) 
def crop_video():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST':
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.files['image']
        img_name = secure_filename(img.filename)
        create_new_folder(app.config['UPLOAD_FOLDER'])
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        return send_file(saved_path)
    else:
        return "Where is the image?" 

@app.route('/test/') 
def image():  
    return send_file("cup.png")

@app.route('/api/setURL', methods=['POST'])
def getURL():
    #START CODE RECUP URL
    url = ""
    #END CODE RECUP URL

    my_downloader = mh.Downloader(url)
    path = my_downloader.download()

    if path != False:
        #Donc le fichier est download
        global file_path
        file_path = path

    else:
        return "Bad URL"


    #if not request.json:
    #    return "not a json post"
    #return "json post succeeded"

@app.route('/api/setFormat', methods=['POST'])
def getFormat():
    #START CODE RECUP FORMAT
    myformat = 1
    #END CODE RECUP FORMAT

    global file_path
    list_format = {1: Dimension.INSTAGRAM_CARRE.value, 
                    2: Dimension.INSTAGRAM_VERTICAL.value,
                    3: Dimension.INSTAGRAM_HORIZONTAL.value,
                    4: Dimension.INSTAGRAM_STORY.value,
                    5: Dimension.TIKTOK.value,
                    6: Dimension.YOUTUBE_HORIZONTAL.value,
                    7: Dimension.FACEBOOK_HORIZONTAL.value,
                    8: Dimension.FACEBOOK_CARRE.value}

    if file_path != "":
        my_sizing = mh.Sizing(path, list_format[myformat])
        final_path = my_sizing.resize(output_name="demo") #faire un nom qui se génère automatiquement

        if final_path != False:
            return send_file(final_path)
        else:
            return "Conversion Failed" #plus de données dans la console
    else:
        return "Bad Path"

if __name__ == "__main__":
    app.run('0.0.0.0')
