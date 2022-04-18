from OpenGL import GL as gl
import numpy as np


# Usage: Create object, add vertex and color buffer data from other objects, render.
# Binding of VAO and VBOs has been adding to each function as needed, so no calls
# to bind buffers are needed in the main program.
class Renderer:
    
    def __init__(self):
        
        self.vertices = []
        self.vertex_buffer_size = 0
        self.vertex_buffer_used_size = 0
        self.tex_coords = []
        self.texture_buffer_size = 0
        self.texture_buffer_used_size = 0
        self.colors = []
        self.color_buffer_size = 0
        self.color_buffer_used_size = 0
        
        self.vao = gl.glGenVertexArrays(1)
        self.vertex_vbo = gl.glGenBuffers(1)
        self.texture_vbo = gl.glGenBuffers(1)
        self.color_vbo = gl.glGenBuffers(1)
    
    def bind_vao(self): 
        gl.glBindVertexArray(self.vao)
    
    def bind_vertex_vbo(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_vbo)
    
    def set_vertex_vbo_buffer_size(self, size):

        self.vertex_buffer_size = size

        self.bind_vao()
        self.bind_vertex_vbo()

        gl.glBufferData(
            gl.GL_ARRAY_BUFFER, 
            self.vertex_buffer_size, 
            None, 
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
    
    def bind_texture_vbo(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.texture_vbo)
    
    def set_texture_vbo_buffer_size(self, size):
    
        self.texture_buffer_size = size
        
        self.bind_vao()
        self.bind_texture_vbo()
        
        gl.glBufferData(
            gl.GL_ARRAY_BUFFER, 
            self.texture_buffer_size, 
            None, 
            gl.GL_STATIC_DRAW
        )
        gl.glVertexAttribPointer(
            1,
            2,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(1)
    
    def bind_color_vbo(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.color_vbo)
    
    def set_color_vbo_buffer_size(self, size):

        self.color_buffer_size = size

        self.bind_vao()
        self.bind_color_vbo()

        gl.glBufferData(
            gl.GL_ARRAY_BUFFER, 
            self.color_buffer_size, 
            None, 
            gl.GL_STATIC_DRAW
        )
        gl.glVertexAttribPointer(
            2,
            3,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(2)
    
    def render(self):

        self.bind_vao()
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, int(len(self.vertices)/3))

    def add_vertex_buffer_data(self, vertices, existing_data=False):
        
        self.bind_vao()
        self.bind_vertex_vbo()
        
        if not existing_data:
            self.update_buffer_size("vertex", self.vertex_buffer_size, self.vertex_buffer_used_size, len(vertices)*4)
            self.vertices += vertices

            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                self.vertex_buffer_used_size,
                len(vertices)*4,
                np.array(vertices, dtype=np.float32)
            )
            self.vertex_buffer_used_size += len(vertices)*4
        
        else:
            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                0,
                len(vertices)*4,
                np.array(vertices, dtype=np.float32)
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

    def add_texture_buffer_data(self, tex_coords, existing_data=False):
        
        self.bind_vao()
        self.bind_texture_vbo()
        
        if not existing_data:
            self.update_buffer_size("tex_coords", self.texture_buffer_size, self.texture_buffer_used_size, len(tex_coords)*4)
            self.tex_coords += tex_coords

            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                self.texture_buffer_used_size,
                len(tex_coords)*4,
                np.array(tex_coords, dtype=np.float32)
            )
            self.texture_buffer_used_size += len(tex_coords)*4
        
        else:
            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                0,
                len(tex_coords)*4,
                np.array(tex_coords, dtype=np.float32)
            )
        
        gl.glVertexAttribPointer(
            1,
            2,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(1)

    def add_color_buffer_data(self, colors, existing_data=False):
        
        self.bind_vao()
        self.bind_color_vbo()
        
        if not existing_data:
            self.update_buffer_size("color", self.color_buffer_size, self.color_buffer_used_size, len(colors)*4)
            self.colors += colors

            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                self.color_buffer_used_size,
                len(colors)*4,
                np.array(colors, dtype=np.float32)
            )
            self.color_buffer_used_size += len(colors)*4
        
        else:
            gl.glBufferSubData(
                gl.GL_ARRAY_BUFFER,
                0,
                len(colors)*4,
                np.array(colors, dtype=np.float32)
            )

        gl.glVertexAttribPointer(
            2,
            3,
            gl.GL_FLOAT,
            False,
            0,
            None
        )
        gl.glEnableVertexAttribArray(2)

    def update_buffer_size(self, buffer_type, current_size, used_size, size_to_be_added):
        
        # If we re-size the buffer, the existing data is copied back into the buffer
        
        if (used_size + size_to_be_added >= 2*current_size):
            if buffer_type == "vertex":
                self.vertex_buffer_size += size_to_be_added
                self.set_vertex_vbo_buffer_size(self.vertex_buffer_size)
                self.add_vertex_buffer_data(self.vertices, existing_data=True)
            elif buffer_type == "color":
                self.color_buffer_size += size_to_be_added
                self.set_color_vbo_buffer_size(self.color_buffer_size)
                self.add_color_buffer_data(self.colors, existing_data=True)
            else:
                self.texture_buffer_size += size_to_be_added
                self.set_texture_vbo_buffer_size(self.texture_buffer_size)
                self.add_texture_buffer_data(self.tex_coords, existing_data=True)
        
        elif (used_size + size_to_be_added > current_size):
            if buffer_type == "vertex":
                self.vertex_buffer_size *= 2
                self.set_vertex_vbo_buffer_size(self.vertex_buffer_size)
                self.add_vertex_buffer_data(self.vertices, existing_data=True)
            elif buffer_type == "color":
                self.color_buffer_size *= 2
                self.set_color_vbo_buffer_size(self.color_buffer_size)
                self.add_color_buffer_data(self.colors, existing_data=True)
            else:
                self.texture_buffer_size *= 2
                self.set_texture_vbo_buffer_size(self.texture_buffer_size)
                self.add_texture_buffer_data(self.tex_coords, existing_data=True)