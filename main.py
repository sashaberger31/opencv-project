import cv2
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True)
args = vars(parser.parse_args())
imageBig = cv2.imread(args["image"])
image =cv2.resize(imageBig, (800, 800))
cv2.imshow("Image", image)
cv2.waitKey(0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (7, 7), 5)
cv2.imshow("Blurred", image)
canny = cv2.Canny(image, 100, 120)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
