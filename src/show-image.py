import cv2

image = cv2.imread("./src/images/test.jpeg")

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.imshow("window", image)

cv2.waitKey(0)
cv2.destroyAllWindows()