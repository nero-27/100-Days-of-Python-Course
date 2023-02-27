from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=200, height=80)



def convert():
    km = float(miles_entry.get()) * 1.61
    answer_label.config(text=str(km))


miles_entry = Entry(width=20)
miles_label = Label(text="miles")
km_label = Label(text="km")
equal_to_label = Label(text="is equal to ")
convert_button = Button(text="Convert", command=convert)
answer_label = Label(text='0')

miles_entry.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equal_to_label.grid(column=0, row=1)
answer_label.grid(column=1, row=1)
convert_button.grid(column=1, row=2)



window.mainloop()
