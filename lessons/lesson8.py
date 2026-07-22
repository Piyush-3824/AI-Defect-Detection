# ==========================================
# Lesson 8 - Feature Detection
# ==========================================

# Topics Covered:
# 1. Understanding Image Features
# 2. Harris Corner Detection
# 3. Shi-Tomasi Corner Detection

import cv2
import numpy as np

# ==========================================
# Read the Image
# ==========================================

# Read image from the images folder

image = cv2.imread("../images/sample.jpg")

# Resize image for better display

image = cv2.resize(
    image,
    (400, 400)
)

# Create separate copies of the image.
# This allows us to display the output of
# different algorithms independently.

harris_image = image.copy()

shi_image = image.copy()

# ==========================================
# Convert Image to Grayscale
# ==========================================

# Most Feature Detection algorithms
# work on Grayscale images because
# color information is not required
# for detecting corners.

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# ==========================================
# Topic 1 - Harris Corner Detection
# ==========================================

# Harris requires the grayscale image
# to be of float32 datatype.

gray_float = np.float32(gray)

# Detect Harris Corners
#
# Parameters:
#
# gray_float -> Input Image
#
# 2 -> Block Size
# Number of neighboring pixels
# considered for corner detection.
#
# 3 -> Sobel Kernel Size
# Used for gradient calculation.
#
# 0.04 -> Harris Detector Constant
# Controls corner sensitivity.

harris_corners = cv2.cornerHarris(
    gray_float,
    2,
    3,
    0.04
)

# Dilate detected corners
#
# Dilate enlarges the detected corner
# regions so they become easier to see.

harris_corners = cv2.dilate(
    harris_corners,
    None
)

# Mark detected corners in Red.
#
# corners.max() gives the strongest
# detected corner.
#
# We keep only corners whose strength
# is greater than 1% of the strongest
# detected corner.

harris_image[
    harris_corners > 0.01 * harris_corners.max()
] = [0, 0, 255]

# ==========================================
# Topic 2 - Shi-Tomasi Corner Detection
# ==========================================

# Detect the best corners.
#
# Parameters:
#
# gray -> Grayscale Image
#
# 50 -> Maximum number of corners
#
# 0.01 -> Quality Level
# Minimum accepted corner quality.
#
# 10 -> Minimum Distance
# Minimum distance between two corners.

shi_corners = cv2.goodFeaturesToTrack(
    gray,
    50,
    0.01,
    10
)

# Convert floating point coordinates
# into integer coordinates because
# pixel locations are integers.

shi_corners = shi_corners.astype(int)

# Draw every detected corner.

for corner in shi_corners:

    # ravel() converts
    #
    # [[x,y]]
    #
    # into
    #
    # [x,y]

    x, y = corner.ravel()

    # Draw a filled Red circle
    # on every detected corner.

    cv2.circle(
        shi_image,
        (x, y),
        5,
        (0, 0, 255),
        -1
    )

# ==========================================
# Display Results
# ==========================================

cv2.imshow(
    "Original Image",
    image
)

cv2.imshow(
    "Harris Corner Detection",
    harris_image
)

cv2.imshow(
    "Shi-Tomasi Corner Detection",
    shi_image
)

# ==========================================
# End Program
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()