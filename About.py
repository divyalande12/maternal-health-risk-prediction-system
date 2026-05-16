from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Maternal Health Risk Prediction")
root.geometry("1600x900")
root.configure(bg="#f5f5f5")

# Navigation Bar
nav_frame = Frame(root, bg="#13919b", height=60)
nav_frame.pack(fill=X)

nav_title = Label(nav_frame, text="Maternal Health Risk Prediction", font=("Helvetica", 20, "bold"), fg="white", bg="#13919b", padx=20)
nav_title.pack(side=LEFT, pady=10)

# Marquee
def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if x2 < 0 or y1 < 0:  # Reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, shift)

canvas = Canvas(root, bg="#f5f5f5")
canvas.pack(fill=X, pady=10)
text_var = "Maternal Health Risk Prediction - Spreading Awareness"
text = canvas.create_text(0, -2000, text=text_var, font=("Raleway", 16, "italic"), fill="#13919b", tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
canvas['width'] = 1600
canvas['height'] = 30
fps = 40
shift()

# Information Section
content_frame = Frame(root, bg="white", bd=2, relief="solid")
content_frame.place(x=100, y=150, width=1400, height=600)


# Left Logo
left_logo_path = "4.webp"  # Replace with your left logo file path
left_logo_image = Image.open(left_logo_path).resize((600, 550), Image.ANTIALIAS)
left_logo = ImageTk.PhotoImage(left_logo_image)
left_logo_label = Label(content_frame, image=left_logo, bg="white")
left_logo_label.place(x=10, y=10)  # Adjust position as needed

# # Left Logo
# left_logo_path = "logo.jpeg"  # Replace with your left logo file path
# left_logo_image = Image.open(left_logo_path).resize((100, 100), Image.ANTIALIAS)
# left_logo = ImageTk.PhotoImage(left_logo_image)
# left_logo_label = Label(content_frame, image=left_logo, bg="white")
# left_logo_label.place(x=10, y=10)  # Adjust position as needed

# Right Logo
right_logo_path = "logo.webp"  # Replace with your right logo file path
right_logo_image = Image.open(right_logo_path).resize((100, 100), Image.ANTIALIAS)
right_logo = ImageTk.PhotoImage(right_logo_image)
right_logo_label = Label(content_frame, image=right_logo, bg="white")
right_logo_label.place(x=1290, y=10)  # Adjust position as needed

info_title = Label(content_frame, text="Maternal Health Risk Prediction", font=("italic", 18, "bold"), bg="white", fg="#13919b")
info_title.place(x=800, y=10)

info_text = (
    "Maternal Health Risk Prediction refers to the process of identifying potential \n health risks that a woman may face during pregnancy, childbirth, or after delivery.\n\n"
    "Common Maternal Health Risks\n"
    "- Gestational Hypertension: High blood pressure during pregnancy.\n"
    "- Preeclampsia: A severe form of high blood pressure that can damage organs.\n"
    "- Gestational Diabetes: High blood sugar levels during pregnancy.\n\n"
    "Symptoms of Maternal Health Risks:\n"
    "- Swelling in hands and face (Possible sign of preeclampsia).\n"
    "- Severe headaches or vision problems (May indicate high blood pressure).\n"
    "- Rapid weight gain (Could be related to fluid retention in preeclampsia).\n"
    "- Excessive thirst and frequent urination (Signs of gestational diabetes).\n\n"
    " How to Reduce Maternal Health Risks:\n"
    "-Maintain a healthy weight and BMI. \n"  "Regular prenatal checkups to monitor health.\n"
    "-Follow a balanced diet rich in iron, calcium, and proteins. \n"
      "- Stay hydrated and get adequate rest.\n"
     "-Take recommended vaccines (e.g., flu, Tdap).\n" 
     "Be aware of any unusual symptoms and seek medical help immediately."
)

info_label = Label(content_frame, text=info_text, font=("Raleway", 14, "italic"), bg="white", fg="#0a3c8e",justify=LEFT, wraplength=1200)
info_label.place(x=660, y=100)

# Footer
footer = Frame(root, bg="#13919b", height=40)
footer.pack(side=BOTTOM, fill=X)
footer_label = Label(footer, text="© 2025 Ovarian Cancer Awareness | All Rights Reserved", font=("Helvetica", 10), fg="white", bg="#13919b")
footer_label.pack()

root.mainloop()
