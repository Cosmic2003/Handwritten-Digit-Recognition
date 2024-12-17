# Handwritten-Digit-Recognition
# MNIST Digit Recognition using CNN

This repository contains a Convolutional Neural Network (CNN) implemented in TensorFlow/Keras for digit recognition using the MNIST dataset. The model is designed to classify handwritten digits (0-9) with 99.12%
accuracy.

![Screenshot (42)](https://github.com/user-attachments/assets/8cfe2f58-5279-4c19-aab0-643af6ef5b14)


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
3. A convolutional layers with 64 filters (3x3 kernel, ReLU activation)
4. MaxPooling layer (2x2 pool size)
5. Dropout layer (30% dropout)
6. A convolutional layers with 32 filters (3x3 kernel, ReLU activation)
7. MaxPooling layer (2x2 pool size)
8. Dropout layer (30% dropout)
9. Flatten layer
10. Dense layer with 128 neurons (ReLU activation)
11. Dropout layer (50% dropout)
12. Output layer with 10 neurons (softmax activation for classification)

---

## Model Results
1. Loss and accuracy plot for Training Data
   
   ![L AT](https://github.com/user-attachments/assets/8fd27aab-f55a-4bb0-8cc2-475ff22f65f1)
2. Accuracy plot for Training and Test Data
   
   ![ATTe](https://github.com/user-attachments/assets/db406c58-618c-4dc8-9683-0d9d274053f1)
3. Loss and Accuracy Plots
   
   ![L A](https://github.com/user-attachments/assets/cc09f77a-7d89-4edc-b305-dc0e889b4146)
4. Predction Results in GUI
   
   ![Results-GUI](https://github.com/user-attachments/assets/6aba2d2e-2e1e-46da-ad89-8eac82df3446)

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
