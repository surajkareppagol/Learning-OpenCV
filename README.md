# 🤖 Learning OpenCV

Learning OpenCV from [FreeCodeCamp](https://www.youtube.com/@freecodecamp) YouTube channel.

Video: [OpenCV Course](https://www.youtube.com/watch?v=oXlwWbU8l2o)

## Usage

```bash
git clone https://github.com/surajkareppagol/Learning-OpenCV
cd Learning-OpenCV
```

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

To `deactivate` virtual environment.

```bash
deactivate
```

## #️⃣ Code Blocks

`Images.py`

```py
import cv2 as cv

# Images

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()
```

---

`Videos.py`

```py
import cv2 as cv

# Videos

# Pass Integer Value For Web Cam
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    read_success, frame = capture.read()
    cv.imshow("Dog", frame)

    # -215: Assertion Error

    """
  q    = 01110001
  0xFF = 11111111
        ----------
         01110001 -----> q so when do bitwise and operation we get the same value of q
  """

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
```

---

`Resize.py`

```py
import cv2 as cv

# Resizing

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat - Without Resize", img)

scale = 0.75

width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
dimensions = (width, height)

img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
cv.imshow("Cat - With Resize", img)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()


# For Resizing Video Capture Use capture.set(3, width) And capture.set(4, height)
```

---

`Shapes.py`

```py
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
```
