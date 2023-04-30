from flask import Flask, request, send_file, send_from_directory
from firebase_admin import credentials, initialize_app, storage
import os
import subprocess
import io

app = Flask(__name__)
app.debug = True

# Initialize Firebase
cred = credentials.Certificate("firebase/serviceAccountKey.json")
initialize_app(cred, {'storageBucket': 'dh-workshop-8aaf6.appspot.com'})

# Get a reference to Firebase Storage
bucket = storage.bucket()


### helpers

def improve_img():
    cmd = ['python', '../GFPGAN/inference_gfpgan.py', '-i', 'temp/upload.jpg', '-o', 'RESULTS'] 
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

### endpoints 

# todo: what decorator goes here?
def upload_img():

    file = pass # todo: what goes here?

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    extention = file.filename.split(".")[-1]
    if extention not in ALLOWED_EXTENSIONS:
        return "invalid file extention"
    
    file_name = os.path.join("temp",file.name+"."+extention)   
    file.save(file_name)

    id = '3' # random id generate

    blob = bucket.blob(id)
    blob.upload_from_filename(file_name)

    # todo: do we need to call anything?

    blob = bucket.blob("new_"+id)
    new_file_name = os.path.join("RESULTS","restored_imgs",file.name+"."+extention) 
    blob.upload_from_filename(new_file_name)

    #os.remove(file_name)
    # change later

    return id


# todo: what goes here?
def get_new_img():
    id = # todo: and here?
    blob = bucket.get_blob('new_'+id)

    if blob is not None:
        image_data = blob.download_as_bytes()
        content_type = blob.content_type

        return send_file(
            io.BytesIO(image_data),
            mimetype=blob.content_type, 
            download_name=blob.name+"."+blob.content_type.split("/")[-1],
            as_attachment=True
            )

    else:
        return f'Error: Blob {blob_id} not found'

