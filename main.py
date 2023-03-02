import cv2
import time
# commit: opencv continous image capture, greyscale Sec36

video=cv2.VideoCapture(0)
time.sleep(1) # give cam time to load

while True:
    check,frame=video.read() # captures an image
    # convert to greyscale, no need for bgr complexity for comparing frames
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # algo to cnv image
    # blur the image to remove the noise, dont ned that much precision
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0)
    cv2.imshow('my video',gray_frame_gau) 

    key=cv2.waitKey(1) # basically creates a keyboard key obj
    if key==ord('q'): # quit if key q is pressed!!!
        break

video.release()
