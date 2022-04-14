import pixels_to_screen_coords
import window_setup

class Button:

    def __init__(self, pos_x, pos_y, size_x, size_y):
        
        self.x_min = pos_x
        self.x_max = pos_x + size_x
        self.y_min = pos_y - size_y
        self.y_max = pos_y
        
        self.set_vertices()
    
    def set_vertices(self):
        
        self.vertices = [self.x_min, self.y_max, 0,
                         self.x_min, self.y_min, 0,
                         self.x_max, self.y_max, 0,
                         
                         self.x_min, self.y_min, 0,
                         self.x_max, self.y_min, 0,
                         self.x_max, self.y_max, 0]
    
    def check_intersection(self, point):
        
        point_coords = pixels_to_screen_coords.pixels_to_screen_coords(
            point[0],
            point[1],
            window_setup.window_size[0],
            window_setup.window_size[1]
            )

        if ((point_coords[0] > self.x_min and point_coords[0] < self.x_max) and
            (point_coords[1] > self.y_min and point_coords[1] < self.y_max)):
           
            print("INSIDE BUTTON")