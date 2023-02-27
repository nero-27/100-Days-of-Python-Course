from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def start():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK MODE", fg=GREEN)



def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN, font=(FONT_NAME, 20, "bold"))
    check_mark.config(text="")
    global reps
    reps = 0


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min == 0:
        count_min = "00"
    elif count_min < 10:
        count_min = f"0{count_min}"

    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check_mark.config(text=mark)



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 20, "bold"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(column=2, row=2)
timer_label.grid(column=2, row=0)


start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=3, row=3)
check_mark = Label(text="", fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_mark.grid(column=2, row=4)

window.mainloop()
