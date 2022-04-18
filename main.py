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
import callbacks
import Renderer
import textures

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
    
    shader = shaders.Shader(shaders.vertex_shader_source, 
                            shaders.fragment_shader_source)
    shader.use()
    
    # -------------------------------------------------------------------------
    # Texture setup
    # -------------------------------------------------------------------------
    
    texture = textures.Texture("textures.png")
    shader.set_vec2("textureSize", [texture.width, texture.height])
    
    # -------------------------------------------------------------------------
    # Buffer Objects setup
    # -------------------------------------------------------------------------
    
    button = Button.Button(-1, 1, 1, 1)
    button1 = Button.Button(0, 0, 1, 1)

    renderer = Renderer.Renderer()
    renderer.add_vertex_buffer_data(button.vertices)
    renderer.add_texture_buffer_data(button.texture_coords)
    renderer.add_vertex_buffer_data(button1.vertices)
    renderer.add_texture_buffer_data(button1.texture_coords)
    
    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    
    while not glfw.window_should_close(window):
        
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Draw
        renderer.render()
        
        glfw.swap_buffers(window)
        glfw.poll_events()
        
        if (callbacks.mouse_button_was_pressed is True):
        
            callbacks.mouse_button_was_pressed = False
            button.check_intersection(callbacks.mouse_pressed_location)
            button1.check_intersection(callbacks.mouse_pressed_location)

        frame_counter.update(window)
    
    glfw.terminate()

# -----------------------------------------------------------------------------
# Prevent code from running on import
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()