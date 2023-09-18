'''
TODO:
1. type in cmd py JPTtoPNGconverter.py (2 args - 1 folder name [ie Pokedex/], 2 folter name to create [ie new/])
'''
import sys
import os
from PIL import Image

## grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

## check if new/ exists, if not, create it
if not os.path.exists(output_folder):
  os.mkdir(output_folder)

## loop through Pokedex
# print(os.listdir(image_folder)) # lists contents of the folder
for filename in os.listdir(image_folder):
  ## convert images to png
  img = Image.open(f"{image_folder}{filename}")
  ## save to the new folder
  clean_name = os.path.splitext(filename)[0] # splits the file names into a tuple
  # print(clean_name[0])
  img.save(f"{output_folder}{clean_name}.png", 'png')
  print('all done!')