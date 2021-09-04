from os import name
from bpy.props import (StringProperty, BoolProperty,
                       IntProperty, FloatProperty, EnumProperty, PointerProperty)

from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       Scene,
                       UIList
                       )





class ListItem(PropertyGroup):
    """Group of properties representing an item in the list."""

    name: StringProperty(
        name="Name",
        description="A name for this item",
        default="Untitled")

    random_prop: StringProperty(
        name="Any other property you want",
        description="",
        default="")


class ROperators(Operator):

    bl_idname = "operators.render_fam"
    bl_label = ""


class MY_UL_List(UIList):
   

    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):

        # We could write some code to decide which icon to use here...
        custom_icon = 'WORLD '

        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon=custom_icon)

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon=custom_icon)


class LIST_OT_NewItem(Operator):
    """Add a new item to the list."""

    bl_idname = "peer_list.new_item"
    bl_label = "Add a new item"

    def execute(self, context):
        context.scene.peer_list.add()

        return{'FINISHED'}


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
        name="Cloud",
        description="Include clients connected via internet in search",
        default=True

    )
    IMPORT_PATH: StringProperty(
        name="Attach file",
        description="Choose a directory",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        # icon = ZOOM_SELECTED
    )


class RenderFamClient(Panel):
    bl_idname = "global-parent-panel"
    bl_category = "RenderFam"
    bl_label = "RenderFam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        mytool = context.scene.ui_properties
        list_index = 'list_index'
        row.prop(mytool, 'SEARCH_QUERY', icon='VIEWZOOM')
        row = layout.row(align=True)
        row.prop(mytool, 'SEARCH_LAN')

        row.prop(mytool, 'SEARCH_INTERNET')
        row = layout.row()
        col = row.column(align=True)
        col.separator(factor=2)

        col.prop(mytool, 'IMPORT_PATH')
        row = layout.row()
        row.template_list("MY_UL_List", "The_List", context.scene,
                          "peer_list", context.scene, list_index)
        row.operator("peer_list.new_item", icon='VIEWZOOM', text="")
