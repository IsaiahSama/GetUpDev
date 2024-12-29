"""This will be the builder for the TK application."""
from tkinter import *

class WidgetBuilder:
    """This class will take care of calling the code to create the necessary widgets."""
    
    def __init__(self, root, state):
        self.root = root
        
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
        
        heading = Label(header_frame, text="Get up Dev!", font = 70)
        heading.pack()

        overview = Message(header_frame, text="Welcome to Get Up Dev! A simple application designed to make sure you don't spend too much consecutive time looking at a screen.", anchor=CENTER, justify=CENTER, width=600)
        overview.pack()
    
    def render_remaining_time(self):
        time_frame = Frame(self.root)
        time_frame.pack(anchor=E)

        current_time_label = Label(time_frame, text="Remaining Time:")
        current_time_label.pack(side = LEFT, fill= BOTH, expand=True)
        
        minute_time_label = Label(time_frame, textvariable=StringVar(value=25))
        minute_time_label.pack(side = LEFT, fill= BOTH, expand=True)

        colon_label = Label(time_frame, text=":")
        colon_label.pack(side=LEFT)

        second_time_label = Label(time_frame, textvariable=StringVar(value=37))
        second_time_label.pack(side = LEFT, fill= BOTH, expand=True)
    
    def render_settings(self):
        settings_frame = Frame(self.root)
        settings_frame.pack()

        time_label = Label(settings_frame, text="Set interval time in minutes (10-30)")
        time_label.pack()

        time_entry = Spinbox(settings_frame, from_=10, to=30)
        time_entry.pack()

        notif_frame = Frame(settings_frame)
        notif_frame.pack()

        message_label = Label(settings_frame, text="How should I notify you?")
        message_label.pack()

        message_value = Entry(settings_frame, width=70, textvariable=StringVar(value="Time to get up and stretch!"))
        message_value.pack()

        use_tts_button = Checkbutton(settings_frame, text="Use tts?", variable=BooleanVar(value=False))
        use_tts_button.pack()

        no_voice = Radiobutton(settings_frame, text="No Voice", variable=IntVar(), value=0)
        male_voice = Radiobutton(settings_frame, text="Male", variable=IntVar(), value=1)
        female_voice = Radiobutton(settings_frame, text="Female", variable=IntVar(), value=2)

        no_voice.pack(side=LEFT, fill=BOTH, expand=True)
        male_voice.pack(side=LEFT, fill=BOTH, expand=True)
        female_voice.pack(side=LEFT, fill=BOTH, expand=True)
    
    def render_action_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack()

        start_timer_button = Button(button_frame, text="Start", width=15, bg="green")
        start_timer_button.pack(side=LEFT)

        stop_timer_button = Button(button_frame, text="Stop", width=15, bg="red")
        stop_timer_button.pack(side=LEFT, padx=10)

        lockin_button = Button(button_frame, text="Lock in!", width=15, bg="yellow")
        lockin_button.pack(side=LEFT)
    
    def build_popup(self):
        pass