from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np

import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Maternal Health Risk Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

img=ImageTk.PhotoImage(Image.open("DR.1.jpg"))

img2=ImageTk.PhotoImage(Image.open("DR.2.jpg"))

img3=ImageTk.PhotoImage(Image.open("DR.3.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

move()

lbl = tk.Label(root, text="Maternal Health Risk Prediction", font=('times', 35,' bold '), height=2, width=62,bg="paleturquoise",fg="Black")
lbl.place(x=0, y=0)

def Model_Training():
    data = pd.read_csv("F:/new project 2025/Maternal Health Risk project 100%/Data Set.csv")
    data.head()
    

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()

    
    data['Age'] = le.fit_transform(data['Age'])
    data['SystolicBP'] = le.fit_transform(data['SystolicBP'])
    data['DiastolicBP'] = le.fit_transform(data['DiastolicBP'])
    data['BS'] = le.fit_transform(data['BS'])
    data['BodyTemp'] = le.fit_transform(data['BodyTemp'])
    data['HeartRate'] = le.fit_transform(data['HeartRate'])
   
   
   

    """Feature Selection => Manual"""
    x = data.drop(['RiskLevel'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['RiskLevel']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=1234)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.ensemble import RandomForestClassifier  # Correct import

# Initialize and train the Random Forest model
    svcclassifier = RandomForestClassifier(n_estimators=100, random_state=42)
    svcclassifier.fit(x_train, y_train)


    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as rf.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"rf.joblib")
    print("Model saved as rf.joblib")

def call_file():
    from subprocess import call
    call(["python", "Check_prediction.py"])
    
def Care_Instructions():
    from subprocess import call
    call(["python", "Care_Instructions.py"])

def CancerDetection():
    from subprocess import call
    call(["python", "Check_Prediction.py"])
    
def checkfile():
    from subprocess import call
    call(["python", "Check_file.py"])

def About():
    from subprocess import call
    call(["python", "About.py"])


def window():
    root.destroy()

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=200)

d2 = tk.Button(root, text="Care Instructions", command=Care_Instructions, width=20, height=1, bd=13,
               background="plum", foreground="black", font=("Times New Roman", 17, "bold"))
d2.place(x=50, y=260)

d3 = tk.Button(root, text="Cancer Detection", command=CancerDetection, width=20, height=1, bd=13,
               background="plum", foreground="black", font=("Times New Roman", 17, "bold"))
d3.place(x=50, y=150)

d3 = tk.Button(root, text="Check file", command=checkfile, width=20, height=1, bd=13,
               background="plum", foreground="black", font=("Times New Roman", 17, "bold"))
d3.place(x=50, y=360) 

d4 = tk.Button(root, text="About", command=About, width=20, height=1, bd=13,
               background="plum", foreground="black", font=("Times New Roman", 17, "bold"))
d4.place(x=50, y=450)


exit = tk.Button(root, text="Exit", command=window,bd=13, width=20, height=1, font=('times', 15, ' bold '),bg="plum",fg="black")
exit.place(x=50, y=540)

root.mainloop()

