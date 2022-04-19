import pixels_to_screen_coords
import window_setup
from TexturedObject import TexturedObject

class Button(TexturedObject):

    def __init__(self,
                 pos_x, 
                 pos_y, 
                 size_x, 
                 size_y,
                 texture_start_x,
                 texture_start_y,
                 texture_size_x,
                 texture_size_y,
                 color=[1, 1, 1]):
        
        super().__init__(pos_x, 
                         pos_y, 
                         size_x, 
                         size_y,
                         texture_start_x,
                         texture_start_y,
                         texture_size_x,
                         texture_size_y,
                         color)
        
    def check_intersection(self, point):
        
        point_coords = pixels_to_screen_coords.pixels_to_screen_coords(
            point[0],
            point[1],
            window_setup.window_size[0],
            window_setup.window_size[1]
            )

        if ((point_coords[0] > self.x_min and point_coords[0] < self.x_max) and
            (point_coords[1] > self.y_min and point_coords[1] < self.y_max)):
           
            self.action()
    
    def action(self):
        print("BUTTON PRESSED")