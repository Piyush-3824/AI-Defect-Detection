import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Could not load the image.")
else:
    print("Type:", type(image))
    print("Shape:", image.shape)
    print("Data Type:", image.dtype)

    cv2.imshow("Sample Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()