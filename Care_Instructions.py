# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:26:03 2025

@author: renuk
"""

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

# Global variable for filename
global fn
fn = ""

# Initialize the Tkinter root
root = tk.Tk()
root.title("HomePage")
root.geometry("1600x900")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

# Load the background image
background_image_path = 'd3.webp'
background_image = Image.open(background_image_path)
background_image = background_image.resize((w, h), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Set the background
background_label = tk.Label(root, image=background_photo)
background_label.image = background_photo
background_label.place(x=0, y=0)

# Title label
label_l1 = tk.Label(
    root, text="Maternal Health Risk Prediction Precations",
    font=("Times New Roman", 18, 'bold'),
    background="pink", fg="black", width=120, height=2
)
label_l1.place(x=0, y=0)

# Load and display four images
image_paths = ['p1.jpeg', 'p2.webp', 'p3.jpg', 'p4.jpg']  # Update these paths with your image filenames
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((500, 300), Image.Resampling.LANCZOS)  # Adjust the size as needed
    images.append(ImageTk.PhotoImage(img))

# Define positions for the images
x_positions = [100, 800, 100, 800]  # Horizontal positions for each image
y_positions = [70, 70, 450, 450]  # Vertical positions for each image

# Place the images using the defined positions
for i, img in enumerate(images):
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x_positions[i], y=y_positions[i])


# Function to destroy the window
def window():
    root.destroy()

# Run the Tkinter main loop
root.mainloop()
