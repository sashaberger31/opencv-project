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
img2 = np.copy(image)
image = cv2.GaussianBlur(image, (7, 7), 5)
cv2.imshow("Blur", image)
cv2.waitKey(0)
(T, image) = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", image)
canny = cv2.Canny(image, 100, 120)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

(T, img2) = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", img2)
img2 = cv2.GaussianBlur(img2, (5, 5), 0)
cv2.imshow("Blur", img2)
cv2.waitKey(0)
canny2 = cv2.Canny(img2, 100, 120)
cv2.imshow("Canny", canny2)
cv2.waitKey(0)
