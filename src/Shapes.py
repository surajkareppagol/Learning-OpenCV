import cv2 as cv
import numpy as np

# Drawing Shapes

# Black

#  [[[0 0 0]
#   [0 0 0]
#   [0 0 0]
#   ...
#   [0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]
#   ...

img = np.zeros((500, 500, 3), dtype="uint8")

cv.imshow("Black Frame", img)

# Green

#  [[[  0 255   0]
#   [  0 255   0]
#   [  0 255   0]
#   ...
#   [  0 255   0]
#   [  0 255   0]
#   [  0 255   0]]

#  [[  0 255   0]
#   [  0 255   0]
#   [  0 255   0]
#   ...

img[:] = 0, 255, 0

cv.imshow("Green Frame", img)

img[:] = 255, 255, 255

# Rectangle
cv.rectangle(img, (0, 0), (250, 250), (20, 232, 32), thickness=2)

cv.imshow("Rectangle Frame", img)

# Center
cv.circle(
    img, (img.shape[1] // 2, img.shape[0] // 2), 40, (120, 45, 2), thickness=cv.FILLED
)

cv.imshow("Circle Frame", img)

# Line
cv.line(img, (0, 0), (250, 250), (220, 232, 32), thickness=2)

cv.imshow("Line Frame", img)

# Text
cv.putText(img, "OpenCV", (0, 350), cv.FONT_HERSHEY_DUPLEX, 1.0, (200, 44, 40), 2)

cv.imshow("Text Frame", img)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()
