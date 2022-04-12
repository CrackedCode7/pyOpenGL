import time


class FrameCounter:
    
    def __init__(self):
        
        self.prev_time = time.time()
        self.current_time = time.time()
        self.frames = 0
    
    def update(self):
        
        self.current_time = time.time()
        if (self.current_time - self.prev_time >= 1):
            self.frames = 0
            self.prev_time = self.current_time
        else:
            self.frames += 1
    
    def print_framerate(self):
        print("FPS:", self.frames)