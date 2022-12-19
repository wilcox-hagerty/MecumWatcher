
# TO-DO
   # x # Download Youtube Video 
   # x # Capture screenshot every second
    # Crop Screenshot for various info (lotnumber, title, bid, sold_ind)
    # run crop screenshots through OCR
    # build dataframe off OCR data
  
# Fixes
    # write much smaller version of image to take up less space    



# https://www.youtube.com/watch?v=mZ6mzzM5LxU

# https://youtu.be/mZ6mzzM5LxU?t=742



### Capturing images from YouTube videos without downloading Video using Python's VidGear Module
## pip install vidgear
import cv2
from vidgear.gears import CamGear
from PIL import Image


# YouTube stream setup
#options = {"STREAM_RESOLUTION": "720p", "STREAM_PARAMS": {"nocheckcertificate": True}}
stream = CamGear(source='https://youtu.be/mZ6mzzM5LxU?t=379', stream_mode=True, logging=True).start()


#this should be the path where u want ur images
#path  = 'C:\\Users\\user\\Desktop\\Capture Frames from Online YouTube Video\\cars\\'
path  = 'C:\\Users\\awilcox\\OneDrive - Hagerty Group LLC\\Desktop\\Current Work\\Mecum Auction Watcher\\ScreenShots'


# Initialize dataframe for OCR data
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
        cv2.imwrite(name, frame)
        
        # create greyscale of frame
        #image = im.fromarray(frame)

        
        
        # ### Load image
        # # test image path
        # image_path = str(current_directory) + '\\ScreenShots\\frames27120.jpg'
        # image = Image.open(image_path).convert('L') # grey scale


        # # crop image in specific secions for OCR processing
        # # Boxed by Pixel location
        # # image.crop((left, top, right, bottom))
        #     # Use MS Paint to find pixel locations 
        # image_crop = image.crop((0,0,1200,200))
        # lot_crop = image.crop((385,70,475,150))
        # ymm_crop = image.crop((500,70,885,150))
        # bid_crop = image.crop((940,60,1175,125))
        # status_crop = image.crop((910,130,1170,160))
        # sold_crop = image.crop((1200,65,1330,160)).rotate(-20)

          
        # # # Passing the image object to image_to_string() function
        # # # This function will extract the text from the image
        # text = pytesseract.image_to_string(image)
        # text_crop = pytesseract.image_to_string(image_crop)
        # text_lot = pytesseract.image_to_string(lot_crop).replace('LOT','').replace('$','S').strip()
        # text_ymm = pytesseract.image_to_string(ymm_crop).replace('\n', ' ').strip()
        # text_bid = int(pytesseract.image_to_string(bid_crop).replace('\n','').replace(',','').replace('$',''))
        # text_status = pytesseract.image_to_string(status_crop, config = '--psm 7').replace('\n','')
        # text_sold = pytesseract.image_to_string(sold_crop, config = '--psm 9').replace('\n','')

        
    
    currentframe += 1 ## increment up frames
  
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
stream.stop()