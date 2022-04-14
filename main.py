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
import Button
import pixels_to_screen_coords
import callbacks

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    
    # -------------------------------------------------------------------------
    # Window setup / callback functions
    # -------------------------------------------------------------------------
    
    window = window_setup.setup()
    gl.glEnable(gl.GL_DEPTH_TEST)

    glfw.set_mouse_button_callback(window, callbacks.mouse_button_callback)
    
    # -------------------------------------------------------------------------
    # Frame counter
    # -------------------------------------------------------------------------
    
    frame_counter = framerate_counter.FrameCounter()
    
    # -------------------------------------------------------------------------
    # Shader setup/activation
    # -------------------------------------------------------------------------
    
    shader_program = shaders.compile_shader_program()
    gl.glUseProgram(shader_program)
    
    # -------------------------------------------------------------------------
    # Buffer Objects setup
    # -------------------------------------------------------------------------
    
    button = Button.Button(-1, 1, 1, 1)
    
    vao = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(vao)
    
    vbo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo)
    gl.glBufferData(
        gl.GL_ARRAY_BUFFER, 
        len(button.vertices)*4, 
        np.array(button.vertices, dtype=np.float32), 
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
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, int(len(button.vertices)/3))
        
        glfw.swap_buffers(window)
        glfw.poll_events()
        
        if (callbacks.mouse_button_was_pressed is True):
        
            callbacks.mouse_button_was_pressed = False
            button.check_intersection(callbacks.mouse_pressed_location)

        frame_counter.update(window)
    
    glfw.terminate()

# -----------------------------------------------------------------------------
# Prevent code from running on import
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()