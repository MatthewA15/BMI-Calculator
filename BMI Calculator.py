#Matthew Allicock
#100860998

import tkinter as tk

class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def calculate_bmi_number(self):
        bmi = self.weight / (self.height ** 2)
        return bmi
    def get_bmi_status(self):
        bmi = self.calculate_bmi_number()
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Healthy Weight'
        else:
            return 'Overweight'
class BMI_Calculator_GUI:
    def __init__(self, master):
        self.master = master
        master.title('BMI Calculator')
        self.weightt = tk.Label(master, text='Weight (kg):')
        self.weightt.grid(row=0, column=0)
        self.weight_e = tk.Entry(master)
        self.weight_e.grid(row=0, column=1)
        self.heightt = tk.Label(master, text='Height (m):')
        self.heightt.grid(row=1, column=0)
        self.height_e = tk.Entry(master)
        self.height_e.grid(row=1, column=1)
        self.calculate_button = tk.Button(master, text='Start Calculate!', command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2)
        self.result_label = tk.Label(master, text='')
        self.result_label.grid(row=3, column=0, columnspan=2)
    def calculate_bmi(self):
        try:
            weight = float(self.weight_e.get())
            height = float(self.height_e.get())
            bmi_calculator = BMI_Calculator(weight, height)
            bmi = bmi_calculator.calculate_bmi_number()
            status = bmi_calculator.get_bmi_status()
            self.result_label.config(text=f'Your BMI is {bmi:.2f}. -- {status}.')
        except ValueError:
            self.result_label.config(text='Please enter valid weight and height values.')
root = tk.Tk()
bmi_calculator_gui = BMI_Calculator_GUI(root)
root.mainloop()