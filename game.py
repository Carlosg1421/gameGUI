from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel(Button):
    def __init__ (self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_Y=0.5,
            texture='grass',
            color=color.rgb(255,255,255),
            highlight_color=color.lime,
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position= self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)
ChunkSize = 16

for z in range(ChunkSize):
    for x in range(ChunkSize):
        voxel = Voxel(position=(x,0,z))
        
player = FirstPersonController(position=(8,1,8),speed=6)
app.run()
