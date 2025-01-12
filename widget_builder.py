"""This will be the builder for the TK application."""
from tkinter import *
from widget_state import WidgetState
from timer import ThreadedTimer

try:
    import winsound
    HAS_WINSOUND = TRUE
except:
    HAS_WINSOUND = FALSE

class WidgetBuilder:
    """This class will take care of calling the code to create the necessary widgets."""
    
    def __init__(self, root: Tk, state: WidgetState, timer: ThreadedTimer):
        self.root = root
        self.state = state
        self.timer = timer
        
    def build_home_page(self):
        # Create the header
        self.render_header()
        
        # Display remaining time
        self.render_remaining_time()
        
        # Display Settings
        self.render_settings()
        
        # Create Action Buttons
        self.render_action_buttons()
        
    def render_header(self):
        header_frame = Frame(self.root)
        header_frame.pack()
        
        Label(header_frame, text="Get up Dev!", font = 70).pack()

        Message(header_frame, text="Welcome to Get Up Dev! A simple application designed to make sure you don't spend too much consecutive time looking at a screen.", anchor=CENTER, justify=CENTER, width=600).pack()
        
        Message(header_frame, textvariable=self.state.alert_text, fg="red", anchor=CENTER, justify=CENTER, width=400).pack()
    
    def render_remaining_time(self):
        info_frame = Frame(self.root)
        info_frame.pack(anchor=W, padx=10)
        
        Label(info_frame, textvariable=self.state.active_text).pack(anchor=W)
        
        time_frame = Frame(info_frame)
        time_frame.pack()
        
        Label(time_frame, text="Remaining Time:").pack(side = LEFT)
        Label(time_frame, textvariable=self.state.minutes).pack(side = LEFT)
        Label(time_frame, text=":").pack(side = LEFT)
        Label(time_frame, textvariable=self.state.seconds).pack(side = LEFT)
        
        lock_in_frame = Frame(info_frame)
        lock_in_frame.pack(anchor=W)
        
        Label(lock_in_frame, textvariable=self.state.locked_in_text).pack(anchor=W)
        
        Label(lock_in_frame, text="Lock in Cooldown:").pack(side = LEFT, anchor=W)
        Label(lock_in_frame, textvariable=self.state.lock_in_cooldown).pack(side = LEFT, anchor=W)
        
        def run(*_):
            self.render_popup()
        
        self.state.notify.trace_add("write", run)
    
    def render_settings(self):
        settings_frame = Frame(self.root)
        settings_frame.pack()

        Label(settings_frame, text="Set interval time in minutes (10-30)").pack()

        Spinbox(settings_frame, from_=10, to=30, textvariable=self.state.interval).pack()

        Label(settings_frame, text="How should I notify you?").pack()

        Entry(settings_frame, width=70, textvariable=self.state.notification_message).pack()
        
        tts_frame = Frame(settings_frame)
        tts_frame.pack(expand=TRUE, anchor=CENTER)

        Checkbutton(tts_frame, text="Use TTS?", variable=self.state.use_tts).pack(side=LEFT)
        
        Checkbutton(tts_frame, text="Read out message notifications?", variable=self.state.alert_with_tts).pack(side=LEFT)
        
        Label(settings_frame, text="Select Voice:").pack()

        Radiobutton(settings_frame, text="Male", variable=self.state.voice, value=0).pack(side=LEFT, fill=BOTH, expand=True)

        Radiobutton(settings_frame, text="Female", variable=self.state.voice, value=1).pack(side=LEFT, fill=BOTH, expand=True)
    
    def render_action_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack()

        Button(button_frame, text="Start", width=15, bg="green", command=self.timer.run).pack(side=LEFT)

        Button(button_frame, text="Stop", width=15, bg="red", command=self.timer.stop).pack(side=LEFT, padx=10)

        Button(button_frame, textvariable=self.state.locked_in_button_text, width=15, bg="yellow", command=self.lock_in).pack(side=LEFT)
    
    def render_popup(self):
        
        if self.state.notify.get() == FALSE:
            return
    
        if HAS_WINSOUND:
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            
        window = Toplevel()
        
        w = 200
        h = 100
        
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        
        x = (sw - w) // 2
        y = (sh - h) // 2
        
        window.geometry(f"{w}x{h}+{x}+{y}")
        window.attributes("-topmost", 1)
        
        window.title("Time to get up!")
        
        Message(window, textvariable=self.state.notification_message, width=180).pack()
        
        count_frame = Frame(window)
        count_frame.pack(pady=5)
        
        Label(count_frame, text="Number of breaks taken today:").pack(side=LEFT)
        Label(count_frame, textvariable=self.state.break_count).pack(side=LEFT)
        
        button_frame = Frame(window)
        button_frame.pack()
                
        def close_window_and_restart_timer():
            self.state.break_count.set(self.state.break_count.get() + 1)
            window.destroy()
            self.timer.reset()
            self.timer.run()
        
        Button(button_frame, text="OK", width=10, bg="green", command=close_window_and_restart_timer).pack(side=LEFT, padx=5)
        
        Button(button_frame, textvariable=self.state.locked_in_button_text, width=10, bg="yellow", command=self.lock_in).pack(side=LEFT, padx=5)
        
        window.protocol("WM_DELETE_WINDOW", close_window_and_restart_timer)
        
        self.state.speak()
        
        self.state.notify.set(False)
        
    def lock_in(self):        
        if self.state.locked_in.get() == False and self.state.lock_in_cooldown.get() == 0:
            if not self.state.active:
                self.timer.run()
                
            self.state.update_locked_in(True)
            self.state.lock_in_cooldown.set(60 * 60)
            self.state.alert("Locking in")
            
        elif self.state.locked_in.get() == True:
            self.state.update_locked_in(False)
            self.state.lock_in_cooldown.set(0)
            self.state.alert("Locking out!")
            
        else:
            self.state.alert("You can't lock in right now!")