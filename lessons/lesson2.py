# ==========================================
# Lesson 2 - Pixels, Slicing, Cropping & Resizing
# ==========================================

import cv2

# Read the image from disk
image = cv2.imread("../images/sample.jpg")

# ==========================================
# Topic 1 - Accessing Pixel Values
# ==========================================

# Print the BGR value of the first pixel
print(image[0, 0])

# Print the image dimensions
print(image.shape)

# Display the original image
cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# Topic 2 - Modifying a Single Pixel
# ==========================================

# Change the first pixel to Red
image[0, 0] = [0, 0, 255]

# Print the modified pixel
print(image[0, 0])

# Display the modified image
cv2.imshow("Modified Pixel", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# Topic 3 - Modifying a Region of Pixels
# ==========================================

# Draw a red square
image[0:100, 0:100] = [0, 0, 255]

# Display the modified image
cv2.imshow("Red Square", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# Topic 4 - Drawing Different Shapes
# ==========================================

# Draw a green rectangle
image[50:250, 100:300] = [0, 255, 0]

# Draw a white rectangle
image[100:150, 100:400] = [255, 255, 255]

# Display the image
cv2.imshow("Rectangles", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# Topic 5 - Image Cropping
# ==========================================

# Crop a region from the image
cropped = image[100:500, 150:750]

# Display the cropped image
cv2.imshow("Cropped Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# Topic 6 - Resizing Images
# ==========================================

# Resize the image
resized = cv2.resize(image, (900, 500))

# Print the resized dimensions
print(resized.shape)

# Display the resized image
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()