from typing import Text
from bpy.props import (StringProperty, BoolProperty,
                       IntProperty, FloatProperty, EnumProperty)

from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

class RenderFamClient(Panel):
    bl_idname = "global-parent-panel"
    bl_label = "RenderFam"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self, context):
        layout = self.layout
        layout = layout.label(text="RenderFam")

SEARCH_QUERY: StringProperty(
    name="search",
    description="Search Query",
    default="",     
    maxlen=70,
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



