# Handwritten-Digit-Recognition
# MNIST Digit Recognition using CNN

This repository contains a Convolutional Neural Network (CNN) implemented in TensorFlow/Keras for digit recognition using the MNIST dataset. The model is designed to classify handwritten digits (0-9) with high accuracy.

---

## Overview
The MNIST dataset is a benchmark dataset in the field of machine learning and computer vision. It consists of 70,000 grayscale images of handwritten digits, each of size 28x28 pixels. This project utilizes a CNN to achieve accurate classification of these digits.

---

## Features
- **Model Architecture:**
  - Input layer to accept 28x28 grayscale images
  - Convolutional layers with ReLU activation and padding
  - Max-pooling layers to downsample feature maps
  - Dense layers for final classification
  - Dropout for regularization to prevent overfitting

- **Technologies Used:**
  - TensorFlow/Keras
  - Python

---

## Model Architecture
The architecture of the CNN is as follows:
1. Input: 28x28 grayscale images
2. Reshape to (28, 28, 1)
3. Two convolutional layers with 32 filters (3x3 kernel, ReLU activation)
4. MaxPooling layer (2x2 pool size)
5. Two convolutional layers with 64 filters (3x3 kernel, ReLU activation)
6. MaxPooling layer (2x2 pool size)
7. Flatten layer
8. Dense layer with 128 neurons (ReLU activation)
9. Dropout layer (40% dropout)
10. Output layer with 10 neurons (softmax activation for classification)

---

## Requirements
To run this project, you need:
- Python 3.7+
- TensorFlow 2.x
- NumPy
- Matplotlib (optional, for visualization)

Install dependencies using:
```bash
pip install tensorflow numpy matplotlib
```

---

##Usage
1. Clone the Repository
```bash
https://github.com/Cosmic2003/Handwritten-Digit-Recognition.git
```
2.  Navigate to the project directory
```bash
cd Handwritten-Digit-Recognition
```
3. Run the script to train the model
```bash
python cnn_model.py
```
4. Run the script to use GUI app
```bash
python app.py
```
