#!/usr/bin/env python3

import requests
import os
from PIL import Image
url="http://35.222.147.153/upload/"
dir="./supplier-data/images/"

for images in os.listdir(dir):
  fullname=os.path.join(dir, images)
  im=Image.open(fullname)
  if im.format=='JPEG':
    with open(fullname, 'rb') as opened:
        r=requests.post(url, files={'file': opened})