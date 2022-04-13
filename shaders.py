import OpenGL.GL.shaders as gl_shaders
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER


vertex_shader_source = """
#version 330 core

layout (location = 0) in vec3 aPos;

void main()
{
	gl_Position = vec4(aPos, 1.0f);
}

"""


fragment_shader_source = """
#version 330 core
out vec4 FragColor;

void main()
{
	FragColor = vec4( 1.0f, 0.0f, 0.0f, 1.0f );
}
"""


def compile_vertex_shader():
    return gl_shaders.compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    
def compile_fragment_shader():
    return gl_shaders.compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    
def compile_shader_program():
    return gl_shaders.compileProgram(compile_vertex_shader(), compile_fragment_shader())