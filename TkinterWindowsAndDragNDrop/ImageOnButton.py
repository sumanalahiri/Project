import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageFont


class Window:
    def __init__(self):
        "Use a new image for the button"
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Window with a Button with text/image")
        self.image = NewImage()
        Button(self.root, self.image.im)
        self.root.mainloop()


class NewImage:
    def __init__(self):
        self.size(300, 32)
        self.new_image()
        self.add_text()
        self.add_lines()

    def size(self, w, fs):
        "Whidth and Height of a button"
        self.width = w
        self.font_size = fs

    def new_image(self):
        "Prepare to draw text on the image"
        self.im = Image.new("RGBA", (self.width, self.font_size), "red")
        self.draw = ImageDraw.Draw(self.im)

    def add_text(self):
        "Add the text to the image"
        self.draw.text((
            0, 0),
            "Click on this button",
            font=ImageFont.truetype("arial", self.font_size),
            fill="blue")

    def add_lines(self):
        "Draw some lines on the image"
        self.draw.line((0, 2, self.width, 2), fill="yellow")
        self.draw.line((0, self.font_size-2, self.width, self.font_size-2), fill="yellow")

class Button:

    def __init__(self, root, image):
        self.root = root
        self.im = image
        self.button_with_image()

    def button_with_image(self):
        "Add the image created to the button"
        img = ImageTk.PhotoImage(self.im)
        img.image = img # to not delete image
        b = tk.Button(self.root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            text="",
            image=img,
            command=lambda : print("Hello"))
        b.pack()


if __name__ == "__main__":
    Window()



