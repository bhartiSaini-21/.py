import customtkinter
from tkinter import *
from tkinter import messagebox, filedialog
import json

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        result_label.configure(text=f'BMI: {bmi:.2f}')
        
        # Display BMI category and health tip
        if bmi < 18.5:
            category = "Underweight"
            tip = "Consider a balanced diet rich in nutrients."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            tip = "Maintain your healthy habits!"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            tip = "Include regular physical activity."
        else:
            category = "Obese"
            tip = "Consult a healthcare provider for advice."
        
        category_label.configure(text=f'Category: {category}')
        tip_label.configure(text=f'Health Tip: {tip}')
        log_history(f"BMI: {bmi:.2f} - {category}")
        
        # Calculate ideal weight range for given height
        min_ideal_weight = 18.5 * (height ** 2)
        max_ideal_weight = 24.9 * (height ** 2)
        ideal_weight_label.configure(
            text=f"Ideal Weight Range: {min_ideal_weight:.1f} - {max_ideal_weight:.1f} kg"
        )
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def clear_fields():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_var.set("")
    result_label.configure(text='')
    category_label.configure(text='')
    tip_label.configure(text='')
    ideal_weight_label.configure(text='')

def log_history(entry):
    history_list.insert(END, entry)

def save_history():
    history = history_list.get(0, END)
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(history, file)
        messagebox.showinfo("Success", "History saved successfully.")

def load_history():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            history = json.load(file)
        history_list.delete(0, END)
        for entry in history:
            history_list.insert(END, entry)
        messagebox.showinfo("Success", "History loaded successfully.")

def show_info():
    messagebox.showinfo("BMI Information", 
                        "BMI Categories:\n"
                        "Underweight: <18.5\n"
                        "Normal weight: 18.5–24.9\n"
                        "Overweight: 25–29.9\n"
                        "Obesity: BMI of 30 or greater")

app = customtkinter.CTk()
app.title('BMI Calculator')
app.geometry('350x600')
app.config(bg='#000')

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 14, 'bold')
font3 = ('Arial', 16, 'bold')

# Title
title_label = customtkinter.CTkLabel(app, font=font1, text='BMI Calculator', text_color='#fff', bg_color='#000')
title_label.place(x=60, y=20)

# Weight input
weight_label = customtkinter.CTkLabel(app, font=font2, text='Weight (kg)', text_color='#fff', bg_color='#000')
weight_label.place(x=20, y=80)
weight_entry = customtkinter.CTkEntry(app, font=font2, width=100)
weight_entry.place(x=150, y=80)

# Height input
height_label = customtkinter.CTkLabel(app, font=font2, text='Height (cm)', text_color='#fff', bg_color='#000')
height_label.place(x=20, y=130)
height_entry = customtkinter.CTkEntry(app, font=font2, width=100)
height_entry.place(x=150, y=130)

# Age input
age_label = customtkinter.CTkLabel(app, font=font2, text='Age', text_color='#fff', bg_color='#000')
age_label.place(x=20, y=180)
age_entry = customtkinter.CTkEntry(app, font=font2, width=100)
age_entry.place(x=150, y=180)

# Gender input
gender_label = customtkinter.CTkLabel(app, font=font2, text='Gender', text_color='#fff', bg_color='#000')
gender_label.place(x=20, y=230)
gender_var = StringVar(value="")
male_radio = customtkinter.CTkRadioButton(app, text="Male", variable=gender_var, value="Male", text_color='#fff', bg_color='#000')
male_radio.place(x=150, y=230)
female_radio = customtkinter.CTkRadioButton(app, text="Female", variable=gender_var, value="Female", text_color='#fff', bg_color='#000')
female_radio.place(x=210, y=230)

# Calculate Button
calculate_button = customtkinter.CTkButton(app, command=calculate_bmi, font=font2, text='Calculate BMI', text_color='#fff', fg_color='#06911f', hover_color='#045c12', corner_radius=5, width=200)
calculate_button.place(x=50, y=280)

# Result Display
result_label = customtkinter.CTkLabel(app, text='', font=font3, text_color='#fff', bg_color='#000')
result_label.place(x=30, y=330)

# Category Display
category_label = customtkinter.CTkLabel(app, text='', font=font3, text_color='#fff', bg_color='#000')
category_label.place(x=30, y=370)

# Health Tip
tip_label = customtkinter.CTkLabel(app, text='', font=font3, text_color='#fff', bg_color='#000')
tip_label.place(x=30, y=410)

# Ideal Weight Display
ideal_weight_label = customtkinter.CTkLabel(app, text='', font=font3, text_color='#fff', bg_color='#000')
ideal_weight_label.place(x=30, y=450)

# Clear Button
clear_button = customtkinter.CTkButton(app, command=clear_fields, font=font2, text='Clear', text_color='#fff', fg_color='#cc0000', hover_color='#9b0000', corner_radius=5, width=200)
clear_button.place(x=50, y=490)

# Show Info Button
info_button = customtkinter.CTkButton(app, command=show_info, font=font2, text='BMI Info', text_color='#fff', fg_color='#0077cc', hover_color='#005fa3', corner_radius=5, width=200)
info_button.place(x=50, y=530)

# Save and Load Buttons
save_button = customtkinter.CTkButton(app, command=save_history, font=font2, text='Save History', text_color='#fff', fg_color='#333', hover_color='#222', corner_radius=5, width=200)
save_button.place(x=50, y=570)
load_button = customtkinter.CTkButton(app, command=load_history, font=font2, text='Load History', text_color='#fff', fg_color='#333', hover_color='#222', corner_radius=5, width=200)
load_button.place(x=50, y=610)

# History List
history_list = Listbox(app, font=font2, bg='#333', fg='#fff', width=30, height=5)
history_list.place(x=20, y=670)

app.mainloop()
