from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text=f"00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN)
    check_mark.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 2#WORK_MIN*60
    short_break_sec = 3#SHORT_BREAK_MIN*60
    long_break_sec = 4#LONG_BREAK_MIN*60
    reps += 1
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", font=(FONT_NAME, 32, "bold"), fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", font=(FONT_NAME, 32, "bold"), fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 32, "bold"), fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count//60
    count_sec = count % 60
    if count_sec//10 == 0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark, fg=GREEN, bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
myimg = PhotoImage(file=r"C:\Users\koush\PycharmProjects\days100code\DAY-28\tomato.png")
canvas.create_image(150, 170, image=myimg)
canvas_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.pack()
#count_down(5)
start_but = Button(text="START", command=start_timer)
start_but.place(x=0, y=200)
stop_but = Button(text="STOP", command=reset_timer)
stop_but.place(x=260, y=200)
timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN)
timer_label.place(x=100, y=0)
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.place(x=150, y=300)
window.mainloop()