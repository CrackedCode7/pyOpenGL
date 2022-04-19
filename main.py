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
import Line
import TexturedObject
import Character

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    
    # -------------------------------------------------------------------------
    # Window setup / callback functions
    # -------------------------------------------------------------------------
    
    window = window_setup.setup()
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glEnable(gl.GL_CULL_FACE)

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
    
    renderer = Renderer.Renderer()
    
    letter = Character.Character(-1, 1, 1, 1, "G", color=[0, 1, 0])
    renderer.add_vertex_buffer_data(letter.vertices)
    renderer.add_texture_buffer_data(letter.texture_coords)
    renderer.add_color_buffer_data(letter.colors)
    
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

        frame_counter.update(window)
    
    glfw.terminate()

# -----------------------------------------------------------------------------
# Prevent code from running on import
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()