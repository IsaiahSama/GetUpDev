"""This will be the builder for the TK application."""
from tkinter import *
from widget_state import WidgetState

try:
    import winsound
    HAS_WINSOUND = TRUE
except:
    HAS_WINSOUND = FALSE

class WidgetBuilder:
    """This class will take care of calling the code to create the necessary widgets."""
    
    def __init__(self, root: Tk, state: WidgetState):
        self.root = root
        self.state = state
        
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
    
    def render_remaining_time(self):
        time_frame = Frame(self.root)
        time_frame.pack(anchor=E)

        Label(time_frame, text="Remaining Time:").pack(side = LEFT, fill= BOTH, expand=True)
        
        Label(time_frame, textvariable=self.state.minutes).pack(side = LEFT, fill= BOTH, expand=True)

        Label(time_frame, text=":").pack(side=LEFT)

        Label(time_frame, textvariable=self.state.seconds).pack(side = LEFT, fill= BOTH, expand=True)
    
    def render_settings(self):
        settings_frame = Frame(self.root)
        settings_frame.pack()

        Label(settings_frame, text="Set interval time in minutes (10-30)").pack()

        Spinbox(settings_frame, from_=10, to=30).pack()

        Label(settings_frame, text="How should I notify you?").pack()

        Entry(settings_frame, width=70, textvariable=self.state.notification_message).pack()

        Checkbutton(settings_frame, text="Use tts?", variable=self.state.use_tts).pack()

        Radiobutton(settings_frame, text="No Voice", variable=self.state.voice, value=0).pack(side=LEFT, fill=BOTH, expand=True)

        Radiobutton(settings_frame, text="Male", variable=self.state.voice, value=1).pack(side=LEFT, fill=BOTH, expand=True)

        Radiobutton(settings_frame, text="Female", variable=self.state.voice, value=2).pack(side=LEFT, fill=BOTH, expand=True)
    
    def render_action_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack()

        Button(button_frame, text="Start", width=15, bg="green").pack(side=LEFT)

        Button(button_frame, text="Stop", width=15, bg="red").pack(side=LEFT, padx=10)

        Button(button_frame, text="Lock in!", width=15, bg="yellow").pack(side=LEFT)
        
        Button(button_frame, text="Trigger Popup!", width=15, bg="purple", command=self.render_popup).pack(side=LEFT, padx=10)
    
    def render_popup(self):
    
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
        
        window.title("Time to get up!")
        
        Message(window, textvariable=self.state.notification_message, width=180).pack()
        
        count_frame = Frame(window)
        count_frame.pack(pady=5)
        
        Label(count_frame, text="Number of breaks taken today:").pack(side=LEFT)
        Label(count_frame, textvariable=self.state.break_count).pack(side=LEFT)
        
        button_frame = Frame(window)
        button_frame.pack()
        
        Button(button_frame, text="OK", width=10, bg="green", command=window.destroy).pack(side=LEFT, padx=5)
        
        Button(button_frame, text="Lock in!", width=10, bg="yellow").pack(side=LEFT, padx=5)