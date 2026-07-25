# 🎨 ColorSense AI

## Project Description

ColorSense AI is a real-time color recognition project developed using Python and OpenCV. The application captures live video from a webcam, detects colored objects, and displays the detected color by drawing a bounding box with the corresponding color name.

---

## Technologies Used

- Python
- OpenCV
- NumPy

---

## Supported Colors

- 🔴 Red
- 🟢 Green
- 🔵 Blue
- 🟡 Yellow

---

## 📝 Project Steps

1. Created the project using Python and OpenCV.
2. Captured live video from the webcam.
3. Converted each frame from BGR to HSV color space.
4. Applied HSV color ranges to detect Red, Green, Blue, and Yellow.
5. Detected the colored objects and displayed the results in real time.

---

## ⚙️ How It Works

The webcam continuously captures video frames. Each frame is converted to the HSV color space, where predefined color ranges are used to identify the supported colors. Once a color is detected, the program locates the object, draws a bounding box around it, and displays the color name on the screen.

---

## How to Run

1. Install the required libraries.
pip install -r requirements.txt

2. Run the project.
python color_recognition.py

3. Show a red, green, blue, or yellow object in front of the webcam.

4. Press Q to close the application.

---

## 📸 Project Results

### 🔴 Red Detection
<img width="1916" height="1075" alt="red" src="https://github.com/user-attachments/assets/938ca054-ebad-4b69-aae2-7caf3f28e05b" />


### 🟢 Green Detection
<img width="1917" height="1078" alt="green" src="https://github.com/user-attachments/assets/ac6c3e14-cecb-4645-bdcf-a3f7f2e81e4d" />


### 🔵 Blue Detection
<img width="1917" height="1078" alt="blue" src="https://github.com/user-attachments/assets/d34a0f1f-3747-4328-82a5-412c6501de8c" />


### 🟡 Yellow Detection
<img width="1917" height="1078" alt="yellow" src="https://github.com/user-attachments/assets/a177e553-c144-4de7-9520-c3e2a350b377" />

---

## 👩‍💻 Author

Eng.Sadeem Al-Harthi
Computer Engineering Student | TU
