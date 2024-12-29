"""This file will be responsible for handling the state of the application"""
from tkinter import StringVar, IntVar, BooleanVar

class WidgetState:
    """This will be the state of the application"""
    
    notification_message: StringVar
    use_tts: BooleanVar
    voice: IntVar
    active: BooleanVar
    interval: IntVar
    remaining_time: IntVar # This will be the remaining time in seconds
    locked_in: BooleanVar
    lock_in_cooldown: IntVar
    break_count: IntVar
    
    minutes: StringVar
    seconds: StringVar
    
    def __init__(self):
        self.notification_message = StringVar(value="Time to get up and stretch!")
        self.use_tts = BooleanVar(value=False)
        self.voice = IntVar(value=0)
        self.active = BooleanVar(value=False)
        self.interval = IntVar(value=15)
        self.remaining_time = IntVar(value=0)
        self.locked_in = BooleanVar(value=False)
        self.lock_in_cooldown = IntVar(value=0)
        self.break_count = IntVar(value=0)
        
        self.minutes = StringVar(value="--")
        self.seconds = StringVar(value="--")