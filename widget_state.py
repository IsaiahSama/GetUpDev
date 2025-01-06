"""This file will be responsible for handling the state of the application"""
from tkinter import StringVar, IntVar, BooleanVar
import pyttsx3 as ttsx

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
    alert_with_tts: BooleanVar
    
    minutes: StringVar
    seconds: StringVar
    active_text: StringVar
    locked_in_text: StringVar
    locked_in_button_text: StringVar
    alert_text: StringVar
    
    tts: ttsx.Engine
    
    def __init__(self):
        self.notification_message = StringVar(value="Time to get up and stretch!")
        self.use_tts = BooleanVar(value=False)
        self.voice = IntVar(value=0)
        self.active = False
        self.interval = IntVar(value=15)
        self.remaining_time = IntVar(value=0)
        self.locked_in = BooleanVar(value=False)
        self.lock_in_cooldown = IntVar(value=0)
        self.break_count = IntVar(value=1)
        self.notify = BooleanVar(value=False)
        self.alert_with_tts = BooleanVar(value=False)
        
        self.minutes = StringVar(value="--")
        self.seconds = StringVar(value="--")
        self.active_text = StringVar(value="Not Running")
        self.locked_in_text = StringVar(value="Not locked in")
        self.locked_in_button_text = StringVar(value="Lock In")
        self.alert_text = StringVar(value="App notifications go here!")
        
    def update_remaining_time(self, remaining_time: int):
        self.remaining_time.set(remaining_time)
        
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        
        self.minutes.set(str(minutes).zfill(2))
        self.seconds.set(str(seconds).zfill(2))
        
    def update_active(self, active: bool):
        self.active = active
        self.active_text.set("Running" if active else "Not Running")
        
    def alert(self, message, useTTS=True):
        self.alert_text.set(message)
        
        if self.alert_with_tts.get() and useTTS:
            self.speak(message)
        
    def speak(self, message: str = None):
        to_speak = message or self.notification_message.get()
        if self.use_tts.get():
            self.tts = ttsx.init()
            
            voices = self.tts.getProperty("voices")
            self.tts.setProperty("voice", voices[self.voice.get()].id)
            
            self.tts.say(to_speak)
            self.tts.runAndWait()
            self.tts.stop()
            
    def update_locked_in(self, locked_in: bool):
        self.locked_in.set(locked_in)
        
        if locked_in:
            self.locked_in_button_text.set("Exit Lock In")
            self.locked_in_text.set("Locked in!")
        else:
            self.locked_in_button_text.set("Lock in!")
            self.locked_in_text.set("Not locked in")
