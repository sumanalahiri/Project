from tkinter import *

class DragDropDemo(Tk):

    def __init__(self):
        super().__init__()

        self.title("Drag and Drop Demo")
        self.geometry("1024x768")

        self.frame1 = Frame(self, bg="lightblue", width=250, height=300)
        self.frame1.pack(side="left", fill="both", expand=True)

        self.frame2 = Frame(self, bg="lightgreen", width=250, height=300)
        self.frame2.pack(side="right", fill="both", expand=True)

        # Set up images for dragging
        self.image1 = PhotoImage(file="1.png")
        self.image2 = PhotoImage(file="2.png")
        self.image3 = PhotoImage(file="3.png")
        self.image4 = PhotoImage(file="4.png")

        # set up variables for correct images
        self.image1_correct = False
        self.image2_correct = True
        self.image3_correct = False
        self.image4_correct = False

        # Create labels for images
        self.label1 = Label(self.frame1, image=self.image1)
        self.label1.place(x=10, y=10)
        self.label2 = Label(self.frame1, image=self.image2)
        self.label2.place(x=10, y=70)
        self.label3 = Label(self.frame1, image=self.image3)
        self.label3.place(x=10, y=130)
        self.label4 = Label(self.frame1, image=self.image4)
        self.label4.place(x=10, y=190)

        # bind the label events
        self.label1.bind("<ButtonPress-1>", self.onDragStart)
        self.label2.bind("<ButtonPress-1>", self.onDragStart)
        self.label3.bind("<ButtonPress-1>", self.onDragStart)
        self.label4.bind("<ButtonPress-1>", self.onDragStart)

        self.label1.bind("<B1-Motion>", self.onDragMotion)
        self.label2.bind("<B1-Motion>", self.onDragMotion)
        self.label3.bind("<B1-Motion>", self.onDragMotion)
        self.label4.bind("<B1-Motion>", self.onDragMotion)

        self.label1.bind("<ButtonRelease-1>", self.onDragStop)
        self.label2.bind("<ButtonRelease-1>", self.onDragStop)
        self.label3.bind("<ButtonRelease-1>", self.onDragStop)
        self.label4.bind("<ButtonRelease-1>", self.onDragStop)

        # set the dragging widget to None initially
        self.draggingWidget = None

    def onDragStart(self, event):
        # save the widget that was clicked on
        self.draggingWidget = event.widget

        # calculate the position of the widget relative to the mouse pointer
        self.offsetX = event.x
        self.offsetY = event.y

    def onDragMotion(self, event):
        # move the widget to follow the mouse pointer
        if self.draggingWidget is not None:
            x = event.x_root - self.offsetX - self.winfo_rootx()
            y = event.y_root - self.offsetY - self.winfo_rooty()
            self.draggingWidget.place(x=x, y=y)

    def onDragStop(self, event):
        # get the current mouse position
        x, y = event.x_root, event.y_root

        # check if the mouse is over the second frame
        if x > self.frame2.winfo_rootx() and x < self.frame2.winfo_rootx() + self.frame2.winfo_width() \
                and y > self.frame2.winfo_rooty() and y < self.frame2.winfo_rooty() + self.frame2.winfo_height():
            # create a new label widget in the second frame
            new_label = Label(self.frame2, image=self.draggingWidget["image"])
            new_label.pack()

            # check if the correct image was dragged
            if self.draggingWidget == self.label2:
                self.correct_label = Label(self.frame2, text="Correct Image Placed!", fg="green", font=("Arial", 16))
                self.correct_label.pack()
                print("Correct!")
            else:
                print("Incorrect.")
                # move the image back to its original position

        # reset the dragging widget
        self.draggingWidget = None


if __name__ == "__main__":
    demo = DragDropDemo()
    demo.mainloop()
