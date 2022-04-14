import glfw

mouse_button_was_pressed = False
mouse_pressed_location = None

def mouse_button_callback(window, button, action, mod):
    
    global mouse_button_was_pressed
    global mouse_pressed_location
    
    if (button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS):
        
        mouse_button_was_pressed = True
        mouse_pressed_location = glfw.get_cursor_pos(window)