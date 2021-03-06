import bpy
import mathutils

from bpy.props import FloatVectorProperty
from bpy.types import Node
from .._base.node_base import ScNode

class ScCellVector(Node, ScNode):
    bl_idname = "ScCellVector"
    bl_label = "Cell (Vector)"

    in_position: FloatVectorProperty(update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketVector", "Position").init("in_position", True)
        self.outputs.new("ScNodeSocketVector", "Value")
    
    def post_execute(self):
        out = {}
        out["Value"] = mathutils.noise.cell_vector(self.inputs["Position"].default_value)
        return out