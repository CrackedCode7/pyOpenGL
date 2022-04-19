import pixels_to_screen_coords
import window_setup
import numpy as np

class Line:
    
    def __init__(self, start_coords, end_coords, line_width, pixel_coords=False, color=[1, 1, 1]):
        
        if pixel_coords:
            self.start_coords = pixels_to_screen_coords.pixels_to_screen_coords(
                start_coords[0],
                start_coords[1],
                window_setup.window_size[0],
                window_setup.window_size[1]
                )
            self.end_coords = pixels_to_screen_coords.pixels_to_screen_coords(
                end_coords[0],
                end_coords[1],
                window_setup.window_size[0],
                window_setup.window_size[1]
                )
        else:
            self.start_coords = start_coords
            self.end_coords = end_coords
        
        self.line_width = line_width
        self.color = color
        
        self.calculate_direction()
        self.set_vertices()
        self.set_texture_coords()
        self.set_colors(self.color)
    
    def set_vertices(self):
        
        self.vertices = [self.start_coords[0]-self.perpendicular_vector[0],
                         self.start_coords[1]-self.perpendicular_vector[1],
                         0,
                         
                         self.end_coords[0]-self.perpendicular_vector[0],
                         self.end_coords[1]-self.perpendicular_vector[1],
                         0,
                         
                         self.end_coords[0]+self.perpendicular_vector[0],
                         self.end_coords[1]+self.perpendicular_vector[1],
                         0,
                         
                         self.start_coords[0]-self.perpendicular_vector[0],
                         self.start_coords[1]-self.perpendicular_vector[1],
                         0,
                         
                         self.end_coords[0]+self.perpendicular_vector[0],
                         self.end_coords[1]+self.perpendicular_vector[1],
                         0,
                         
                         self.start_coords[0]+self.perpendicular_vector[0],
                         self.start_coords[1]+self.perpendicular_vector[1],
                         0]
    
    def set_texture_coords(self):

        self.texture_coords = [0, 0,
                               0, 0,
                               0, 0,
                               
                               0, 0,
                               0, 0,
                               0, 0]
    
    def set_colors(self, color):
        
        self.colors = [color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       
                       color[0], color[1], color[2],
                       color[0], color[1], color[2],
                       color[0], color[1], color[2]]
    
    def calculate_direction(self):
        
        self.direction_vector = [self.end_coords[0]-self.start_coords[0],
                                 self.end_coords[1]-self.start_coords[1]]
        self.direction_vector /= np.linalg.norm(self.direction_vector)
        
        self.perpendicular_vector = np.array([-self.direction_vector[1], self.direction_vector[0]])
        self.perpendicular_vector *= (self.line_width/window_setup.window_size[0]/np.linalg.norm(self.perpendicular_vector))