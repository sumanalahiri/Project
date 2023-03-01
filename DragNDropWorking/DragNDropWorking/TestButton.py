import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

root = tk.Tk()


URL = "https://www.pinclipart.com/picdir/big/65-654632_setting-icon-clipart-png-download.png"
u = urllib.request.urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im = im.resize((50,50),Image.ANTIALIAS)


photo = ImageTk.PhotoImage(im)

button = tk.Button(image=photo,width=50,height=50,compound="c")
button.image = photo
button.pack()


img = Image.open("download.jpg")


img = img.resize((250, 250))
tkimage = ImageTk.PhotoImage(img)
tk.Label(root, image=tkimage).pack()# changed to pack from grid

button1 = tk.Button(image=tkimage,width=250,height=250,compound="c")
button1.image = tkimage
button1.pack()


root.mainloop()
