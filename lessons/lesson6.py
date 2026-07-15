import cv2
import matplotlib.pyplot as plt

# ==========================================
# Lesson 7 - Histogram Equalization & CLAHE
# ==========================================

# Read the image
image = cv2.imread("../images/image.jpg")

# Convert the image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ==========================================
# Topic 1 - Histogram Equalization
# ==========================================

# Improve the overall contrast of the image
equalized = cv2.equalizeHist(gray)

# ==========================================
# Topic 2 - CLAHE
# ==========================================

# Create CLAHE object
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

# Apply CLAHE
clahe_image = clahe.apply(gray)

# ==========================================
# Topic 3 - Histograms
# ==========================================

# Histogram of Original Image
hist_original = cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0, 256]
)

# Histogram of Equalized Image
hist_equalized = cv2.calcHist(
    [equalized],
    [0],
    None,
    [256],
    [0, 256]
)

# Histogram of CLAHE Image
hist_clahe = cv2.calcHist(
    [clahe_image],
    [0],
    None,
    [256],
    [0, 256]
)

# ==========================================
# Display Images
# ==========================================

cv2.imshow("Original Grayscale", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.imshow("CLAHE", clahe_image)

# ==========================================
# Plot Histograms
# ==========================================

plt.figure(figsize=(12,6))

plt.plot(hist_original, color="blue", label="Original")

plt.plot(hist_equalized, color="red", label="Equalized")

plt.plot(hist_clahe, color="green", label="CLAHE")

plt.title("Histogram Comparison")

plt.xlabel("Pixel Intensity")

plt.ylabel("Number of Pixels")

plt.xlim([0,256])

plt.grid(True)

plt.legend()

plt.show()

# ==========================================
# End Program
# ==========================================

cv2.waitKey(0)
cv2.destroyAllWindows()