#from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import pygame
import random

root=tk.Tk()
root.title("FRUIT  WARRIOR")
root.geometry("580x640")
root.resizable(0, 0)
image = Image.open("wood3.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo) #assigning it to a widget attribute
label.image = photo #label used to assign data and display stuff
label.pack()

#buttons
b1=tk.Button(root,font="Broadway 18",text="Start",height=2,width=10)
b1.place(x=30,y=400)#button placement

b2=tk.Button(root,font="Broadway 17",text="Instructions",height=2,width=10)
b2.place(x=370,y=400)

b3=tk.Button(root,font="Broadway 18",text="Settings",height=2,width=10)
b3.place(x=30,y=520)

b4=tk.Button(root,font="Broadway 18",text="About",height=2,width=10)
b4.place(x=370,y=520)

root.mainloop()