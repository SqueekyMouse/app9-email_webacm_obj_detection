import cv2
import time
# commit: opencv image capture Sec36

video=cv2.VideoCapture(0)

check1,frame1=video.read() # captures an image
time.sleep(1) # cam would stay on longer

check2,frame2=video.read() # captures an image
time.sleep(1)

check3,frame3=video.read() # captures an image

print(check3)
print(frame3)# this would e the image captured
# print(frame.shape) #(480, 640, 3)
