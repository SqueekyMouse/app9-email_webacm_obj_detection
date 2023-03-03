import cv2
import time
# commit: contours: detect filter get bound draw rect Sec36

video=cv2.VideoCapture(0)
time.sleep(1) # give cam time to load

# get first frame and compare rest against the first
first_frame=None

while True:
    check,frame=video.read() # captures an image
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert to greyscale, no need for bgr complexity for comparing frames algo to cnv image
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0) # blur the image to remove the noise, dont ned that much precision
    #cv2.imshow('my video',gray_frame_gau) #show grey blur img

    if first_frame is None: # get first frame and compare rest against the first
        first_frame=gray_frame_gau

    delta_frame=cv2.absdiff(first_frame,gray_frame_gau) #get the difference matrix
    # cv2.imshow('my video',delta_frame) #show the delta frame

    # cnv del to black and white, ie, remove more noise, #30 or more px to be set as 255
    thresh_frame=cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)[1] #60 looks good
    # cv2.imshow('my video',thresh_frame) 

    dil_frame=cv2.dilate(thresh_frame,None,iterations=2) # remove more noise, more iter more processing
    # cv2.imshow('my video',thresh_frame) 

    # to add frame, detect contours around white areas
    contours,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # to filter out smaller insignificant contours
    for contour in contours:
        # if cv2.contourArea(contour)<10000: # skip small objects
        if cv2.contourArea(contour)<5000: # skip small objects, 5k is better
            continue
        x,y,w,h=cv2.boundingRect(contour) # extract dimensions of obj
        cv2.rectangle(img=frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3) # draw frame on frame

    cv2.imshow('Video',frame)
    key=cv2.waitKey(1) # basically creates a keyboard key obj
    if key==ord('q'): # quit if key q is pressed!!!
        break

video.release()
