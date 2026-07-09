# import cv2

# # Read the original image from the images folder
# image = cv2.imread("../images/sample.jpg")

# # Crop a region from the image
# # Syntax:
# # image[row_start:row_end, column_start:column_end]
# cropped = image[100:500, 300:900]

# # Print the shape of the original image
# print("Original Shape :", image.shape)

# # Print the shape of the cropped image
# print("Cropped Shape :", cropped.shape)

# # Resize both images only for display purposes
# display_original = cv2.resize(image, (900, 500))
# display_cropped = cv2.resize(cropped, (600, 400))

# # Display the original image
# cv2.imshow("Original Image", display_original)

# # Display the cropped image
# cv2.imshow("Cropped Image", display_cropped)

# # Wait until any key is pressed
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()

# Cropping Of Image using resize operator

# import cv2

# # Read the image from disk
# image = cv2.imread("../images/sample.jpg")

# # Print the original shape of the image
# print("Original Shape :", image.shape)

# # Resize the image
# # Syntax: cv2.resize(image, (width, height))
# resized = cv2.resize(image, (600, 400))

# # Print the new shape
# print("Resized Shape :", resized.shape)

# # Display both images
# cv2.imshow("Original Image", image)
# cv2.imshow("Resized Image", resized)

# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()

# Distortion Of an Image

# import cv2

# # Read the image
# image = cv2.imread("../images/sample.jpg")

# # Resize while changing the aspect ratio (this will distort the image)
# stretched = cv2.resize(image, (800, 800))

# # Resize to another rectangular size
# normal = cv2.resize(image, (800, 450))

# # Display both images
# cv2.imshow("Stretched Image", stretched)
# cv2.imshow("Normal Resize", normal)

# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all windows
# cv2.destroyAllWindows()


import cv2

# Read the image
image = cv2.imread("../images/sample.jpg")

# Resize while changing the aspect ratio (this will distort the image)
stretched = cv2.resize(image, (200, 200))

# Resize to another rectangular size
normal = cv2.resize(image, (800, 800))

# Display both images
cv2.imshow("Original Image", stretched)
cv2.imshow("Next", normal)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()