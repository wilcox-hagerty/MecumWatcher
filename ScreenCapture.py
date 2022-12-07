
# TO-DO
   # x # Download Youtube Video 
   # x # Capture screenshot every second
    # Crop Screenshot for various info (lotnumber, title, bid, sold_ind)
    # run crop screenshots through OCR
    # build dataframe off OCR data
    



# https://www.youtube.com/watch?v=mZ6mzzM5LxU

# https://youtu.be/mZ6mzzM5LxU?t=742



### Capturing images from YouTube videos without downloading Video using Python's VidGear Module
## pip install vidgear
import cv2
from vidgear.gears import CamGear

# YouTube stream setup
#options = {"STREAM_RESOLUTION": "720p", "STREAM_PARAMS": {"nocheckcertificate": True}}
stream = CamGear(source='https://youtu.be/mZ6mzzM5LxU?t=379', stream_mode=True, logging=True).start()


#this should be the path where u want ur images
#path  = 'C:\\Users\\user\\Desktop\\Capture Frames from Online YouTube Video\\cars\\'
path  = 'C:\\Users\\awilcox\\OneDrive - Hagerty Group LLC\\Desktop\\Current Work\\Mecum Auction Watcher\\ScreenShots'

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
        print ('Creating...' + name) 
        
        cv2.imwrite(name, frame)
        
    
    currentframe += 1 ## increment up frames
  
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
stream.stop()