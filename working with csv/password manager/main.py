from tkinter import *
from tkinter import messagebox
import random as r
import csv
import pyperclip
import string
import json
import os

DATA_FILE_PATH = "data.json"
# --------------------------------- SEARCH -------------------------------------- #


def search_info():
    site = website.get()

    try:
        try:
            with open(DATA_FILE_PATH, mode="r") as data_file:
                content = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Data missing!",
                                 message="Data file not found!")
        else:
            user = content[site]["email"]
            passwd = content[site]["password"]

    except:
        messagebox.showerror(
            title="Error", message="No such site found! Check for spellings or add data.")

    else:
        messagebox.showinfo(
            title=site, message=f"Username/E-mail: {user} \nPassword: {passwd}")

    finally:
        website.delete(0, END)
        password.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_random_password():

    password.delete(0, END)
    length = r.randint(8, 12)
    random_password = ''.join(r.choices(
        string.ascii_letters + string.digits, k=length))

    password.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    site = website.get()
    user = username.get()
    passwd = password.get()
    new_data = {
        site: {
            "email": user,
            "password": passwd
        }
    }

    if len(site) == 0 or len(user) == 0 or len(passwd) == 0:
        messagebox.showwarning(
            title="Oops", message="You have left empty spaces!")

    else:

        is_ok = messagebox.askokcancel(
            title=site, message=f"These are the details entered:\nE-mail/Username: {user} \nPassword: {passwd} \nAre they correct?")

        if is_ok:
            try:
                with open(DATA_FILE_PATH, mode="r") as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open(DATA_FILE_PATH, mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open(DATA_FILE_PATH, mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=455, height=400)
window.maxsize(width=455, height=400)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(
    file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='e')

website = Entry(width=30)
website.grid(row=1, column=1, columnspan=2, sticky='w')
website.focus()

search_button = Button(text="Search",
                       command=search_info, width=14)
search_button.grid(row=1, column=2, sticky='w')

# Add a space between rows 1 and 2
space_label_1 = Label(window, text="")
space_label_1.grid(row=2)

username_label = Label(text="E-mail/Username:")
username_label.grid(row=3, column=0, sticky='e')

username = Entry(width=45)
username.insert(0, "johndoe@gmail.com")
username.grid(row=3, column=1, columnspan=2, sticky='w')

# Add a space between rows 3 and 4
space_label_2 = Label(window, text="")
space_label_2.grid(row=4)

password_label = Label(text="Password:")
password_label.grid(row=5, column=0, sticky='e')

password = Entry(width=30)
password.grid(row=5, column=1, sticky='w')

generate_pass = Button(text="Generate Password",
                       command=generate_random_password)
generate_pass.grid(row=5, column=2, sticky='w')

# Add a space between rows 5 and 6
space_label_3 = Label(window, text="")
space_label_3.grid(row=6)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=7, column=1, columnspan=2)

window.mainloop()
