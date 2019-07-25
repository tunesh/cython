from AmazonApi import text_recognition
from centroidtracker import CentroidTracker 
from trackableobject import TrackableObject
from resize_as import image_resize
from text_detection_video import *

# %%writefile main_2.py
def main():
    start = time.time()
    text_detection_amazonapi('frozen_east_text_detection.pb', 'rtsp://admin:mintm1234@192.168.0.64:554/Streaming/Channels/101', 0.5, 320, 320)
    duration = time.time() - start
    print(duration)
 
 
if __name__ == '__main__':
    main()