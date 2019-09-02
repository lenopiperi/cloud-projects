# Copyright 2018 Google LLC

import os
from flask import Flask
from google.cloud import storage
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_blob(file, filename):

	bucket_name = 'reading-writing-cloud-storage.appspot.com' #enhancement idea: get this value from the environment
	storage_client = storage.Client()
	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.blob(filename) #bug
	blob.upload_from_file(file)
	return 'check your bucket!!!'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_blob(file, filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Your file has been uploaded' #enhancement idea: redirect to your uploaded file either through a link or buy opening the uploaded file
            #add way to submit a new file

    return form.html



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]