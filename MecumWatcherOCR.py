
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:37:32 2022

@author: awilcox
"""


from PIL import Image
from pytesseract import pytesseract
import pathlib
import numpy as np
import time
import pyodbc
import pandas as pd
import os.path



## ISSUES ###
# text doesn't work on status = "current bid"
# text sold not working??


### Defining paths to tesseract.exe
current_directory = os.getcwd()
path_to_tesseract = str(current_directory) + '\Tesseract-OCR\\tesseract.exe'
# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract


### Load image
# test image path
image_path = str(current_directory) + '\\ScreenShots\\frames27120.jpg'
image = Image.open(image_path).convert('L') # grey scale


# crop image in specific secions for OCR processing
# Boxed by Pixel location
# image.crop((left, top, right, bottom))
    # Use MS Paint to find pixel locations 
image_crop = image.crop((0,0,1200,200))
lot_crop = image.crop((385,70,475,150))
ymm_crop = image.crop((500,70,885,150))
bid_crop = image.crop((940,60,1175,125))
status_crop = image.crop((910,130,1170,160))
sold_crop = image.crop((1200,65,1330,160)).rotate(-20)

  
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
text = pytesseract.image_to_string(image)
text_crop = pytesseract.image_to_string(image_crop)
text_lot = pytesseract.image_to_string(lot_crop).replace('LOT','').replace('$','S').strip()
text_ymm = pytesseract.image_to_string(ymm_crop).replace('\n', ' ').strip()
text_bid = int(pytesseract.image_to_string(bid_crop).replace('\n','').replace(',','').replace('$',''))
text_status = pytesseract.image_to_string(status_crop)
text_sold = pytesseract.image_to_string(sold_crop)


# # Size of the image in pixels (size of original image)
# width, height = image.size
 
# # Setting the points for cropped image
# left = 5
# top = height 
# right = 500
# bottom = height
 
# # Cropped image of above dimension
# image_crop = image.crop((left, top, right, bottom))



# text = pytesseract.image_to_string(img)
# text_grey = pytesseract.image_to_string(img_grey)
# text_crop = pytesseract.image_to_string(img_crop)
# text_crop_grey = pytesseract.image_to_string(img_crop_grey)
# text_straight_crop = pytesseract.image_to_string(img_straight_crop)
# text_straight_crop_grey = pytesseract.image_to_string(img_straight_crop_grey)

# text = pytesseract.run_and_get_output(img)


#text = pytesseract.image_to_string(img, config = '--psm 4 --oem 1 -c tessedit_char_whitelist=ABCDEFG0123456789')