from OpenGL import GL as gl
import glfw


window_size = [200, 200]


def framebuffer_size_callback(window, width, height):

    global window_size
    window_size = [width, height]
    
    gl.glViewport(0, 0, width, height)


def setup():

    if not glfw.init():
        print("Failed to initialize glfw")
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    
    window = glfw.create_window(window_size[0], window_size[1], "FPS", None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(0)
    gl.glClearColor(0, 0, 0, 0)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback);
    
    return window