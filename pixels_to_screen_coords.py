def pixels_to_screen_coords(pixel_x, pixel_y, screen_pixel_width, screen_pixel_height):
    
    # Assumed pixel 0,0 is bottom left corner
    
    if (pixel_x <= 0):
        screen_x = -1
    elif (pixel_x >= screen_pixel_width):
        screen_x = 1
    else:
        screen_x = pixel_x / screen_pixel_width * (1 - (-1)) + (-1)

    if (pixel_y <= 0):
        screen_y = -1
    elif (pixel_y >= screen_pixel_height):
        screen_y = 1
    else:
        screen_y = pixel_y / screen_pixel_height * (-1 - 1) + 1
    
    return screen_x, screen_y