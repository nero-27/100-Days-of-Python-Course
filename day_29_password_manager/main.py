from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password_list = "".join(password_list)



    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_ent = website_entry.get()
    email_ent = email_entry.get()
    password_ent = password_entry.get()
    entry = f"{website_ent} | {email_ent} | {password_ent}"

    is_not_empty = len(website_ent) == 0 or len(password_ent) == 0
    if is_not_empty:
        messagebox.showerror(title="Blank fields", message="You have left some fields blank. Please fill them.")
    else:
        is_ok = messagebox.askokcancel(title=website_ent, message=f"You entered:\n Website: {website_ent} \n Password: {password_ent} \n Would you like to save?")

        if is_ok:
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            with open('password_manager.txt', 'a') as pm:
                pm.write(f"{entry}\n")

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)

canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "richavpatel98@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()