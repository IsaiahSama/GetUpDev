from tkinter import *
from widget_builder import WidgetBuilder
from widget_state import WidgetState

class Main:
    """
    This class is used to create the main window of the application.
    """
    
    root = None
    widget_builder = None
    
    def __init__(self):
        self.setup()
        
    def setup(self):
        self.root = Tk()
        self.root.geometry("620x360")
        self.root.title("Get up Dev!")
        
        self.state = WidgetState()
        
        self.widget_builder = WidgetBuilder(self.root, self.state)
        
    def run(self):
        self.widget_builder.build_home_page()
        self.root.mainloop()
        
if __name__ == "__main__": 
    Main().run()