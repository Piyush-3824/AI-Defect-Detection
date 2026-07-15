# AI-Powered Defect Detection & Quality Inspection

An Industrial AI project using **Computer Vision**, **Deep Learning**, and **YOLO** to automatically detect manufacturing defects from images. This project is being built step by step while learning OpenCV, Machine Learning, and Deep Learning from scratch.

---

# 🚀 Tech Stack

- Python
- OpenCV
- NumPy
- Matplotlib
- Git & GitHub

---

# 📚 Learning Progress

## ✅ Project Setup

- Project structure created
- Virtual environment configured
- Git & GitHub integration
- Repository initialized

---

## 🟢 Lesson 1 - Reading Images

- Reading images using `cv2.imread()`
- Displaying images using `cv2.imshow()`
- Understanding images as NumPy arrays
- Image shape (`Height`, `Width`, `Channels`)
- Understanding pixel representation

---

## 🟢 Lesson 2 - Pixels, Cropping & Resizing

- Accessing pixel values
- Modifying pixel values
- NumPy image indexing
- Image slicing
- Image cropping
- Image resizing using `cv2.resize()`
- Understanding aspect ratio
- Basic interpolation concepts

---

## 🟢 Lesson 3 - Color Spaces

- BGR Color Space
- RGB Color Space
- Grayscale Images
- HSV Color Space
- Color Space Conversion using `cv2.cvtColor()`
- BGR vs RGB
- BGR vs HSV
- Displaying images using Matplotlib
- Splitting Color Channels (`cv2.split()`)
- Merging Color Channels (`cv2.merge()`)

---

## 🟢 Lesson 4 - Image Processing

### Image Filtering

- Gaussian Blur
- Median Blur
- Bilateral Filter

### Thresholding

- Binary Thresholding
- Understanding Threshold Values
- Grayscale to Binary Conversion

### Edge Detection

- Canny Edge Detection
- Lower & Upper Thresholds

### Contours

- Finding Contours using `cv2.findContours()`
- Contour Retrieval Modes
- Contour Approximation
- Drawing Contours using `cv2.drawContours()`

### Morphological Operations

- Structuring Element (Kernel)
- Erosion
- Dilation
- Effect of Kernel Size
- Effect of Iterations

---

## 🟢 Lesson 5 - Image Transformations

### Translation

- Translation Matrix
- Translation along X & Y Axis
- Border Modes & Border Colors
- Image Translation using `cv2.warpAffine()`

### Rotation

- Rotation about Image Center
- Rotation Matrix
- Clockwise & Anti-Clockwise Rotation
- Scaling During Rotation
- Black Border Regions

### Scaling

- Image Resizing
- Scaling Factors (`fx`, `fy`)
- Upscaling & Downscaling
- Importance of Image Resizing in AI Models

### Affine Transformation

- Understanding Affine Transformations
- Source & Destination Points
- Affine Transformation Matrix
- `cv2.getAffineTransform()`
- `cv2.warpAffine()`

### Perspective Transformation

- Camera Perspective Correction
- Four Point Mapping
- Perspective Transformation Matrix
- `cv2.getPerspectiveTransform()`
- `cv2.warpPerspective()`

---

## 🟢 Lesson 6 - Histograms & Image Enhancement

### Histograms

- Understanding Image Histograms
- Pixel Intensity Distribution
- Histogram Calculation using `cv2.calcHist()`
- Plotting Histograms using Matplotlib
- Reading Histogram Graphs
- Low Contrast vs High Contrast Images

### Histogram Equalization

- Image Contrast Enhancement
- Histogram Equalization using `cv2.equalizeHist()`
- Advantages & Limitations

### CLAHE (Contrast Limited Adaptive Histogram Equalization)

- Local Contrast Enhancement
- Contrast Limiting
- Tile Grid Processing
- `cv2.createCLAHE()`
- `clipLimit`
- `tileGridSize`
- `clahe.apply()`

### Histogram Comparison

- Comparing Original Histogram
- Comparing Histogram Equalization
- Comparing CLAHE
- Visual Analysis of Contrast Enhancement

---

# 🔄 Currently Learning

- Color Segmentation

---

# 📅 Upcoming Topics

## OpenCV

- Color Segmentation
- Feature Detection
- Video Processing
- Mini Computer Vision Projects

## AI & Deep Learning

- Dataset Preparation
- PyTorch Fundamentals
- CNN (Convolutional Neural Networks)
- YOLO Object Detection
- Model Training & Evaluation

## Deployment

- FastAPI Backend
- Frontend Dashboard
- Industrial AI Defect Detection System
- Deployment

---

# 🎯 Final Goal

Build a complete **Industrial AI Defect Detection System** capable of detecting manufacturing defects in real time using:

- Computer Vision
- Deep Learning
- YOLO
- FastAPI
- Modern Frontend Technologies

The final system will detect manufacturing defects such as:

- Scratches
- Dents
- Cracks
- Paint Defects
- Surface Anomalies

from car images.

---

# 📂 Project Structure

```text
AI_DEFECT_DETECTION/
│
├── images/
│   └── image.jpg
│
├── lessons/
│   ├── lesson1.py
│   ├── lesson2.py
│   ├── lesson3.py
│   ├── lesson4.py
│   ├── lesson5.py
    ├── lesson6.py

│
├── README.md
├── Working.docx
├── .gitignore
└── requirements.txt
```

---

# 📌 Project Status

### Current Stage

✅ OpenCV Fundamentals (Lessons 1–6 Completed)

### Next Milestone

➡️ Color Segmentation (Lesson 7)

---

# 📈 Learning Roadmap

- ✅ Lesson 1 - Reading Images
- ✅ Lesson 2 - Pixels, Cropping & Resizing
- ✅ Lesson 3 - Color Spaces
- ✅ Lesson 4 - Image Processing
- ✅ Lesson 5 - Image Transformations
- ✅ Lesson 6 - Histograms & Image Enhancement
- ⬜ Lesson 7 - Color Segmentation
- ⬜ Lesson 8 - Feature Detection
- ⬜ Lesson 9 - Video Processing
- ⬜ Mini Computer Vision Projects
- ⬜ PyTorch Fundamentals
- ⬜ CNN (Convolutional Neural Networks)
- ⬜ YOLO Object Detection
- ⬜ Model Training & Evaluation
- ⬜ FastAPI Backend
- ⬜ Frontend Dashboard
- ⬜ Final Industrial AI Defect Detection System

---

# 🖼️ Sample Outputs

Sample outputs from every lesson will be added as the project progresses.

---

# 🎯 Skills Learned

# 🎯 Skills Learned

- Image Reading & Display
- Pixel Manipulation
- Image Cropping & Resizing
- Color Space Conversion
- Image Filtering
- Thresholding
- Edge Detection
- Contour Detection
- Morphological Operations
- Image Transformations
- Histogram Analysis
- Histogram Equalization
- CLAHE (Adaptive Histogram Equalization)
- Image Contrast Enhancement
- Computer Vision Fundamentals
- Industrial AI Pre-processing

---

# 📌 Future Scope

- Real-time Car Defect Detection
- Multi-Camera Inspection System
- Scratch & Dent Classification
- Defect Severity Analysis
- Production Monitoring Dashboard
- Cloud Deployment
- Industrial Automation Integration

---

### ⭐ This repository documents my journey of building a complete Industrial AI Defect Detection System from scratch. Every lesson focuses on understanding the underlying mathematics, algorithms, and implementation details instead of simply using pre-trained models. The goal is to develop strong Computer Vision and Deep Learning fundamentals before building a production-ready Industrial AI system.
