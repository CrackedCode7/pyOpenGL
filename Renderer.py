from OpenGL import GL as gl
import numpy as np


class Renderer:
    
    def __init__(self):
        
        self.vertices = []
        self.colors = []
        
        self.vao = gl.glGenVertexArrays(1)
        self.vertex_vbo = gl.glGenBuffers(1)
        self.color_vbo = gl.glGenBuffers(1)
    
    def bind_vao(self): 
        gl.glBindVertexArray(self.vao)
    
    def bind_vertex_vbo(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_vbo)
    
    def set_vertex_vbo_buffer_data(self):
    
        gl.glBufferData(
            gl.GL_ARRAY_BUFFER, 
            len(self.vertices)*4, 
            np.array(self.vertices, dtype=np.float32), 
            gl.GL_STATIC_DRAW
        )
        gl.glVertexAttribPointer(
            0,
            3,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(0)
    
    def bind_color_vbo(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.color_vbo)
    
    def set_color_vbo_buffer_data(self):
    
        gl.glBufferData(
            gl.GL_ARRAY_BUFFER, 
            len(self.colors)*4, 
            np.array(self.colors, dtype=np.float32), 
            gl.GL_STATIC_DRAW
        )
        gl.glVertexAttribPointer(
            1,
            3,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(1)
    
    def add_vertices(self, vertices):
        self.vertices += vertices
    
    def add_colors(self, colors):
        self.colors += colors