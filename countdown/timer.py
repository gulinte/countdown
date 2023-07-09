from tkinter import *
from playsound import playsound
import time

root=Tk()
root.title("Timer")
root.geometry("400x400")
root.config(bg="#FDF4F5")
root.resizable(False,False)

heading=Label(root,text="Countdown", font="helvetica 36 bold", bg="#FDF4F5", fg="#E8A0BF")
heading.pack(pady=10)

def clock():
    clock_time=time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time=Label(root, font=("arial",15,"bold"), text="", fg="#FDF4F5", bg="#E8A0BF")

current_time.pack(anchor='center')
clock()

hrs=StringVar()
Entry(root,textvariable=hrs, width=2, font="helvetica 50" , bd=0, bg="#FDF4F5").place(x=30,y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins, width=2, font="helvetica 50" , bd=0, bg="#FDF4F5").place(x=150,y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec, width=2, font="helvetica 50" , bd=0, bg="#FDF4F5").place(x=270,y=155)
sec.set("00")

Label(root,text="hours" , font="helvetica 12", bg="#E8A0BF", fg="#fff").place(x=105,y=200)
Label(root,text="min" , font="helvetica 12", bg="#E8A0BF", fg="#fff").place(x=225,y=200)
Label(root,text="sec" , font="helvetica 12", bg="#E8A0BF", fg="#fff").place(x=345,y=200)

def start_timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    countdown(times)

def countdown(times):
    if times > 0:
        minute, second = divmod(times, 60)
        hour, minute = divmod(minute, 60)

        sec.set(str(second).zfill(2))
        mins.set(str(minute).zfill(2))
        hrs.set(str(hour).zfill(2))

        root.update()
        root.after(1000, countdown, times - 1)
    else:
        playsound("b r u h.wav")
        sec.set("00")
        mins.set("00")
        hrs.set("00")

button=Button(root,text="Start", bg="#E8A0BF" , bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=start_timer)
button.pack(padx=5,pady=40,side=BOTTOM)

root.mainloop()
