import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize Tkinter
root = Tk()
root.withdraw()  # Hide the main window

# Ask the user to select an image file
file_path = askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

# Check if a file was selected
if not file_path:
    print("No file selected. Exiting.")
    exit()

# Load the selected image
image = cv2.imread(file_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Denoise using GaussianBlur
denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

# Sharpen using filter2D
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
sharpened_image = cv2.filter2D(denoised_image, -1, kernel)

# Display the original and enhanced images
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the enhanced image
cv2.imwrite('enhanced_image.jpg', sharpened_image)
