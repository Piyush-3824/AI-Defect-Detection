import cv2

# Read the image from disk
image = cv2.imread("../images/sample.jpg")

# Print information about the image
print("Type:", type(image))
print("Shape:", image.shape)
print("Data Type:", image.dtype)

# Display the image
cv2.imshow("Sample Image", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
