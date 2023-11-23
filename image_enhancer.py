import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


def enhance_image():
    # Ask the user to select an image file
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

    # Check if a file was selected
    if not file_path:
        status_label.config(text="No file selected.")
        return

    # Load the selected image
    image = cv2.imread(file_path)

    # Check if the image is loaded successfully
    if image is None:
        status_label.config(text="Error: Could not open or find the image.")
        return

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
    output_path = 'enhanced_image.jpg'
    cv2.imwrite(output_path, sharpened_image)

    status_label.config(text=f"Enhanced image saved to {output_path}")


# Create the main window
root = tk.Tk()
root.title("Image Enhancer")

# Create and configure widgets
select_button = tk.Button(root, text="Select Image", command=enhance_image)
select_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

# Start the Tkinter event loop
root.mainloop()
