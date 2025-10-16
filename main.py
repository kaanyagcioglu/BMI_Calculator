from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.geometry("300x160")

# Create function(s)
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"

    if bmi <= 16:
        messagebox.showinfo("BMI Category", "Severe Thinness")
    elif 16 < bmi <= 17:
        messagebox.showinfo("BMI Category", "Mild Thinness")
    elif 17 < bmi <= 18.5:
        messagebox.showinfo("BMI Category", "Moderate Thinness")
    elif 18.5 < bmi <= 25:
        messagebox.showinfo("BMI Category", "Normal")
    elif 25 < bmi <= 30:
        messagebox.showinfo("BMI Category", "Overweight")
    elif 30 <= bmi <= 35:
        messagebox.showinfo("BMI Category", "Obese Class I")
    elif 35 <= bmi <= 40:
        messagebox.showinfo("BMI Category", "Obese Class II")
    elif bmi > 40:
        messagebox.showinfo("BMI Category", "Obese Class III")



# Create GUI
label_kg = Label(window, text="KG: ")
label_kg.grid(column=1, row=1)

entry_kg = Entry(window)
entry_kg.grid(column=2, row=1)

label_height = Label(window, text="HEIGHT: ")
label_height.grid(column=1, row=2)

entry_height = Entry(window)
entry_height.grid(column=2, row=2)

button_calculate = Button(window, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=1, row=3)

label_result = Label(window, text="BMI: ")
label_result.grid(column=2, row=3)

window.mainloop()



