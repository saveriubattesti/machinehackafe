from flask import Flask, url_for, send_from_directory, request, send_file
import logging, os
from werkzeug.utils import secure_filename



app = Flask(__name__)

old_fileName = ""

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    if request.method == 'POST' and request.files['image']:
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


if __name__ == "__main__":
    app.run('0.0.0.0')
