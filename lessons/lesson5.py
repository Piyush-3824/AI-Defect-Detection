# ==========================================
# Lesson 5 - Image Transformations
# ==========================================

# Topics Covered:
# 1. Translation
# 2. Rotation
# 3. Scaling
# 4. Affine Transformation
# 5. Perspective Transformation

import cv2
import numpy as np

# ==========================================
# Read the Image
# ==========================================

# Read the image from the images folder.
# cv2.imread() returns the image as a NumPy array.
image = cv2.imread("../images/sample.jpg")

# ==========================================================
# Topic 1 - Translation
# ==========================================================

# Translation means moving an image from one position to another.
#
# Translation Matrix Format:
#
# [1  0  tx]
# [0  1  ty]
#
# tx -> Horizontal Movement (X-axis)
#       +ve = Right
#       -ve = Left
#
# ty -> Vertical Movement (Y-axis)
#       +ve = Down
#       -ve = Up

# translation_matrix = np.float32([
#     [1, 0, 100],      # Move 100 pixels to the Right
#     [0, 1, -50]       # Move 50 pixels Up
# ])

# Apply Translation
#
# warpAffine(
#     source_image,
#     transformation_matrix,
#     (width, height)
# )
#
# NOTE:
# image.shape returns:
# (Height, Width, Channels)
#
# Example:
# image.shape = (720,1280,3)
#
# Therefore,
#
# image.shape[1] -> Width
# image.shape[0] -> Height

# translated = cv2.warpAffine(
#     image,
#     translation_matrix,
#     (image.shape[1], image.shape[0]),
#
#     # Fill newly created empty regions
#     borderMode=cv2.BORDER_CONSTANT,
#
#     # BGR Color
#     borderValue=(255,0,0)
# )

# cv2.imshow("Translated Image", translated)

# ==========================================================
# Topic 2 - Rotation
# ==========================================================

# Rotation rotates the image around a fixed point.

# Find the center of the image
#
# Width  = image.shape[1]
# Height = image.shape[0]
#
# Integer division (//) gives the exact center pixel.

# center = (
#     image.shape[1] // 2,
#     image.shape[0] // 2
# )

# Create Rotation Matrix
#
# Parameters:
#
# center -> Point around which image rotates
#
# angle
# Positive  -> Anti-Clockwise
# Negative  -> Clockwise
#
# scale
# 1.0 -> Original Size
# 0.5 -> Half Size
# 2.0 -> Double Size

# rotation_matrix = cv2.getRotationMatrix2D(
#     center,
#     -45,
#     0.5
# )

# Rotate Image

# rotated = cv2.warpAffine(
#     image,
#     rotation_matrix,
#     (image.shape[1], image.shape[0])
# )

# cv2.imshow("Rotated Image", rotated)

# ==========================================================
# Topic 3 - Scaling
# ==========================================================

# Scaling changes the size of an image.

# Parameters:
#
# None
# Means OpenCV automatically calculates
# the new size using fx and fy.
#
# fx -> Width Scale
# fy -> Height Scale

# scaled = cv2.resize(
#     image,
#     None,
#
#     # 50% Width
#     fx=0.5,
#
#     # 50% Height
#     fy=0.5
# )

# cv2.imshow("Scaled Image", scaled)

# ==========================================================
# Topic 4 - Affine Transformation
# ==========================================================

# Affine Transformation is a combination of:
#
# Translation
# Rotation
# Scaling
# Shearing
#
# It requires THREE points.

# Source Points
#
# Points selected from the original image.

# src_points = np.float32([
#     [50,50],
#     [200,50],
#     [50,200]
# ])

# Destination Points
#
# New positions of those three points.

# dst_points = np.float32([
#     [50,50],
#     [200,50],
#     [150,200]
# ])

# Create Affine Matrix

# affine_matrix = cv2.getAffineTransform(
#     src_points,
#     dst_points
# )

# Apply Affine Transformation

# affine = cv2.warpAffine(
#     image,
#     affine_matrix,
#     (image.shape[1], image.shape[0])
# )

# cv2.imshow("Affine Transformation", affine)

# ==========================================================
# Topic 5 - Perspective Transformation
# ==========================================================

# Perspective Transformation changes the viewing angle
# of the image.
#
# Unlike Affine,
# Perspective requires FOUR points.
#
# Used in:
# • CamScanner
# • Document Scanner
# • Lane Detection
# • Industrial Inspection
# • Bird's Eye View

# Source Points
#
# Four corners from the original image.

src_points = np.float32([
    [100,100],     # Top Left
    [500,100],     # Top Right
    [100,400],     # Bottom Left
    [500,400]      # Bottom Right
])

# Destination Points
#
# New locations of the four corners.

dst_points = np.float32([
    [50,50],
    [550,100],
    [100,450],
    [500,400]
])

# Create Perspective Transformation Matrix

perspective_matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

# Apply Perspective Transformation
#
# NOTE:
#
# Perspective uses:
#
# warpPerspective()
#
# Affine uses:
#
# warpAffine()

perspective = cv2.warpPerspective(
    image,
    perspective_matrix,
    (image.shape[1], image.shape[0])
)

# Display Perspective Result

cv2.imshow(
    "Perspective Transformation",
    perspective
)

# Display Original Image

cv2.imshow(
    "Original Image",
    image
)

# ==========================================
# Wait Until Any Key Is Pressed
# ==========================================

cv2.waitKey(0)

# Close All OpenCV Windows

cv2.destroyAllWindows()