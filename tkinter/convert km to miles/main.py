import tkinter as tk

window = tk.Tk()
window.title("Converter")
window.configure(padx=15, pady=15)

FONT = ("Arial", 10, "normal")

heading = tk.Label(text="Convert kms to miles", font=("Arial", 18, "bold"))
heading.grid(column=1, row=0)


in_miles = 0


# convert input from km to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


def calculate():
    global in_miles
    in_miles = km_to_miles(float(km_input.get()))
    miles_output.configure(text=str(in_miles))


# take input in kms
km_label = tk.Label(text="km",
                    font=FONT)
km_label.grid(column=2, row=1)
km_input = tk.Entry()
km_input.grid(column=1, row=1)
km_input.configure(width="15")

is_equal_to = tk.Label(text=" is equal to ", font=FONT)
is_equal_to.grid(column=0, row=2)


# calculate button
calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)

miles_output = tk.Label(text="0")
miles_output.grid(column=1, row=2)

miles = tk.Label(text="miles", font=FONT)
miles.grid(column=2, row=2)


window.mainloop()
