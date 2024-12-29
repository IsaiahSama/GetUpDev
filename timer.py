"""This class will be responsible for managing the timer"""
from widget_state import WidgetState
from threading import Thread
from time import sleep

class ThreadedTimer:
    
    state: WidgetState
    
    def __init__(self, state: WidgetState):
        self.state = state
        
    def run(self):
        if self.state.active:
            return
        self.state.update_active(True)
        
        thread = Thread(target=self.countdown, daemon=True)
        thread.start()
    
    def countdown(self):
        initial_time = self.state.interval.get() # Time in minutes
        
        # current_time = initial_time * 60 # Time in seconds
        current_time = initial_time # Keeping it as seconds for testing purposes
        
        while current_time > 0 and self.state.active:
            sleep(1)
            
            if self.state.locked_in.get() and self.state.lock_in_cooldown.get() > 0:
                print("Updating lock in cooldown")
                self.state.lock_in_cooldown.set(self.state.lock_in_cooldown.get() - 1)
                continue
            
            if self.state.locked_in.get() and self.state.lock_in_cooldown.get() == 0:
                self.state.update_locked_in(False)
            
            current_time -= 1
            self.state.update_remaining_time(current_time)
            
        if not self.state.active:
            self.reset()
        else:
            self.state.update_active(False)
            self.state.notify.set(True)
    
    def stop(self):
        self.state.update_active(False)
        self.reset()
    
    def reset(self):
        self.state.update_remaining_time(self.state.interval.get() * 60)
        