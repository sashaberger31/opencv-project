import cv2
import argparse
import numpy as np


def getTrackerFromContour(contours, hierarchy):
    deepest = 0
    depth = 0
    for contourId in range(len(hierarchy[0])):
        newDeepest, newDepth = getDeepest(hierarchy, contourId)
        if newDepth > depth:
            depth = newDepth
            deepest = newDeepest
    if depth>2:
        perimeter = cv2.arcLength(contours[deepest], True)
        approx = cv2.approxPolyDP(contours[deepest], 0.02 * perimeter, True)
        print(len(approx))
    else:
        print("Failed to find a suitable tracker.")



def getDeepest(hierarchy, contourNum):
    """
    Function to find the deepest child contour inside of contourNum and then
    return (the index of) its n-th parent. If the n-th parent is above contourNum,
    return -1
    """

    print(contourNum)
    # We will use a recursive depth-first search
    firstChild = hierarchy[0][contourNum][2]

    if firstChild == -1:
        print(firstChild)
        return (contourNum,1)
    else:
        deepest, depth = getDeepest(hierarchy, firstChild)

    curContour = contourNum
    while True:
        next = hierarchy[0][curContour][0]
        if next != -1:
            newDeepest, newDepth = getDeepest(hierarchy, next)
            print("hihi")
            if newDepth > depth:
                print("reassigning)")
                depth = newDepth
                deepest = newDeepest
        else:
            print("Breaking")
            break
        curContour = next
    return (deepest, depth+1)




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

image = cv2.GaussianBlur(imageGray, (11, 11), 2)
cv2.imshow("Blur", image)
cv2.waitKey(0)
#(T, imageGray) = cv2.threshold(imageGray, 200, 255, cv2.THRESH_BINARY)
#cv2.imshow("Thresh", imageGray)
canny = cv2.Canny(imageGray, 170, 180)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
(contours, hierarchy) = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#create an empty image for contours
img_contours = np.copy(image)

getTrackerFromContour(contours, hierarchy)

# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
cv2.imshow("Contours", img_contours)
cv2.waitKey(0)
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
