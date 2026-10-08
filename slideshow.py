from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Path
image_paths = [
    r"C:\Users\tanus\Downloads\WhatsApp Image 2026-09-17 at 5.27.29 PM.jpeg",
    r"C:\Users\tanus\Downloads\Tanushree Yaltiwar Photo.jpeg",
    r"C:\Users\tanus\OneDrive\Pictures\Instagram\IMG_20241130_080450_766.jpg",
    r"C:\Users\tanus\Downloads\me.jpg",
    r"C:\Users\tanus\OneDrive\Pictures\Instagram\IMG_20240429_183256_472.jpg",
]

# Resize the images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()


def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        root.update()
        time.sleep(3)


slideshow = cycle(photo_images)


def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()


play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
