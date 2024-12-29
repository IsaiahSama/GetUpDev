from tkinter import *

root = Tk()
root.geometry("620x360")
root.title("Get up Dev!")

heading = Label(root, text="Get up Dev!", font = 70)
heading.pack()

overview = Message(root, text="Welcome to Get Up Dev! A simple application designed to make sure you don't spend too much consecutive time looking at a screen.", anchor=CENTER, justify=CENTER, width=600)
overview.pack()

time_frame = Frame(root)
time_frame.pack(anchor=E)

current_time_label = Label(time_frame, text="Remaining Time:")
current_time_label.pack(side = LEFT, fill= BOTH, expand=True)

minute_value = StringVar(value=25)
second_value = StringVar(value=37)

minute_time_label = Label(time_frame, textvariable=minute_value)
minute_time_label.pack(side = LEFT, fill= BOTH, expand=True)

colon_label = Label(time_frame, text=":")
colon_label.pack(side=LEFT)

second_time_label = Label(time_frame, textvariable=second_value)
second_time_label.pack(side = LEFT, fill= BOTH, expand=True)

settings_frame = Frame(root)
settings_frame.pack()

time_label = Label(settings_frame, text="Set interval time in minutes (10-30)")
time_label.pack()

time_entry = Spinbox(settings_frame, from_=10, to=30)
time_entry.pack()

notif_frame = Frame(settings_frame)
notif_frame.pack()

message_label = Label(settings_frame, text="How should I notify you?")
message_label.pack()

notification_message = StringVar(value="Time to get up and stretch!")

message_value = Entry(settings_frame, width=70, textvariable=notification_message)
message_value.pack()

use_tts = BooleanVar()

use_tts_button = Checkbutton(settings_frame, text="Use tts?", variable=use_tts)
use_tts_button.pack()

voice = IntVar(value=0)

no_voice = Radiobutton(settings_frame, text="No Voice", variable=voice, value=0)
male_voice = Radiobutton(settings_frame, text="Male", variable=voice, value=1)
female_voice = Radiobutton(settings_frame, text="Female", variable=voice, value=2)

no_voice.pack(side=LEFT, fill=BOTH, expand=True)
male_voice.pack(side=LEFT, fill=BOTH, expand=True)
female_voice.pack(side=LEFT, fill=BOTH, expand=True)

button_frame = Frame(root)
button_frame.pack()

start_timer_button = Button(button_frame, text="Start", width=15, bg="green")
start_timer_button.pack(side=LEFT)

stop_timer_button = Button(button_frame, text="Stop", width=15, bg="red")
stop_timer_button.pack(side=LEFT, padx=10)

lockin_button = Button(button_frame, text="Lock in!", width=15, bg="yellow")
lockin_button.pack(side=LEFT)

root.mainloop()