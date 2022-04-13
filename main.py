# -----------------------------------------------------------------------------
# Package imports
# -----------------------------------------------------------------------------

from OpenGL import GL as gl
import glfw
import numpy as np

# -----------------------------------------------------------------------------
# Local imports
# -----------------------------------------------------------------------------

import window_setup
import framerate_counter
import shaders

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    
    # -------------------------------------------------------------------------
    # Window setup
    # -------------------------------------------------------------------------
    
    window = window_setup.setup()
    gl.glEnable(gl.GL_DEPTH_TEST)
    
    # -------------------------------------------------------------------------
    # Frame counter
    # -------------------------------------------------------------------------
    
    frame_counter = framerate_counter.FrameCounter()
    
    # -------------------------------------------------------------------------
    # Shader setup/activation
    # -------------------------------------------------------------------------
    
    shader_program = shaders.compile_shader_program()
    gl.glUseProgram(shader_program)
    result = gl.glGetProgramiv(shader_program, gl.GL_LINK_STATUS)
    print(result)
    
    # -------------------------------------------------------------------------
    # Buffer Objects setup
    # -------------------------------------------------------------------------
    
    triangle = np.array([-0.5, -0.5, 0,
                         0.5, -0.5, 0,
                         0, 0.5, 0
                        ], 
                        dtype=np.float32
                        )
    
    vao = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(vao)
    
    vbo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo)
    gl.glBufferData(
        gl.GL_ARRAY_BUFFER, 
        len(triangle)*4, 
        triangle, 
        gl.GL_STATIC_DRAW
    )
    gl.glVertexAttribPointer(
        0,              # Attribute location
        3,              # Number of elements in attribute (number of verts, etc.)
        gl.GL_FLOAT,    # Data type
        False,          # Normalize?
        0,              # Stride
        None            # Offset pointer
    )
    gl.glEnableVertexAttribArray(0)
    
    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    
    while not glfw.window_should_close(window):
    
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Draw
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
        
        glfw.swap_buffers(window)
        glfw.poll_events()

        frame_counter.update()
    
    glfw.terminate()

# -----------------------------------------------------------------------------
# Prevent code from running on import
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()