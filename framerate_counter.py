import time
import glfw


class FrameCounter:
    
    def __init__(self):
        
        self.prev_time = time.time()
        self.current_time = time.time()
        self.frames = 0
    
    def update(self, window):
        
        self.current_time = time.time()
        if (self.current_time - self.prev_time >= 1):
            self.update_framerate(window)
            self.frames = 0
            self.prev_time = self.current_time
        else:
            self.frames += 1
    
    def update_framerate(self, window):
        glfw.set_window_title(window, str(self.frames))