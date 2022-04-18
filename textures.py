from PIL import Image
from OpenGL import GL as gl
import numpy as np

#print(img.format, img.mode)


class Texture:
    
    def __init__(self, filename):
        
        self.img = Image.open(filename)
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        self.width = self.img.width
        self.height = self.img.height
        self.data = np.array(list(self.img.getdata()), np.int8)
        
        self.texture = gl.glGenTextures(1)
        self.bind()
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, self.width, self.height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, self.data)
        gl.glGenerateMipmap(gl.GL_TEXTURE_2D)
    
    def bind(self):
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)