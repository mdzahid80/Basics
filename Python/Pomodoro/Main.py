from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Timer=None
rep=0
checkmark=" "

# ---------------------------- TIMER RESET Function ------------------------------- # 
def reset_timer():
    global rep
    
    Window.after_cancel(Timer)
    rep=0
    canvas.itemconfig(timer_text,text=f"00:00")
    Timer_label.config(text="Timer",fg=GREEN ,font=[FONT_NAME,35])
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep+=1

    if rep%8==0:
        count_down(LONG_BREAK_MIN*60)
        Timer_label.config(text="Break",fg=RED ,font=[FONT_NAME,35])
    elif rep%2==0:
        count_down(SHORT_BREAK_MIN*60)
        Timer_label.config(text="Break",fg=PINK ,font=[FONT_NAME,35])
    else :
        count_down(WORK_MIN*60)
        Timer_label.config(text="Work",fg=GREEN ,font=[FONT_NAME,35])
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global checkmark
    global Timer
    count_min= math.floor(count/60)
    count_sec= count%60

    if count_sec<10:
        count_sec= f"0{count_sec}"

    if count_min<10:
        count_min= f"0{count_min}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        Timer=Window.after(1000, count_down, count-1)

    else:
        start_timer()
        checkmark=""
        work_sess=math.floor(rep/2)

        for _ in range(work_sess):
            checkmark += "✓"
        check.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #

Window=Tk()
Window.title("tomato")
Window.config(padx=50,pady=50,bg=YELLOW)

canvas=Canvas(width=205,height=224, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(103,112, image=img)
timer_text=canvas.create_text(103,130,text=0,fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


Timer_label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
Timer_label.grid(row=0,column=1)

butstrt=Button(text="Start",command=start_timer,highlightthickness=0)
butstrt.grid(row=2,column=0)

check=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35))
check.grid(row=3,column=1)

butrst=Button(text="Reset",command=reset_timer,highlightthickness=0)
butrst.grid(row=2,column=2)



Window.mainloop()  
