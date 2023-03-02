import cv2
import time
# commit: frame comaprision, get delta fame Sec36

video=cv2.VideoCapture(0)
time.sleep(1) # give cam time to load

# get first frame and compare rest against the first
first_frame=None

while True:
    check,frame=video.read() # captures an image
    # convert to greyscale, no need for bgr complexity for comparing frames
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # algo to cnv image
    # blur the image to remove the noise, dont ned that much precision
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0)
    #cv2.imshow('my video',gray_frame_gau) #show grey blur img

    # get first frame and compare rest against the first
    if first_frame is None:
        first_frame=gray_frame_gau

    delta_frame=cv2.absdiff(first_frame,gray_frame_gau) #get the difference matrix
    cv2.imshow('my video',delta_frame) #show the delta frame

    key=cv2.waitKey(1) # basically creates a keyboard key obj
    if key==ord('q'): # quit if key q is pressed!!!
        break

video.release()
