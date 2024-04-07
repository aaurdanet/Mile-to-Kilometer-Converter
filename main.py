from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

num1_input = Entry(width=10)
num1_input.grid(row=0, column=3)

equals_label = Label(text="equals to", font=("Arial", 12))
equals_label.grid(row=2, column=2)

result_label = Label(text=f"0", font=("Arial", 12))
result_label.grid(row=2, column=3)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=4)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(row=2, column=4)


def calc():
    input = num1_input.get()
    result = int(input) * 1.60934
    result = float(result)
    result_label.config(text=f"{result}")


calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(row=3, column=3)

window.mainloop()
