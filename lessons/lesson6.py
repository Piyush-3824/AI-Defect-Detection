# ==========================================
# Lesson 6 - Histograms & Image Enhancement
# ==========================================

# Topics Covered:
# 1. Image Histogram
# 2. Histogram Calculation
# 3. Histogram Interpretation
# 4. Histogram Equalization
# 5. CLAHE (Contrast Limited Adaptive Histogram Equalization)

import cv2
import matplotlib.pyplot as plt

# ==========================================
# Read the Image
# ==========================================

# Read image from images folder
image = cv2.imread("../images/image.jpg")

# Histogram Equalization and CLAHE work only on
# grayscale images.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ==========================================================
# Topic 1 - Histogram Calculation
# ==========================================================

# Calculate Histogram
#
# cv2.calcHist(
#     images,
#     channels,
#     mask,
#     histSize,
#     ranges
# )

hist_original = cv2.calcHist(
    [gray],        # Source Image
    [0],           # Grayscale Channel
    None,          # Entire Image
    [256],         # Number of Bins
    [0,256]        # Pixel Range
)

# ==========================================================
# Topic 2 - Histogram Equalization
# ==========================================================

# Improve the overall contrast
# of the grayscale image.

equalized = cv2.equalizeHist(gray)

# Histogram of Equalized Image

hist_equalized = cv2.calcHist(
    [equalized],
    [0],
    None,
    [256],
    [0,256]
)

# ==========================================================
# Topic 3 - CLAHE
# ==========================================================

# Create CLAHE Object
#
# clipLimit
# Controls maximum contrast.
#
# tileGridSize
# Divides image into
# small tiles.

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

# Apply CLAHE

clahe_image = clahe.apply(gray)

# Histogram of CLAHE Image

hist_clahe = cv2.calcHist(
    [clahe_image],
    [0],
    None,
    [256],
    [0,256]
)

# ==========================================================
# Display Images
# ==========================================================

cv2.imshow("Original", gray)

cv2.imshow(
    "Histogram Equalization",
    equalized
)

cv2.imshow(
    "CLAHE",
    clahe_image
)

# ==========================================================
# Plot Histograms
# ==========================================================

# Create Graph Window

plt.figure(figsize=(12,6))

# Original Histogram

plt.plot(
    hist_original,
    color="blue",
    label="Original"
)

# Histogram Equalization

plt.plot(
    hist_equalized,
    color="red",
    label="Equalized"
)

# CLAHE Histogram

plt.plot(
    hist_clahe,
    color="green",
    label="CLAHE"
)

# Graph Title

plt.title("Histogram Comparison")

# X-axis Label

plt.xlabel("Pixel Intensity")

# Y-axis Label

plt.ylabel("Number of Pixels")

# X-axis Range

plt.xlim([0,256])

# Show Grid

plt.grid(True)

# Display Labels

plt.legend()

# Show Graph

plt.show()

# ==========================================
# End Program
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()