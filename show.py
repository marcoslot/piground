#!/usr/bin/python3
import sys
import tkinter as tk
from PIL import Image, ImageTk

def display_image_fullscreen(image_path):
    # Create the main window
    root = tk.Tk()

    # Remove window decorations
    root.overrideredirect(True)

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window size and position
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Load and resize the image
    img = Image.open(image_path)
    img = img.resize((screen_width, screen_height), Image.ANTIALIAS)

    # Convert to a format Tkinter can use
    tk_img = ImageTk.PhotoImage(img)

    # Add an image label to the window
    label = tk.Label(root, image=tk_img)
    label.pack()

    # Exit fullscreen with the 'Esc' key
    root.bind("<Escape>", lambda event: root.destroy())

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = 'generated-latest.png'

    display_image_fullscreen(image_path)
