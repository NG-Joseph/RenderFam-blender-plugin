import sys
import typing
import bpy.types
import mathutils


class Buffer:
    ''' For Python access to GPU functions requiring a pointer. :arg format: Format type to interpret the buffer. Possible values are FLOAT , INT , UINT , UBYTE , UINT_24_8 and 10_11_11_REV . :type type: str :arg dimensions: Array describing the dimensions. :type dimensions: int :arg data: Optional data array. :type data: sequence return the buffer as a list
    '''

    dimensions = None
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.'''


class GPUBatch:
    ''' Reusable container for drawable geometry. :arg type: The primitive type of geometry to be drawn. Possible values are POINTS , LINES , TRIS , LINE_STRIP , LINE_LOOP , TRI_STRIP , TRI_FAN , LINES_ADJ , TRIS_ADJ and LINE_STRIP_ADJ . :type type: str :arg buf: Vertex buffer containing all or some of the attributes required for drawing. :type buf: gpu.types.GPUVertBuf :arg elem: An optional index buffer. :type elem: gpu.types.GPUIndexBuf
    '''

    def draw(self, program: 'GPUShader' = None):
        ''' Run the drawing program with the parameters assigned to the batch.

        :param program: Program that performs the drawing operations. If None is passed, the last program set to this batch will run.
        :type program: 'GPUShader'
        '''
        pass

    def program_set(self, program: 'GPUShader'):
        ''' Assign a shader to this batch that will be used for drawing when not overwritten later. Note: This method has to be called in the draw context that the batch will be drawn in. This function does not need to be called when you always set the shader when calling :meth: gpu.types.GPUBatch.draw .

        :param program: The program/shader the batch will use in future draw calls.
        :type program: 'GPUShader'
        '''
        pass

    def vertbuf_add(self, buf: 'GPUVertBuf'):
        ''' Add another vertex buffer to the Batch. It is not possible to add more vertices to the batch using this method. Instead it can be used to add more attributes to the existing vertices. A good use case would be when you have a separate vertex buffer for vertex positions and vertex normals. Current a batch can have at most 6 vertex buffers.

        :param buf: The vertex buffer that will be added to the batch.
        :type buf: 'GPUVertBuf'
        '''
        pass


class GPUFrameBuffer:
    ''' This object gives access to framebuffer functionallities. When a 'layer' is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer. For cube map textures, layer is translated into a cube map face. :arg depth_slot: GPUTexture to attach or a dict containing keywords: 'texture', 'layer' and 'mip'. :type depth_slot: gpu.types.GPUTexture , dict or Nonetype :arg color_slots: Tuple where each item can be a GPUTexture or a dict containing keywords: 'texture', 'layer' and 'mip'. :type color_slots: tuple or Nonetype
    '''

    is_bound = None
    ''' Checks if this is the active framebuffer in the context.'''

    @staticmethod
    def bind():
        ''' Context manager to ensure balanced bind calls, even in the case of an error.

        '''
        pass

    def clear(self,
              color: list = None,
              depth: float = None,
              stencil: int = None):
        ''' Fill color, depth and stencil textures with specific value. Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.

        :param color: float sequence each representing (r, g, b, a) .
        :type color: list
        :param depth: depth value.
        :type depth: float
        :param stencil: stencil value.
        :type stencil: int
        '''
        pass

    @staticmethod
    def viewport_get():
        ''' Returns position and dimension to current viewport.

        '''
        pass

    @staticmethod
    def viewport_set(x: int, y: int, xsize: int, ysize: int):
        ''' Set the viewport for this framebuffer object. Note: The viewport state is not saved upon framebuffer rebind.

        :param x: lower left corner of the viewport_set rectangle, in pixels.
        :type x: int
        :param y: lower left corner of the viewport_set rectangle, in pixels.
        :type y: int
        :param xsize: width and height of the viewport_set.
        :type xsize: int
        :param ysize: width and height of the viewport_set.
        :type ysize: int
        '''
        pass


class GPUIndexBuf:
    ''' Contains an index buffer. :arg type: The primitive type this index buffer is composed of. Possible values are POINTS , LINES , TRIS and LINE_STRIP_ADJ . :type type: str :param seq: Indices this index buffer will contain. Whether a 1D or 2D sequence is required depends on the type. Optionally the sequence can support the buffer protocol. :type seq: 1D or 2D sequence
    '''

    pass


class GPUOffScreen:
    ''' This object gives access to off screen buffers. :arg width: Horizontal dimension of the buffer. :type width: int :arg height: Vertical dimension of the buffer. :type height: int
    '''

    color_texture: int = None
    ''' OpenGL bindcode for the color texture.

    :type: int
    '''

    height: int = None
    ''' Height of the texture.

    :type: int
    '''

    width: int = None
    ''' Width of the texture.

    :type: int
    '''

    @staticmethod
    def bind():
        ''' Context manager to ensure balanced bind calls, even in the case of an error.

        '''
        pass

    def draw_view3d(
            self, scene: 'bpy.types.Scene', view_layer: 'bpy.types.ViewLayer',
            view3d: 'bpy.types.SpaceView3D', region: 'bpy.types.Region',
            view_matrix: 'mathutils.Matrix',
            projection_matrix: 'mathutils.Matrix'):
        ''' Draw the 3d viewport in the offscreen object.

        :param scene: Scene to draw.
        :type scene: 'bpy.types.Scene'
        :param view_layer: View layer to draw.
        :type view_layer: 'bpy.types.ViewLayer'
        :param view3d: 3D View to get the drawing settings from.
        :type view3d: 'bpy.types.SpaceView3D'
        :param region: Region of the 3D View (required as temporary draw target).
        :type region: 'bpy.types.Region'
        :param view_matrix: View Matrix (e.g. camera.matrix_world.inverted() ).
        :type view_matrix: 'mathutils.Matrix'
        :param projection_matrix: Projection Matrix (e.g. camera.calc_matrix_camera(...) ).
        :type projection_matrix: 'mathutils.Matrix'
        '''
        pass

    def free(self):
        ''' Free the offscreen object. The framebuffer, texture and render objects will no longer be accessible.

        '''
        pass

    def unbind(self, restore: bool = True):
        ''' Unbind the offscreen object.

        :param restore: Restore the OpenGL state, can only be used when the state has been saved before.
        :type restore: bool
        '''
        pass


class GPUShader:
    ''' GPUShader combines multiple GLSL shaders into a program used for drawing. It must contain a vertex and fragment shaders, with an optional geometry shader. The GLSL #version directive is automatically included at the top of shaders, and set to 330. Some preprocessor directives are automatically added according to the Operating System or availability: GPU_ATI , GPU_NVIDIA and GPU_INTEL . The following extensions are enabled by default if supported by the GPU: GL_ARB_texture_gather , GL_ARB_texture_cube_map_array and GL_ARB_shader_draw_parameters . For drawing user interface elements and gizmos, use fragOutput = blender_srgb_to_framebuffer_space(fragOutput) to transform the output sRGB colors to the frame-buffer color-space. :param vertexcode: Vertex shader code. :type vertexcode: str :param fragcode: Fragment shader code. :type value: str :param geocode: Geometry shader code. :type value: str :param libcode: Code with functions and presets to be shared between shaders. :type value: str :param defines: Preprocessor directives. :type value: str
    '''

    program: int = None
    ''' The name of the program object for use by the OpenGL API (read-only).

    :type: int
    '''

    def attr_from_name(self, name: str) -> int:
        ''' Get attribute location by name.

        :param name: The name of the attribute variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: The location of an attribute variable.
        '''
        pass

    def bind(self):
        ''' Bind the shader object. Required to be able to change uniforms of this shader.

        '''
        pass

    def calc_format(self) -> 'GPUVertFormat':
        ''' Build a new format based on the attributes of the shader.

        :rtype: 'GPUVertFormat'
        :return: vertex attribute format for the shader
        '''
        pass

    def uniform_block(self, name: str, ubo):
        ''' Specify the value of an uniform buffer object variable for the current GPUShader.

        :param name: name of the uniform variable whose UBO is to be specified.
        :type name: str
        :param texture: 
        :type texture: 'GPUUniformBuf'
        :param ubo: 
        :type ubo: 
        '''
        pass

    def uniform_block_from_name(self, name: str) -> int:
        ''' Get uniform block location by name.

        :param name: Name of the uniform block variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: The location of the uniform block variable.
        '''
        pass

    def uniform_bool(self, name: str, seq: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable.
        :type seq: list
        '''
        pass

    def uniform_float(self, name: str, value: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: Name of the uniform variable whose value is to be changed.
        :type name: str
        :param value: Value that will be used to update the specified uniform variable.
        :type value: list
        '''
        pass

    def uniform_from_name(self, name: str) -> int:
        ''' Get uniform location by name.

        :param name: Name of the uniform variable whose location is to be queried.
        :type name: str
        :rtype: int
        :return: Location of the uniform variable.
        '''
        pass

    def uniform_int(self, name: str, seq: list):
        ''' Specify the value of a uniform variable for the current program object.

        :param name: name of the uniform variable whose value is to be changed.
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable.
        :type seq: list
        '''
        pass

    def uniform_sampler(self, name: str, texture: 'GPUTexture'):
        ''' Specify the value of a texture uniform variable for the current GPUShader.

        :param name: name of the uniform variable whose texture is to be specified.
        :type name: str
        :param texture: Texture to attach.
        :type texture: 'GPUTexture'
        '''
        pass

    def uniform_vector_float(self, location: int, buffer: list, length: int,
                             count: int):
        ''' Set the buffer to fill the uniform.

        :param location: Location of the uniform variable to be modified.
        :type location: int
        :param buffer: The data that should be set. Can support the buffer protocol.
        :type buffer: list
        :param length: - 1: float - 2: vec2 or float[2] - 3: vec3 or float[3] - 4: vec4 or float[4] - 9: mat3 - 16: mat4
        :type length: int
        :param count: Specifies the number of elements, vector or matrices that are to be modified.
        :type count: int
        '''
        pass

    def uniform_vector_int(self, location, buffer, length, count):
        ''' See GPUShader.uniform_vector_float(...) description.

        '''
        pass


class GPUTexture:
    ''' This object gives access to off GPU textures. :arg size: Dimensions of the texture 1D, 2D, 3D or cubemap. :type size: tuple or int :arg layers: Number of layers in texture array or number of cubemaps in cubemap array :type layers: int :arg is_cubemap: Indicates the creation of a cubemap texture. :type is_cubemap: int :arg format: Internal data format inside GPU memory. Possible values are: RGBA8UI , RGBA8I , RGBA8 , RGBA32UI , RGBA32I , RGBA32F , RGBA16UI , RGBA16I , RGBA16F , RGBA16 , RG8UI , RG8I , RG8 , RG32UI , RG32I , RG32F , RG16UI , RG16I , RG16F , RG16 , R8UI , R8I , R8 , R32UI , R32I , R32F , R16UI , R16I , R16F , R16 , R11F_G11F_B10F , DEPTH32F_STENCIL8 , DEPTH24_STENCIL8 , SRGB8_A8 , RGB16F , SRGB8_A8_DXT1 , SRGB8_A8_DXT3 , SRGB8_A8_DXT5 , RGBA8_DXT1 , RGBA8_DXT3 , RGBA8_DXT5 , DEPTH_COMPONENT32F , DEPTH_COMPONENT24 , DEPTH_COMPONENT16 , :type format: str :arg data: Buffer object to fill the texture. :type data: gpu.types.Buffer
    '''

    format: str = None
    ''' Format of the texture.

    :type: str
    '''

    height: int = None
    ''' Height of the texture.

    :type: int
    '''

    width: int = None
    ''' Width of the texture.

    :type: int
    '''

    def clear(self, format='FLOAT', value: list = (0.0, 0.0, 0.0, 1.0)):
        ''' Fill texture with specific value.

        :param type: 
        :type type: str
        :param value: sequence each representing the value to fill.
        :type value: list
        :param format: 
        :type format: 
        '''
        pass

    def read(self):
        ''' Creates a buffer with the value of all pixels.

        '''
        pass


class GPUUniformBuf:
    ''' This object gives access to off uniform buffers. :arg data: Buffer object. :type data: gpu.types.Buffer
    '''

    def update(self, data):
        ''' Update the data of the uniform buffer object.

        '''
        pass


class GPUVertBuf:
    ''' Contains a VBO. :param len: Amount of vertices that will fit into this buffer. :type type: int :param format: Vertex format. :type buf: gpu.types.GPUVertFormat
    '''

    def attr_fill(self, id: typing.Union[str, int], data: list):
        ''' Insert data into the buffer for a single attribute.

        :param id: Either the name or the id of the attribute.
        :type id: typing.Union[str, int]
        :param data: Sequence of data that should be stored in the buffer
        :type data: list
        '''
        pass


class GPUVertFormat:
    ''' This object contains information about the structure of a vertex buffer.
    '''

    def attr_add(self, id: str, comp_type: str, len: int, fetch_mode: str):
        ''' Add a new attribute to the format.

        :param id: Name the attribute. Often position , normal , ...
        :type id: str
        :param comp_type: The data type that will be used store the value in memory. Possible values are I8 , U8 , I16 , U16 , I32 , U32 , F32 and I10 .
        :type comp_type: str
        :param len: How many individual values the attribute consists of (e.g. 2 for uv coordinates).
        :type len: int
        :param fetch_mode: How values from memory will be converted when used in the shader. This is mainly useful for memory optimizations when you want to store values with reduced precision. E.g. you can store a float in only 1 byte but it will be converted to a normal 4 byte float when used. Possible values are FLOAT , INT , INT_TO_FLOAT_UNIT and INT_TO_FLOAT .
        :type fetch_mode: str
        '''
        pass
