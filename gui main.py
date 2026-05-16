# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:26:03 2025

@author: renuk
"""

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

global fn
fn = ""

root = tk.Tk()
root.title("HomePage ")
root.geometry("1600x900")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

image2 = Image.open('7.jpg')
image2 = image2.resize((w, h), Image.Resampling.LANCZOS)

background_image = ImageTk.PhotoImage(image2) 
background_label = tk.Label(root, image=background_image)
background_label.image = background_image 
background_label.place(x=0, y=0)

label_l1 = tk.Label(root, text="Maternal Health Risk Prediction",font=("Times New Roman", 18, 'bold'),background="paleturquoise", fg="black", width=30, height=2)                   
label_l1.place(x=0, y=0)

welcome_label = tk.Label( root, text="......Welcome to Maternal Health Risk Prediction......", width=110, height=3, background="paleturquoise",foreground="black", font=("Times New Roman", 19, "bold"),)
welcome_label.place(x=0, y=620)

from tkinter import messagebox as ms

def Login():
    from subprocess import call
    call(["python", "login.py"])

def Register():
    from subprocess import call
    call(["python", "registration.py"])


    
def About():
    from subprocess import call
    call(["python", "About.py"])
  

def window():
    root.destroy()


d2 = tk.Button(root, text="Register", command=Register, width=30, height=2, bd=0, background="paleturquoise", foreground="black", font=("times new roman", 14, "bold"))
d2.place(x=400, y=0)

d3 = tk.Button(root, text="Login", command=Login, width=30, height=2, bd=0, background="paleturquoise", foreground="black", font=("times new roman", 14, "bold"))
d3.place(x=700, y=0)

d3 = tk.Button(root, text="About", command=About, width=40, height=2, bd=0, background="paleturquoise", foreground="black", font=("times new roman", 14, "bold"))
d3.place(x=900, y=0)

d4 = tk.Button(root, text="Exit", command=window, width=20, height=2, bd=0, background="paleturquoise", foreground="black", font=("times new roman", 14, "bold"))
d4.place(x=1300, y=0)



root.mainloop()
