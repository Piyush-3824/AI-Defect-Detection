# ==========================================
# Lesson 1 - Reading and Displaying Images
# ==========================================

import cv2

# ==========================================
# Topic 1 - Reading an Image
# ==========================================

# Read the image from disk.
# cv2.imread() returns a NumPy array.
image = cv2.imread("../images/sample.jpg")

# Print the complete NumPy array
print(image)

# Print the type of the returned object
print(type(image))

# Print the dimensions of the image
print(image.shape)

# ==========================================
# Topic 2 - Displaying an Image
# ==========================================

# Display the image in a new window
cv2.imshow("Original Image", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()