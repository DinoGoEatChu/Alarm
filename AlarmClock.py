from datetime import datetime
from tkinter import ttk
import winsound
import time
from tkinter import *
from threading import *
import pygame

root = Tk()
root.geometry("400x300")

alarm_on = True

#threading
def Threading():
    thread1 = Thread(target = alarm)
    thread1.start()
    root.iconify() #minimize alarm

def alarm():
    global alarm_on
    pygame.mixer.init()
    while True:
        #set alarm
        alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        #waint 1 second
        time.sleep(1)

        #get current time
        current_time = datetime.now().strftime("%H:%M:%S")
        
        #check if alarm time = now
        if current_time == alarm_time:
            print("Wakey Wakey Eggs and Bakey")
            #play alarm sound any .wav file
            pygame.mixer.music.load("Gerudo-Valley.wav")
            pygame.mixer.music.play(-1) #loop alarm sound
            root.deiconify() #restore alarm window  
            break

def stop_alarm():
    global alarm_on
    alarm_on = False
    pygame.mixer.music.stop() #stop alarm music
          

style = ttk.Style()

frame = Frame(root)
frame.pack(expand=True)

#Labels and app itself
L1=Label(frame,text="Alarm Clock",font=("Helvetica 20 bold"),foreground="red")
L2=Label(frame,text="Set Time 24HR",font=("Helvetica 15 bold"))
L1.grid(row=0, column=0, columnspan=3, pady=10)
L2.grid(row=1, column=0, columnspan=3)

#alarm time entry
hour = StringVar()
minute = StringVar()
second = StringVar()

#root, variable, box color bg, width, fontsize
hr = Entry(frame, textvariable=hour, width = 4, font = (20))
min = Entry(frame, textvariable=minute, width = 4, font = (20))
sec = Entry(frame, textvariable=second, width = 4, font = (20))
hour.set("HH")
minute.set("MM")
second.set("SS")

hr.grid(row=3, column=0)
min.grid(row=3, column=1)
sec.grid(row=3, column=2)

#set alarm button
Button(frame,text="Set Alarm",font=("Helvetica 15"), background="green",command=Threading).grid(row=4, column=0, columnspan=3, pady=20)
Button(frame, text="Stop Alarm", font=("Helvetica 15"), background="red", command=stop_alarm).grid(row=5, column=0, columnspan=3, pady=10)

# Execute Tkinter
root.mainloop()