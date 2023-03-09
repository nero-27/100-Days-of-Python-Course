from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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

    json_data = {
        website_ent: {
            'email': email_ent,
            'password': password_ent,
        },
    }
    # entry = f"{website_ent} | {email_ent} | {password_ent}"

    is_not_empty = len(website_ent) == 0 or len(password_ent) == 0
    if is_not_empty:
        messagebox.showerror(title="Blank fields", message="You have left some fields blank. Please fill them.")
    else:
        is_ok = messagebox.askokcancel(title=website_ent, message=f"You entered:\n Website: {website_ent} \n Password: {password_ent} \n Would you like to save?")

        if is_ok:
            try:
                with open('password_manager.json', 'r') as pm:
                    # read old data
                    data = json.load(pm)
                    print(data)
            except FileNotFoundError:
                with open('password_manager.json', 'w') as pm:
                    # write new data to json file
                    json.dump(json_data, pm, indent=4)
            else:
                # update old data with new data
                data.update(json_data)
                print(data)
                with open('password_manager.json', 'w') as pm:
                    # write new data to json file
                    json.dump(data, pm, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    website_ent = website_entry.get()

    try:
        with open("password_manager.json", 'r') as pm:
            data = json.load(pm)
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message="File not found. Add a new entry.")
    else:
        if website_ent in data.keys():
            email_data = data[website_ent]['email']
            password_data = data[website_ent]['password']
            messagebox.showinfo(title=website_ent, message=f"{email_data}\n{password_data}")
        else:
            messagebox.showerror(title="Not found", message="Website not found")
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
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)





window.mainloop()