import firebase_admin
import glob
from PIL import Image
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'serviceAccountKey.json'

client = storage.Client()
bucket = client.get_bucket('firepy-92edd.appspot.com')

for filename in glob.glob('files/*.jpg'):
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    print(blob.public_url)
