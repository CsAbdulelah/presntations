import cv2
import numpy as np

img = cv2.imread('img/edge.jpg',0)
edges = cv2.Canny(img,100,400)
cv2.imshow('pic1', edges); cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
