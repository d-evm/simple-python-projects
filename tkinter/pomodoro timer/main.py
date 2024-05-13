from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def pause_timer():
    window.after_cancel(timer)
    reset_button.config(text="Reset", command=reset_timer)
    start_button.destroy()


def reset_timer():
    global rep
    global timer
    timer = None
    rep = 1
    reset_button.config(text="Pause", command=pause_timer)
    timer_text.config(text="Timer")
    canvas.itemconfig(countdown_timer, text="00:00")
    start_button = Button(text="Start", command=start_timer)
    start_button.grid(row=2, column=0)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    sessions = rep // 2
    check_marks.config(text="✅"*sessions)

    if rep == 8:
        countdown(LONG_BREAK_MIN*60)
        timer_text.config(text="It's a long break!", fg=RED)
        rep = 0
        sessions = 0
    elif rep % 2 != 0:
        countdown(WORK_MIN*60)
        timer_text.config(text="Time to work!", fg=GREEN)
    else:
        countdown(SHORT_BREAK_MIN*60)
        timer_text.config(text="Have a short break!", fg=PINK)
    rep += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    mins = "{:02d}".format(count // 60)
    secs = "{:02d}".format(count % 60)

    canvas.itemconfig(countdown_timer, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file=r"D:\python course\day 28 - pomodoro timer\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
countdown_timer = canvas.create_text(103, 130, text="00:00", fill="white",
                                     font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_text = Label(text="Timer", font=(FONT_NAME, 37, "bold"))
timer_text.config(bg=YELLOW, fg=GREEN)
timer_text.grid(column=1, row=0)

reset_button = Button(text="Pause", command=pause_timer)
reset_button.grid(row=2, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

check_marks = Label(text="", fg=RED, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
