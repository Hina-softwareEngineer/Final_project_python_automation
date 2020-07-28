#!/usr/bin/env python3

import requests
import os


dir="./supplier-data/descriptions/"
fruit = {}


for name in os.listdir(dir):
    with open(dir+name) as file:
            line = file.readlines()
            print(dir+name)
            fruit={"name":line[0].strip(), "weight" : int(line[1].strip().replace(" lbs",'')),"description": line[2].strip(), "image_name": name[:3]+".jpeg"}
            response=requests.post("http://35.222.147.153/fruits/", json=fruit)
            print(response.status_code)
            

print(fruit)