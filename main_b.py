import cv2
import time
# commit: opencv continous image capture and display Sec36

video=cv2.VideoCapture(0)
time.sleep(1) # give cam time to load

while True:
    #time.sleep(1) # basically 1 frame per sec
    check,frame=video.read() # captures an image
    cv2.imshow('my video',frame) # this need to be in while loop
    # print(frame)

    key=cv2.waitKey(1) # basically creates a keyboard key obj
    if key==ord('q'): # quit if key q is pressed!!!
        break

video.release()
