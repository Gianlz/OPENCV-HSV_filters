# OPENCV-HSV_filters

![image](https://github.com/Gianlz/OPENCV-HSV_filters/assets/67298422/283ee081-2ff5-4ebe-99dd-26683553417d)

# OPENCV-FILTERS by Gianluca Zugno

## Description
This code is a PyQt5 application that allows you to apply filters to an image. The image is read from a URL and then decoded into a NumPy array. The application allows you to adjust the HSV values of the image using sliders, enable/disable dilation and erosion, print the current HSV values, enable/disable Canny edge detection, and toggle dark mode.

## Requirements
- Python 3.x
- PyQt5
- NumPy
- OpenCV

## Installation
1. Clone the repository: `git clone https://github.com/gianlucazugno/opencv-filters.git](https://github.com/Gianlz/OPENCV-HSV_filters.git)`
2. Install the required packages: `pip install -r requirements.txt` ## Soon
3. Run the application: `python main.py`
   OBS: change the path for your non-local image changing this line `#Read image from URL
url = ''`

## Usage
1. Adjust the HSV values using the sliders in the "HSV Lower" and "HSV Upper" groups.
2. Enable/disable dilation and erosion using the checkboxes.
3. Print the current HSV values by clicking the "Print HSV Values" button.
4. Enable/disable Canny edge detection by clicking the "Enable Canny" button.
5. Toggle dark mode by clicking the "Dark Mode" button.

## Credits
- Gianluca Zugno

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## TO DO

1. Add a feature to save the filtered image to a file. On process
2. Add a feature to adjust the brightness and contrast of the image.
3. Add a feature to crop the image to a specific size or aspect ratio.
4. Add a feature to rotate the image by a specific angle.
