import sys
import cv2
import urllib.request
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QGroupBox, QCheckBox, QGridLayout, QMainWindow

# Read image from URL
url = 'https://img.freepik.com/free-photo/majestic-lion-rests-africa-wilderness-area-generated-by-ai_188544-16817.jpg'
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

# Decode image data into NumPy array
img = cv2.imdecode(arr, -1)

# Create a QMainWindow to hold the QLabel, sliders, and button
app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("OPENCV-FILTERS by Gianluca Zugno")

# Create a QWidget to hold the QLabel, sliders, and button
widget = QWidget()
main_window.setCentralWidget(widget)

# Set the background color of the widget
widget.setStyleSheet("background-color: #f2f2f2;")

# Create a QGridLayout to arrange the widgets
layout = QGridLayout()
widget.setLayout(layout)

# Create a QLabel and set the image as its pixmap
label = QLabel()
height, width, channel = img.shape
bytesPerLine = 3 * width
qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
pixmap = QPixmap(qImg)
label.setPixmap(pixmap)
layout.addWidget(label, 0, 0, 1, 2)

# Create two QGroupBoxes for the lower and upper sliders
hsv_lower_group = QGroupBox('HSV Lower')
hsv_lower_layout = QVBoxLayout()
hsv_lower_group.setLayout(hsv_lower_layout)
layout.addWidget(hsv_lower_group, 1, 0)

hsv_upper_group = QGroupBox('HSV Upper')
hsv_upper_layout = QVBoxLayout()
hsv_upper_group.setLayout(hsv_upper_layout)
layout.addWidget(hsv_upper_group, 1, 1)

# Create three sliders for each set of HSV values
hsv_lower_sliders = []
hsv_upper_sliders = []
hsv_labels = []
for i in range(3):
    hsv_lower_slider = QSlider()
    hsv_lower_slider.setOrientation(1)  # Vertical orientation
    hsv_lower_slider.setRange(0, 255)
    hsv_lower_slider.setValue(0)
    hsv_lower_layout.addWidget(QLabel(f'H: {hsv_lower_slider.value()}'))
    hsv_lower_layout.addWidget(hsv_lower_slider)
    hsv_lower_sliders.append(hsv_lower_slider)

    hsv_upper_slider = QSlider()
    hsv_upper_slider.setOrientation(1)  # Vertical orientation
    hsv_upper_slider.setRange(0, 255)
    hsv_upper_slider.setValue(255)
    hsv_upper_layout.addWidget(QLabel(f'H: {hsv_upper_slider.value()}'))
    hsv_upper_layout.addWidget(hsv_upper_slider)
    hsv_upper_sliders.append(hsv_upper_slider)

    hsv_label = QLabel(f'{["H", "S", "V"][i]}')
    hsv_lower_layout.addWidget(hsv_label)
    hsv_labels.append(hsv_label)

# Create a slider for dilation
dilation_slider = QSlider()
dilation_slider.setOrientation(1)  # Vertical orientation
dilation_slider.setRange(0, 10)
dilation_slider.setValue(0)
layout.addWidget(QLabel('Dilation'), 2, 0)
layout.addWidget(dilation_slider, 3, 0)

# Create a checkbox to enable/disable dilation
dilation_checkbox = QCheckBox('Enable Dilation')
layout.addWidget(dilation_checkbox, 4, 0)

# Create a slider for erosion
erosion_slider = QSlider()
erosion_slider.setOrientation(1)  # Vertical orientation
erosion_slider.setRange(0, 10)
erosion_slider.setValue(0)
layout.addWidget(QLabel('Erosion'), 2, 1)
layout.addWidget(erosion_slider, 3, 1)

# Create a checkbox to enable/disable erosion
erosion_checkbox = QCheckBox('Enable Erosion')
layout.addWidget(erosion_checkbox, 4, 1)

# Create a QPushButton to print the current HSV values
button = QPushButton('Print HSV Values')
layout.addWidget(button, 5, 0)

# Create a QLabel to display the current HSV values
hsv_values_label = QLabel()
layout.addWidget(hsv_values_label, 5, 1)

# Create a QPushButton to enable/disable Canny edge detection
canny_button = QPushButton('Enable Canny')
layout.addWidget(canny_button, 6, 0)

# Create a QPushButton to toggle dark mode
dark_mode_button = QPushButton('Dark Mode')
layout.addWidget(dark_mode_button, 6, 1)

# Define a function to update the image when the sliders are moved
def update_image():
    hsv_lower = np.array([hsv_lower_sliders[0].value(), hsv_lower_sliders[1].value(), hsv_lower_sliders[2].value()])
    hsv_upper = np.array([hsv_upper_sliders[0].value(), hsv_upper_sliders[1].value(), hsv_upper_sliders[2].value()])
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, hsv_lower, hsv_upper)
    if dilation_checkbox.isChecked():
        kernel = np.ones((dilation_slider.value(), dilation_slider.value()), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=1)
    if erosion_checkbox.isChecked():
        kernel = np.ones((erosion_slider.value(), erosion_slider.value()), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
    if canny_button.text() == 'Disable Canny':
        edges = cv2.Canny(mask, 100, 200)
        masked_img = cv2.bitwise_and(img, img, mask=edges)
    else:
        masked_img = cv2.bitwise_and(img, img, mask=mask)
    height, width, channel = masked_img.shape
    bytesPerLine = 3 * width
    qImg = QImage(masked_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    pixmap = QPixmap(qImg)
    label.setPixmap(pixmap)

    for i in range(3):
        hsv_labels[i].setText(f'{["H", "S", "V"][i]}: {hsv_lower_sliders[i].value()} - {hsv_upper_sliders[i].value()}')

# Define a function to print the current HSV values
def print_hsv_values():
    hsv_lower = np.array([hsv_lower_sliders[0].value(), hsv_lower_sliders[1].value(), hsv_lower_sliders[2].value()])
    hsv_upper = np.array([hsv_upper_sliders[0].value(), hsv_upper_sliders[1].value(), hsv_upper_sliders[2].value()])
    hsv_values_label.setText(f'HSV Lower: {hsv_lower} | HSV Upper: {hsv_upper}')

# Define a function to toggle Canny edge detection
def toggle_canny():
    if canny_button.text() == 'Enable Canny':
        canny_button.setText('Disable Canny')
    else:
        canny_button.setText('Enable Canny')
    update_image()

# Define a function to toggle dark mode
def toggle_dark_mode():
    if widget.styleSheet() == '':
        widget.setStyleSheet("background-color: #222222; color: #f2f2f2;")
    else:
        widget.setStyleSheet("")

# Connect the sliders, checkbox, and buttons to their respective functions
for slider in hsv_lower_sliders:
    slider.valueChanged.connect(update_image)
for slider in hsv_upper_sliders:
    slider.valueChanged.connect(update_image)
dilation_slider.valueChanged.connect(update_image)
erosion_slider.valueChanged.connect(update_image)
dilation_checkbox.stateChanged.connect(update_image)
erosion_checkbox.stateChanged.connect(update_image)
button.clicked.connect(print_hsv_values)
canny_button.clicked.connect(toggle_canny)
dark_mode_button.clicked.connect(toggle_dark_mode)

# Set the size of the window to be proportional to the screen resolution
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()
main_window.resize(width // 2, height // 2)

# Show the widget
main_window.show()

# Run the event loop
sys.exit(app.exec_())
