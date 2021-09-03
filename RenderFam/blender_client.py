from bpy.props import (StringProperty, BoolProperty,
                       IntProperty, FloatProperty, EnumProperty, PointerProperty)

from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       Scene
                       )




scene = Scene



class MyProperties(PropertyGroup):

    bl_idname = "options.render_fam"
    bl_label = "Options"

    SEARCH_QUERY: StringProperty(
        name="",
        description="Search Query",
        default="",
        maxlen=20,
        
    )

    SEARCH_LAN: BoolProperty(
        name="LAN",
        description="Include LAN-connected clients in search",
        default=True
    )

    SEARCH_INTERNET: BoolProperty(
        name="Internet",
        description="Include clients connected via internet in search",
        default=True

    )
    IMPORT_PATH: StringProperty(
        name="Directory",
        description="Choose a directory",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
        # icon = ZOOM_SELECTED
    )




class RenderFamClient(Panel):
    bl_idname = "global-parent-panel"
    bl_category= "RenderFam"
    bl_label = "RenderFam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        mytool = context.scene.my_tool
        col.prop(mytool, 'SEARCH_QUERY', icon='VIEWZOOM')
        col.prop(mytool, 'SEARCH_LAN')
        col.separator(factor=10)
        col.prop(mytool, 'IMPORT_PATH')
        
        layout.use_property_split = True  # Active single-column layout
        
