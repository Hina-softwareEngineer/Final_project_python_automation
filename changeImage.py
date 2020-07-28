#! /usr/bin/env python3

import os 
from PIL import Image

dir="./supplier-data/images/"

for name in os.listdir(dir):
  fullname=os.path.join(dir,name)
  im=Image.open(fullname)
  image=im.convert("RGB")
  image.resize((600,400)).save(dir+name[:3]+".jpeg")