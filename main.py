from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops...!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you had enter:\nEmail: {email}\nPassword:"
                                               f" {password}\nfor this Website {website}.\nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                    file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=35)


# Logo
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


# LABELS
website_label = Label(text="Website:", font="bold" )
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font="bold")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font="bold")
password_label.grid(column=0, row=3)


# ENTRIES
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, string="vinayop@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


# BUTTONS
add_button = Button(text="Add", font="bold", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
generate_button = Button(text="Generate Password", font="bold", command=generate_password)
generate_button.grid(column=2, row=3)


window.mainloop()
