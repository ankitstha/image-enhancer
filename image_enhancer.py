# image_enhancer.py
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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
    display_original_image(image)
    display_enhanced_image(sharpened_image)

    # Prompt the user to select a location to save the enhanced image
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

    # Check if a location was selected
    if not save_path:
        status_label.config(text="Enhancement canceled.")
        return

    # Save the enhanced image
    cv2.imwrite(save_path, sharpened_image)
    status_label.config(text=f"Enhanced image saved to {save_path}")

def display_original_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)

    original_image_label.config(image=img)
    original_image_label.image = img

def display_enhanced_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)

    enhanced_image_label.config(image=img)
    enhanced_image_label.image = img

# Create the main window
root = tk.Tk()
root.title("Image Enhancer")

# Create and configure widgets
select_button = tk.Button(root, text="Select Image", command=enhance_image)
select_button.pack(pady=10)

original_image_label = tk.Label(root, text="Original Image")
original_image_label.pack()

enhanced_image_label = tk.Label(root, text="Enhanced Image")
enhanced_image_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Start the Tkinter event loop
root.mainloop()
