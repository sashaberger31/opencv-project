import cv2
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True)
args = vars(parser.parse_args())
imageBig = cv2.imread(args["image"])
image =cv2.resize(imageBig, (800, 800))
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlue = cv2.split(image)[0]
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("Gray", imageGray)
cv2.imshow("Blue", imageBlue)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.GaussianBlur(imageGray, (7, 7), 2)
cv2.imshow("Blur", image)
cv2.waitKey(0)
#(T, imageGray) = cv2.threshold(imageGray, 200, 255, cv2.THRESH_BINARY)
#cv2.imshow("Thresh", imageGray)
canny = cv2.Canny(imageGray, 170, 180)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

(countours, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""
(T, img2) = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", img2)
img2 = cv2.GaussianBlur(img2, (5, 5), 0)
cv2.imshow("Blur", img2)
cv2.waitKey(0)
canny2 = cv2.Canny(img2, 100, 120)
cv2.imshow("Canny", canny2)
cv2.waitKey(0)
"""
