import cv2
import numpy
#commot: create img using numpy array manually

a=numpy.array(
    [[[255, 0, 0],
      [255, 255, 255],
      [255, 255, 255],
      [187, 41, 160]],

     [[255, 255, 255],
      [255, 255, 255],
      [255, 255, 255],
      [255, 255, 255]],

     [[255, 255, 255],
      [0,   0,  0],
      [47, 255, 173],
      [255, 255, 255]]]
)

cv2.imwrite('img.png',a)