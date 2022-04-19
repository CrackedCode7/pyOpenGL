import pixels_to_screen_coords
import window_setup

class TexturedObject:

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
        
        self.x_min = pos_x
        self.x_max = pos_x + size_x
        self.y_min = pos_y - size_y
        self.y_max = pos_y
        
        self.set_vertices()
        self.set_texture_coords(
            texture_start_x,
            texture_start_y,
            texture_size_x, 
            texture_size_y
            )
        self.set_colors(color)
    
    def set_vertices(self):
        
        self.vertices = [self.x_min, self.y_max, 0,
                         self.x_min, self.y_min, 0,
                         self.x_max, self.y_max, 0,
                         
                         self.x_min, self.y_min, 0,
                         self.x_max, self.y_min, 0,
                         self.x_max, self.y_max, 0]
    
    def set_texture_coords(
        self,
        texture_start_x,
        texture_start_y,
        texture_size_x, 
        texture_size_y
        ):

        self.texture_coords = [
            texture_start_x, texture_start_y,
            texture_start_x, texture_start_y-texture_size_y,
            texture_start_x+texture_size_x, texture_start_y,
           
            texture_start_x, texture_start_y-texture_size_y,
            texture_start_x+texture_size_x, texture_start_y-texture_size_y,
            texture_start_x+texture_size_x, texture_start_y
            ]
    
    def set_colors(self, color):
        
        self.colors = [color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       
                       color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       color[0], color[1], color[2]] 