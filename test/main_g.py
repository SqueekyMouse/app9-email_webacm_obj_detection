import cv2
import time
from emailing import send_email
import glob
# commit: get list of obj frames and save only middle one Sec37

video=cv2.VideoCapture(0)
time.sleep(1) # give cam time to load

first_frame=None # get first frame and compare rest against the first
status_list=[] # to track obj detection status
count=1
cap_img=[]

while True:
    status=0 # to track obj moving out of frame
    check,frame=video.read() 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0)
    #cv2.imshow('my video',gray_frame_gau) #show grey blur img

    if first_frame is None: # get first frame
        first_frame=gray_frame_gau

    delta_frame=cv2.absdiff(first_frame,gray_frame_gau) #get the difference matrix
    # cv2.imshow('my video',delta_frame) #show the delta frame

    # cnv delta to black and white, ie 30 or more px to be set as 255
    thresh_frame=cv2.threshold(src=delta_frame,thresh=60,maxval=255,type=cv2.THRESH_BINARY)[1] #60 looks good
    # cv2.imshow('my video',thresh_frame) 

    dil_frame=cv2.dilate(thresh_frame,None,iterations=2) # remove more noise, more iter more processing
    # cv2.imshow('my video',thresh_frame) 

    # to add frame, detect contours around white areas
    contours,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours: # to filter out smaller insignificant contours
        if cv2.contourArea(contour)<5000: # skip small objects, 5k is better
            continue
        # this is where we detect a suitable object from cam
        x,y,w,h=cv2.boundingRect(contour) # extract dimensions of obj
        rectangle=cv2.rectangle(img=frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3) # draw frame on frame

        if rectangle.any(): # obj detected, update status
            status=1
            # add frames with objects to the list so we can later get the middle one to email
            cap_img.append(frame)

    status_list.append(status) # list of obj detection statuses
    status_list=status_list[-2:] # status 1 to 0 means obj exited frame

    if status_list[0]==1 and status_list[1]==0: #ie, ob exited frame so send mail
        idx=int(len(cap_img)/2)-1 # get mid index
        cv2.imwrite(filename='images/q.png',img=cap_img[idx]) # save the middle frame from list to file
        cap_img=[] # clear the list
        send_email()

    print(status_list)

    cv2.imshow('Video',frame)
    key=cv2.waitKey(1) # basically creates a keyboard key obj
    if key==ord('q'): # quit if key q is pressed!!!
        break

video.release()
