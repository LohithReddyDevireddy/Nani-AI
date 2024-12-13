from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
from pygame import mixer
mixer.init()

root=Tk()
root.geometry("750x750")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    #img = Image.open("NaniGPT_Logo.png")
    img = Image.open("NaniGPT_Animation.gif")
    lbl=Label(root)
    lbl.place(x=0,y=0)
    i=0
    
    
    for img in ImageSequence.Iterator(img):
        img=img.resize((750,750))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.0078125)
    root.destroy()
play_gif()
root.mainloop()