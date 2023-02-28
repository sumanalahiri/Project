from tkinter import *
from FrameController import FrameController


def quitRevise():
    root.destroy()


root = Tk(className='Revision Tool')
root.geometry('1000x700')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

fc = FrameController(root)
quit_but = Button(root, text='Quit', font=("Arial", 30), command=quitRevise)
quit_but.grid(sticky='s', pady=10, padx=10)

root.mainloop()











#Aydan Hung CS IA