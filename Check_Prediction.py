from tkinter import *
from tkinter import ttk 
import tkinter as tk
import numpy as np
import pandas as pd
from joblib import load

from PIL import Image, ImageTk  # Import PIL for image handling

root = tk.Tk()
root.geometry("800x850+250+5")
root.title("Maternal Health Risk Prediction")
root.configure(background="sky blue")

# Load and place the background image on the right side
bg_image = Image.open("bg.png")  # Replace with your image path
bg_image = bg_image.resize((1000, 800))  # Adjust size as needed
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=600, y=0)  # Adjust position as needed


Age = tk.StringVar()
SystolicBP = tk.StringVar()
DiastolicBP = tk.StringVar()
BS = tk.StringVar()
BodyTemp = tk.StringVar()
HeartRate = tk.StringVar()

def Detect1():
    e1 = float(Age.get())  
    e2 = float(SystolicBP.get())
    e3 = float(DiastolicBP.get())
    e4 = float(BS.get())
    e5 = float(BodyTemp.get())
    e6 = float(HeartRate.get())

    model = load('Model1.joblib')
    v1 = model.predict([[e1, e2, e3, e4, e5, e6]])

    print(v1)  # Debugging print statement

    if v1[0] == 'low risk':
        print("low risk")
        yes = tk.Label(root, text="low risk", background="green", foreground="white", font=('times', 20, ' bold '), width=15)
        yes.place(x=100, y=600)

    elif v1[0] == 'mid risk':
        print("mid risk")
        no = tk.Label(root, text="mid risk", background="blue", foreground="white", font=('times', 20, ' bold '), width=15)
        no.place(x=100, y=600)

    else:
        print("high risk")
        no = tk.Label(root, text="high risk", background="red", foreground="white", font=('times', 20, ' bold '), width=15)
        no.place(x=100, y=600)

l1 = tk.Label(root, text="Age", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l1.place(x=5, y=1)
Age = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Age)
Age.place(x=500, y=1)

l2 = tk.Label(root, text="SystolicBP", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l2.place(x=5, y=50)
SystolicBP = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=SystolicBP)
SystolicBP.place(x=500, y=50)

l3 = tk.Label(root, text="DiastolicBP", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l3.place(x=5, y=100)
DiastolicBP = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=DiastolicBP)
DiastolicBP.place(x=500, y=100)

l4 = tk.Label(root, text="BS", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l4.place(x=5, y=150)
BS = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=BS)
BS.place(x=500, y=150)

l5 = tk.Label(root, text="BodyTemp", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l5.place(x=5, y=200)
BodyTemp = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=BodyTemp)
BodyTemp.place(x=500, y=200)

l6 = tk.Label(root, text="HeartRate", background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
l6.place(x=5, y=250)
HeartRate = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=HeartRate)
HeartRate.place(x=500, y=250)

button1 = tk.Button(root, text="Prediction", command=Detect1, background="darkolivegreen1", font=('times', 20, ' bold '), width=25)
button1.place(x=100, y=400)

root.mainloop()
