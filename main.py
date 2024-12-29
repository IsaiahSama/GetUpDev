from tkinter import *

root = Tk()
root.geometry("620x480")
root.title("Get up Dev!")

heading = Label(root, text="Get up Dev!", font = 70)
heading.pack()

overview = Message(root, text="Welcome to Get Up Dev! A simple application designed to make sure you don't spend too much consecutive time looking at a screen.")
overview.pack(padx=0)

current_time_label = Label(root, text="Remaining Time:")
current_time_label.pack()

minute_value = IntVar(value=25)
second_value = IntVar(value=37)

minute_time_label = Label(root, textvariable=minute_value)
minute_time_label.pack()

colon_label = Label(root, text=":")
colon_label.pack()

second_time_label = Label(root, textvariable=second_value)
second_time_label.pack()

time_label = Label(root, text="Set interval time in minutes (10-30)")
time_label.pack()

time_entry = Spinbox(root, from_=10, to=30)
time_entry.pack()

message_label = Label(root, text="How should I notify you?")
message_label.pack()

message_value = Entry(root)
message_value.pack()

use_tts = BooleanVar()

use_tts_button = Checkbutton(root, text="Use tts?", variable=use_tts)
use_tts_button.pack()

voice = IntVar(value=0)

no_voice = Radiobutton(root, text="No Voice", variable=voice, value=0)
male_voice = Radiobutton(root, text="Male", variable=voice, value=1)
female_voice = Radiobutton(root, text="Female", variable=voice, value=2)

no_voice.pack()
male_voice.pack()
female_voice.pack()

start_timer_button = Button(root, text="Start", width=15)
start_timer_button.pack()

stop_timer_button = Button(root, text="Stop", width=15)
stop_timer_button.pack()

lockin_button = Button(root, text="Lock in!", width=15)
lockin_button.pack()

root.mainloop()