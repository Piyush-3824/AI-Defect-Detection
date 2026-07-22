# ==========================================
# Lesson 4 - Image Filtering
# ==========================================

# General Noise
#        │
#        ▼
# Gaussian Blur

# ------------------------

# Salt & Pepper Noise
#        │
#        ▼
# Median Blur

# ------------------------

# General Noise + Preserve Edges
#        │
#        ▼
# Bilateral Filter

import cv2


# ==========================================
# Load Image
# ==========================================

# Read the image from disk
image = cv2.imread("../images/image.jpg")

# Optional Resize
# image = cv2.resize(image, (400, 300))


# ==========================================
# Topic 1 - Gaussian Blur
# ==========================================

# Apply Gaussian Blur
# blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Parameters:
# (5,5) -> Kernel Size
#         Smaller Kernel (3x3)  -> Less Blur
#         Medium Kernel (5x5)   -> Moderate Blur
#         Large Kernel (9x9)    -> More Blur
#         Very Large (15x15+)   -> Heavy Blur
#
# 0 -> Sigma
#      OpenCV automatically calculates Sigma
#
# blurred = cv2.resize(blurred, (600, 400))

# Display Images
# cv2.imshow("Original Image", image)
# cv2.imshow("Gaussian Blur", blurred)


# ==========================================
# Topic 2 - Median Blur
# ==========================================

# Apply Median Blur
# Removes Salt & Pepper Noise

# median = cv2.medianBlur(image, 9)

# Parameters:
# 3  -> Light Noise Removal
# 5  -> Moderate Noise Removal
# 9  -> Strong Noise Removal
# 15 -> Heavy Noise Removal
#
# Kernel Size must always be Odd.

# Display Image
# cv2.imshow("Median Blur", median)


# ==========================================
# Topic 3 - Bilateral Filter
# ==========================================

# Apply Bilateral Filter
# Removes Noise while Preserving Edges

# bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Parameters:
#
# 9
# Diameter (d)
# Number of neighbouring pixels considered.
#
# Smaller d -> Faster, Less Smoothing
# Larger d  -> More Smoothing

# 75
# Sigma Color
# Controls colour similarity.
#
# Smaller Value -> Preserve more colours
# Larger Value  -> More colour smoothing
#
# 75
# Sigma Space
# Controls spatial distance.
#
# Smaller Value -> Nearby pixels only
# Larger Value  -> Distant pixels also influence

# Display Image
# cv2.imshow("Bilateral Filter", bilateral)


# ==========================================
# Topic 4 - Thresholding
# ==========================================

# Convert Image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Binary Threshold

ret, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Parameters:
#
# 127 -> Threshold Value
# Pixels >= 127 become White
# Pixels < 127 become Black
#
# 255 -> Maximum Pixel Value

# Display Images
cv2.imshow("Grayscale", gray)
cv2.imshow("Binary", binary)


# ==========================================
# Topic 5 - Canny Edge Detection
# ==========================================

# Detect Edges

edges = cv2.Canny(gray, 100, 200)

# Parameters:

# 100 -> Lower Threshold
# 200 -> Upper Threshold

# Smaller Thresholds -> More Edges
# Larger Thresholds  -> Fewer Edges

# Display Image
cv2.imshow("Canny Edge Detection", edges)


# Processing Pipeline
#
# Original Image
#       │
#       ▼
# Grayscale
#       │
#       ▼
# Threshold
#       │
#       ▼
# Binary Image
#       │
#       ▼
# Find Contours


# ==========================================
# Topic 6 - Contours
# ==========================================

# Find Contours

contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Contour Retrieval Mode
#
# RETR_EXTERNAL
# Returns only the outermost contours.
#
# CHAIN_APPROX_SIMPLE
# Compresses contour points to save memory.

# Create Copy of Original Image

contour_image = image.copy()

# Print Number of Contours
# print(len(contours))

# Draw Contours

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

# Parameters:
#
# contour_image -> Image on which contours are drawn
# contours      -> List of detected contours
# -1            -> Draw all contours
# (0,255,0)     -> Green Colour (BGR)
# 2             -> Thickness

# Display Image
cv2.imshow("Contours", contour_image)


# ==========================================
# Topic 7 - Morphological Operations
# ==========================================

# Create Structuring Element (Kernel)

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5, 5)
)

# Parameters:
#
# MORPH_RECT
# Creates a Rectangular Kernel.
#
# (5,5)
# Kernel Size
#
# 3x3  -> Less Erosion / Dilation
# 5x5  -> Moderate Erosion / Dilation
# 9x9  -> Strong Erosion / Dilation
# 15x15 -> Very Strong Erosion / Dilation

# ------------------------------------------
# Erosion
# ------------------------------------------

# eroded = cv2.erode(
#     binary,
#     kernel,
#     iterations=1
# )

# Iterations:
#
# 1 -> Apply Once
# 2 -> Apply Twice
# 3 -> Stronger Erosion
# 5 -> Very Strong Erosion
#
# More Iterations
# ↓
# Smaller White Objects

# cv2.imshow("Eroded Image", eroded)


# ------------------------------------------
# Dilation
# ------------------------------------------

dilated = cv2.dilate(
    binary,
    kernel,
    iterations=1
)

# More Iterations
# ↓
# Larger White Objects
#
# Small Gaps Get Filled
# Thin Objects Become Thicker

cv2.imshow("Dilated Image", dilated)


# ==========================================
# Exit Program
# ==========================================

cv2.waitKey(0)
cv2.destroyAllWindows()