"""This file will be responsible for handling the state of the application"""
from tkinter import StringVar, IntVar, BooleanVar

class WidgetState:
    """This will be the state of the application"""
    
    notification_message: StringVar
    use_tts: BooleanVar
    voice: IntVar
    active: bool
    interval: IntVar # Time in minutes
    remaining_time: IntVar # This will be the remaining time in seconds
    locked_in: BooleanVar
    lock_in_cooldown: IntVar
    break_count: IntVar
    notify: BooleanVar
    
    minutes: StringVar
    seconds: StringVar
    active_text: StringVar
    
    def __init__(self):
        self.notification_message = StringVar(value="Time to get up and stretch!")
        self.use_tts = BooleanVar(value=False)
        self.voice = IntVar(value=0)
        self.active = False
        self.interval = IntVar(value=15)
        self.remaining_time = IntVar(value=0)
        self.locked_in = BooleanVar(value=False)
        self.lock_in_cooldown = IntVar(value=0)
        self.break_count = IntVar(value=0)
        self.notify = BooleanVar(value=False)
        
        self.minutes = StringVar(value="--")
        self.seconds = StringVar(value="--")
        self.active_text = StringVar(value="Not Running")
        
    def update_remaining_time(self, remaining_time: int):
        self.remaining_time.set(remaining_time)
        
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        
        self.minutes.set(str(minutes).zfill(2))
        self.seconds.set(str(seconds).zfill(2))
        
    def update_active(self, active: bool):
        self.active = active
        self.active_text.set("Running" if active else "Not Running")
