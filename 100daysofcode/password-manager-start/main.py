from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
from typing import TextIO


def save():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    with open("data.txt", "a") as data:
        data.write(f"{website_name} | {email_name} | {password_name}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.config(padx=50, pady=50)
windows.title("PASSWORD MANAGER")

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=600, height=600)
canvas.config(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=60)
website_entry.grid(row=1, column=1, columnspan=2)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
