from OpenGL import GL as gl
import glfw
import time

import window_setup
import framerate_counter


def main():
    
    frame_counter = framerate_counter.FrameCounter()

    window = window_setup.setup()
    
    while not glfw.window_should_close(window):
    
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()
        
        frame_counter.update()


if __name__ == "__main__":
    main()