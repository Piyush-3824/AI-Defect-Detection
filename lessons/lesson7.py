# ==========================================
# Lesson 7 - Color Segmentation
# ==========================================

# Topics Covered:
# 1. BGR to HSV Conversion
# 2. HSV Color Ranges
# 3. Creating a Mask
# 4. Extracting the Required Color
# 5. HSV Trackbars
# 6. Real-Time Color Detection

import cv2
import numpy as np

# ==========================================
# Read the Image
# ==========================================

# Read image from the images folder
image = cv2.imread("../images/luffy.jpg")

# Resize image for better display
image = cv2.resize(image, (600, 400))

# ==========================================
# Topic 1 - Convert BGR to HSV
# ==========================================

# Convert the BGR image into HSV.
# HSV makes color detection much easier
# than the BGR color space.

hsv = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2HSV
)

# ==========================================
# Topic 2 - HSV Color Range
# ==========================================

# Lower HSV values for Blue

lower_blue = np.array([
    100,
    150,
    50
])

# Upper HSV values for Blue

upper_blue = np.array([
    140,
    255,
    255
])

# ==========================================
# Topic 3 - Create Mask
# ==========================================

# Pixels inside the HSV range
# become White (255)
#
# Remaining pixels become
# Black (0)

mask = cv2.inRange(
    hsv,
    lower_blue,
    upper_blue
)

# ==========================================
# Topic 4 - Extract Blue Objects
# ==========================================

# Keep only those pixels
# where the mask is White.

result = cv2.bitwise_and(
    image,
    image,
    mask=mask
)

# ==========================================
# Display Fixed HSV Detection
# ==========================================

# cv2.imshow(
#     "Original Image",
#     image
# )

# cv2.imshow(
#     "Mask",
#     mask
# )

# cv2.imshow(
#     "Blue Objects",
#     result
# )

# ==========================================
# Topic 5 - HSV Trackbars
# ==========================================

# Trackbars help us find the
# correct HSV values interactively.

# Callback function required by OpenCV.
# We don't need to perform any action
# when the slider moves, so we use pass.

def nothing(x):
    pass

# Create Trackbar Window

cv2.namedWindow("Trackbars")

# ==========================================
# Create Trackbars
# ==========================================

# Lower HSV Values

cv2.createTrackbar(
    "LH",
    "Trackbars",
    0,
    179,
    nothing
)

cv2.createTrackbar(
    "LS",
    "Trackbars",
    0,
    255,
    nothing
)

cv2.createTrackbar(
    "LV",
    "Trackbars",
    0,
    255,
    nothing
)

# Upper HSV Values

cv2.createTrackbar(
    "UH",
    "Trackbars",
    179,
    179,
    nothing
)

cv2.createTrackbar(
    "US",
    "Trackbars",
    255,
    255,
    nothing
)

cv2.createTrackbar(
    "UV",
    "Trackbars",
    255,
    255,
    nothing
)

# ==========================================
# Topic 6 - Real-Time Color Detection
# ==========================================

while True:

    # Read Trackbar Positions

    lh = cv2.getTrackbarPos(
        "LH",
        "Trackbars"
    )

    ls = cv2.getTrackbarPos(
        "LS",
        "Trackbars"
    )

    lv = cv2.getTrackbarPos(
        "LV",
        "Trackbars"
    )

    uh = cv2.getTrackbarPos(
        "UH",
        "Trackbars"
    )

    us = cv2.getTrackbarPos(
        "US",
        "Trackbars"
    )

    uv = cv2.getTrackbarPos(
        "UV",
        "Trackbars"
    )

    # Create Lower HSV Array

    lower = np.array([
        lh,
        ls,
        lv
    ])

    # Create Upper HSV Array

    upper = np.array([
        uh,
        us,
        uv
    ])

    # Create Mask using
    # Trackbar Values

    trackbar_mask = cv2.inRange(
        hsv,
        lower,
        upper
    )

    # Extract Required Color

    trackbar_result = cv2.bitwise_and(
        image,
        image,
        mask=trackbar_mask
    )

    # Display Results
    # cv2.imshow(
    #     "Original Image",
    #     image
    # )
    cv2.imshow(
        "Trackbar Mask",
        trackbar_mask
    )

    cv2.imshow(
        "Trackbar Result",
        trackbar_result
    )

    # Press ESC Key to Exit

    key = cv2.waitKey(1)

    if key == 27:
        break

# ==========================================
# End Program
# ==========================================

cv2.destroyAllWindows()