import tkinter as tk
from tkinterDnD import *

class DragDropCanvas(tk.Canvas):
    def __init__(self, master=None, **kw):
        tk.Canvas.__init__(self, master=master, **kw)
        self.dragging = None
        dnd.make_draggable(self, tag='draggable')
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_drop)
        self.correct_image = "example.png" # replace with the correct image filename
        self.correct_image_dragged = False

    def on_drag(self, event):
        if self.dragging is not None:
            x, y = event.x, event.y
            self.coords(self.dragging, x, y)

    def on_drop(self, event):
        if self.dragging is not None:
            dragged_item_tags = self.gettags(self.dragging)
            if 'draggable' in dragged_item_tags:
                image_item = self.find_withtag('current')
                image_item_tags = self.gettags(image_item)
                if self.correct_image in image_item_tags:
                    self.correct_image_dragged = True
                else:
                    self.correct_image_dragged = False
            self.dragging = None

root = tk.Tk()
canvas = DragDropCanvas(root, width=300, height=300)
canvas.pack()

# create a list of draggable images
image_files = ["example1.png", "example2.png", "example3.png"]
images = []
for image_file in image_files:
    image = tk.PhotoImage(file=image_file)
    images.append(image)
    canvas.create_image(50, 50, image=image, tags=(image_file, 'draggable'))

root.mainloop()
