# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:53:40 2022

@author: awilcox
"""


# TO-DO
   # x # Download Youtube Video 
   # x # Capture screenshot every second
    # Crop Screenshot for various info (lotnumber, title, bid, sold_ind)
    # run crop screenshots through OCR
    # build dataframe off OCR data
  
# Fixes
    # write much smaller version of image to take up less space  
    # Why is the image show up as blue when converted from array
    # If sold, add premium
    # skip frame if "Lot" not found in lot number text
    # Maybe crop image down before running it through loop. Its 1920x1080 currently


# Train model to better recognize text



# https://www.youtube.com/watch?v=mZ6mzzM5LxU

# https://youtu.be/mZ6mzzM5LxU?t=742





### Capturing images from YouTube videos without downloading Video using Python's VidGear Module
## pip install vidgear
import cv2
from vidgear.gears import CamGear

import os.path
from pytesseract import pytesseract
from PIL import Image
import pandas as pd



### Defining paths to tesseract.exe
current_directory = os.getcwd()
path_to_tesseract = str(current_directory) + '\Tesseract-OCR\\tesseract.exe'
# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract


# YouTube stream setup
#options = {"STREAM_RESOLUTION": "720p", "STREAM_PARAMS": {"nocheckcertificate": True}}
#stream = CamGear(source='https://youtu.be/mZ6mzzM5LxU', stream_mode=True, logging=True).start()

# test video
stream = CamGear(source='https://youtu.be/HkqKdWJEd4k', stream_mode=True, logging=True).start()

#this should be the path where u want ur images
#path  = 'C:\\Users\\user\\Desktop\\Capture Frames from Online YouTube Video\\cars\\'
path  = 'C:\\Users\\awilcox\\OneDrive - Hagerty Group LLC\\Desktop\\Current Work\\Mecum Auction Watcher\\ScreenShots'


# Initialize list for OCR data
MecumOCR = []


# choose how many seconds to skip in between screen shots
# Mecum auctions are 60 frames per second usually
framerate = stream.framerate # finds framerate of stream
secondskip = framerate*2
 
currentframe = 0
while True:

    frame = stream.read() ### using functions from vidGear module
    if frame is None:
        break
    
    #cv2.imshow("Output Frame", frame) # optional if u want to show the frames
    
    if currentframe % secondskip == 0:
        name = path + './frames' + str(currentframe) + '.jpg'
        print ('Analyzing...' + name) 
        
        # save frame for testing
        cv2.imwrite(name, frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        
        # create greyscale of frame
        image = Image.fromarray(frame).convert('L')
        
        # Text from cropped images run through specific OCR configs
        # Only run ocr on frame if Lot number is found. Add found text to the dataframe
        if 'lot' in pytesseract.image_to_string(image.crop((380,70,480,155))).lower():
            MecumOCR.append(
                {
                    'FrameName': 'frames' + str(currentframe)
                    # Cropped images are boxed by pixel locations --- image.crop((left, top, right, bottom))
                    ,'LotNumber': pytesseract.image_to_string(image.crop((380,70,480,155))).replace('LOT','').replace('$','S').strip()
                    ,'YMM': pytesseract.image_to_string(image.crop((490,70,885,155))).replace('\n', ' ').strip()
                    ,'HighBid': pytesseract.image_to_string(image.crop((940,60,1170,125)), config = '-c tessedit_char_whitelist="0123456789"').replace('\n','')
                    ,'LotStatus': pytesseract.image_to_string(image.crop((910,130,1170,160)), config = '--psm 7 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ "').replace('\n','')
                    ,'SoldInd': 'sold' in pytesseract.image_to_string(image.crop((1200,65,1330,160)).rotate(-20), config = '--psm 9 -c tessedit_char_whitelist="sold"').lower()
                    }
                )
            
            MecumOCRdf = pd.DataFrame(MecumOCR)
        
    
    currentframe += 1 ## increment up frames
  
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
stream.stop()