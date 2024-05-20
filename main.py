from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    print(reps)
    if reps == 9:
        timer_label.config(text="Session Finish ", fg=GREEN)
        return

    elif reps % 2 != 0:

        count_down(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)

    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Long Break", fg=RED)

    else:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global marks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            marks += "✓"
            print(marks)
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(113, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
