from tkinter import *

def miles_to_kilometer():
    miles = float(miles_entry.get())
    km = round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")

windows = Tk()
windows.title("Miles to Kilometer converter")
windows.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text = "km")
kilometer_label.grid(column=2, row=1)
calculate_button = Button(text="Caculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)

windows.mainloop()