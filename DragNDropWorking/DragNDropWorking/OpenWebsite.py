# importing webbrowser module
import webbrowser
# importing all files from tkinter module
from tkinter import *

# creating root
root = Tk()
# setting GUI title
root.title("WebBrowsers")
# setting GUI geometry
root.geometry("660x660")


# function to open linkedin in browser
def linkedin():
    webbrowser.open("www.linkedin.com")
# function to open facebook in browser
def facebook():
    webbrowser.open("www.facebook.com")
# function to open twitter in browser
def twitter():
    webbrowser.open("www.twitter.com")
# function to open youtube in browser
def youtube():
    webbrowser.open("www.youtube.com")
# function to open whatsapp web in browser
def whatsappweb():
    webbrowser.open("www.whatsappweb.com")
# function to open instagram in browser
def instagram():
    webbrowser.open("www.instagram.com")
# function to open gmail in browser
def gmail():
    webbrowser.open("www.gmail.com")

Label(root, text="WELCOME TO MY FAVOURITE \nWEBSITES", font="Helvtica 25 bold").pack()
Label(root,text="Click on the buttons to open website",font="LUCIDA").pack()
#creating button for each functions
# button to call linkedin function
mylinkedin = Button(root,text="LINKEDIN", command=linkedin,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call facebook function
myfacebook = Button(root, text="FACEBOOK", command=facebook,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call twitter  function
mytwitter = Button(root, text="TWITTER", command=twitter,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call youtube  function
myyoutube = Button(root, text="YOUTUBE", command=youtube,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call whatsappweb  function
mywhatsapp = Button(root, text="WHATSAPP WEB", command=whatsappweb,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call instagram  function
myinstagram = Button(root, text="INSTAGRAM", command=instagram,font="LUCIDA 15 bold").pack(padx=20,pady=20)
# button to call gmail  function
mygmail= Button(root, text="GMAIL" , command=gmail,font="LUCIDA 15 bold").pack(padx=20,pady=20)

#running the mainloop()
root.mainloop()
