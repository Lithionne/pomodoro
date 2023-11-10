from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5  # 25
SHORT_BREAK_MIN = 1  # 5
LONG_BREAK_MIN = 1.5  # 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    # pomodoro_is_on = True
    # while pomodoro_is_on:

    if reps % 2 != 0:
        count_down(work_time)
        timer_label.config(text="Work", fg=GREEN)

    elif reps == 8:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)

    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=10, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.config(padx=0, pady=10, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# count_down(5)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
# label_check_mark.config(text="✔")
label_check_mark.grid(column=1, row=3)

label_blank = Label(bg=YELLOW)
label_blank.grid(column=1, row=4)


window.mainloop()
