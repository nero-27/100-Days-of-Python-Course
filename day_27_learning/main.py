from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

my_label = Label(text="this a label", font=('Arial', 20, "bold"))
my_label.pack()

my_label['text'] = "new text"
# my_label.config(text="new new text")

def button_clicked():
    my_label.config(text=input.get())

input = Entry(width=20)
input.pack()
# input.get()

button = Button(text="button", command=button_clicked)
button.pack()

window.mainloop()