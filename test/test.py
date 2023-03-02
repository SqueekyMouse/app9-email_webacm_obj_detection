import cv2
#commit: img opencv read create as array Sec36

array=cv2.imread('res/image.png')

# print(type(array))
print(array.shape) # get dimensions of the array!!!
#(3, 4, 3) 3px vertical, 4px horiz, 3channels bgr!!!
# opencv uses bgr!!!
print(array)# this is a 3*4 pixel img so 12 px, real pics have millons of px!!!
