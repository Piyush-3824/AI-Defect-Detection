# ==========================================
# Lesson 3 - Color Spaces
# ==========================================

import cv2
import matplotlib.pyplot as plt


# ==========================================
# Topic 1 - BGR to Grayscale
# ==========================================

# Read the image from disk (OpenCV reads images in BGR format)
# image = cv2.imread("../images/sample.jpg")

# # Convert the image from BGR to Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Print the dimensions of both images
# print("Original Image Shape :", image.shape)
# print("Grayscale Image Shape :", gray.shape)

# # Display the original image
# cv2.imshow("Original Image", image)

# # Display the grayscale image
# cv2.imshow("Grayscale Image", gray)

# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()


# ==========================================
# Topic 2 - BGR to RGB
# ==========================================

# Read the image again
# image = cv2.imread("../images/sample.jpg")

# # Convert the image from BGR to RGB
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Print the dimensions
# print("BGR Shape :", image.shape)
# print("RGB Shape :", rgb.shape)

# # Display using OpenCV
# # (Both windows may look almost the same because OpenCV expects BGR.)
# cv2.imshow("Original (BGR)", image)
# cv2.imshow("RGB Image", rgb)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ==========================================
# Topic 3 - BGR vs RGB using Matplotlib
# ==========================================

# # Read the image
# image = cv2.imread("../images/sample.jpg")

# # Convert BGR to RGB
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Display the BGR image using Matplotlib
# # (Colors will appear incorrect because Matplotlib expects RGB.)
# plt.imshow(image)
# plt.title("BGR Image displayed using Matplotlib")
# plt.show()

# # Display the RGB image using Matplotlib
# # (Colors will now appear correct.)
# plt.imshow(rgb)
# plt.title("RGB Image displayed using Matplotlib")
# plt.show()


# ==========================================
# Topic 4 - HSV Color Space
# ==========================================
#
# Theory Topic
#
# HSV stands for:
# H = Hue        (Actual Color)
# S = Saturation (Purity/Richness of the Color)
# V = Value      (Brightness of the Color)
#
# HSV is widely used in Computer Vision for:
# - Color Detection
# - Object Tracking
# - Image Segmentation
#
# No code is required in this topic because we only learned the theory.


# ==========================================
# Topic 5 - BGR to HSV Conversion
# ==========================================

# Read the image
# image = cv2.imread("../images/sample.jpg")

# # Convert the image from BGR to HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # Print the dimensions
# print("BGR Shape :", image.shape)
# print("HSV Shape :", hsv.shape)

# image=cv2.resize(image,(600,400))
# hsv=cv2.resize(hsv,(600,400))
# # Display the original image
# cv2.imshow("Original Image", image)

# # Display the HSV image
# # (The colors may look unusual because OpenCV is displaying HSV values directly.)
# cv2.imshow("HSV Image", hsv)

# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()



# ==========================================
# Topic 6 - Splitting Color Channels
# ==========================================

# import cv2

# Read the image
# image = cv2.imread("../images/sample.jpg")

# # Split the image into Blue, Green and Red channels
# blue, green, red = cv2.split(image)

# # Print the shapes
# print("Original Image Shape :", image.shape)
# print("Blue Channel Shape :", blue.shape)
# print("Green Channel Shape :", green.shape)
# print("Red Channel Shape :", red.shape)

# image=cv2.resize(image,(600,400))
# blue=cv2.resize(blue,(600,400))
# green=cv2.resize(green,(600,400))
# red=cv2.resize(red,(600,400))
# # Display all channels
# cv2.imshow("Original Image", image)
# cv2.imshow("Blue Channel", blue)
# cv2.imshow("Green Channel", green)
# cv2.imshow("Red Channel", red)

# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all windows
# cv2.destroyAllWindows()

# ==========================================
# Topic 7 - Merging Color Channels
# ==========================================

import cv2

# Read the image
image = cv2.imread("../images/sample.jpg")

# Split the image into three channels
blue, green, red = cv2.split(image)

# Merge the three channels back together
merged = cv2.merge((blue, green, red))

# Print the shape of the merged image
print("Merged Image Shape :", merged.shape)

# Display the original image
image=cv2.resize(image,(600,400))
cv2.imshow("Original Image", image)

# Display the merged image
merged=cv2.resize(merged,(600,400))
cv2.imshow("Merged Image", merged)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()