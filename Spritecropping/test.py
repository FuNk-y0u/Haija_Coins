import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
window = tk.Tk(className = "test")

image = Image.open("title.png")

box = (0, 0, 69, 69)
image_cropped = image.crop(box)

image1 = ImageTk.PhotoImage(image_cropped)

test = tk.Label(image = image1)
test.pack()
window.mainloop()
