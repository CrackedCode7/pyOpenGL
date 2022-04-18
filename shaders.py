import OpenGL.GL.shaders as gl_shaders
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER
from OpenGL import GL as gl


vertex_shader_source = """
#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

void main()
{
	gl_Position = vec4(aPos, 1.0f);
    TexCoord = aTexCoord;
}

"""

fragment_shader_source = """
#version 330 core

in vec2 TexCoord;

out vec4 FragColor;

uniform sampler2D ourTexture;
uniform vec2 textureSize;

void main()
{
	FragColor = texture(ourTexture, TexCoord/textureSize);
}
"""


def compile_vertex_shader(vertex_shader_source):
    return gl_shaders.compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    
def compile_fragment_shader(fragment_shader_source):
    return gl_shaders.compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    
def compile_shader_program(vertex_shader_source, fragment_shader_source):
    return gl_shaders.compileProgram(compile_vertex_shader(vertex_shader_source), compile_fragment_shader(fragment_shader_source))
    
    
class Shader:
    
    def __init__(self, vertex_shader_source, fragment_shader_source):
        
        self.id = compile_shader_program(vertex_shader_source, fragment_shader_source)
    
    def use(self):
        gl.glUseProgram(self.id)
    
    def set_vec2(self, name, value):
        gl.glUniform2fv(gl.glGetUniformLocation(self.id, name), 1, value)