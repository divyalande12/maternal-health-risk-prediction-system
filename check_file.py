import tkinter as tk
from tkinter import filedialog
from joblib import load
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding="utf-8") as file:
            content = text.get(1.0, tk.END)
            file.write(content)

def predict_job():
    try:
        # Load the model
        predictor = load("Model1.joblib")

        # Get input text
        text_content = text.get(1.0, tk.END).strip()

        if not text_content:
            result_label.config(text='Error: No text provided for prediction.', fg='red')
            return

        # Making prediction (assuming Model1.joblib can directly handle raw text input)
        y_predict = predictor.predict([text_content])
  # Direct prediction without tf_vect

        if y_predict[0] == 0:
            result_label.config(text='Prediction: Low risk', fg='green')
        elif y_predict[0] == 1:
            result_label.config(text='Prediction: Mid risk', fg='orange')
        else:
            result_label.config(text='Prediction: High risk', fg='red')

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg='red')

# Create the main Tkinter window
root = tk.Tk()
root.title("Fake Job Postings Detector")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")

# Load and set background image
try:
    image2 = Image.open(r'pp.jpeg')
    image2 = image2.resize((w, h), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0)
except Exception as e:
    print(f"Error loading background image: {e}")

# Create a Text widget for displaying and editing text
text = tk.Text(root, wrap="word", width=70, height=30)
text.place(x=700, y=60)

# Create "Open" and "Save" buttons
open_button = tk.Button(root, text="Open File", command=open_file, relief="solid", bg="aliceblue", fg="black", width=15, font=("Times New Roman", 15, "bold"))
open_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(root, text="Save File", command=save_file, relief="solid", bg="aliceblue", fg="black", width=15, font=("Times New Roman", 15, "bold"))
save_button.pack(side=tk.LEFT, padx=5)

# Create a button to predict
predict_button = tk.Button(root, text="Predict", command=predict_job, relief="solid", bg="aliceblue", fg="black", width=15, font=("Times New Roman", 15, "bold"))
predict_button.pack(side=tk.LEFT, padx=5)

# Create a label to display prediction results
result_label = tk.Label(root, text="", relief="solid", font=("Times New Roman", 15, "bold"))
result_label.place(x=100, y=650, width=800, height=50)

# Run the Tkinter main loop
root.mainloop()
