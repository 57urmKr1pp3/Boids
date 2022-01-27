from ursina import *

def input(keys):
    if held_keys["a"]:
        #e.world_rotation_z -= time.dt * 100
        e.world_rotation_z = -45
    if held_keys["d"]:
        #e.world_rotation_z += time.dt * 100
        e.world_rotation_z = 45
    if held_keys["w"]:
        #e.world_rotation_x += time.dt * 100
        e.world_rotation_x = 45
    if held_keys["s"]:
        #e.world_rotation_x -= time.dt * 100
        e.world_rotation_x = -45
    if held_keys["e"]:
        #e.world_rotation_y += time.dt * 100
        e.world_rotation_y = 45
    if held_keys["q"]:
        #e.world_rotation_y -= time.dt * 100
        e.world_rotation_y = -45
    if held_keys["f"]:
        e.world_rotation = (0,0,0)
    if held_keys["g"]:
        e.world_rotation = (e.world_rotation *(-1))
app = Ursina()
e = Entity(model = 'sprites', position = (0,0,0), color = color.red)
EditorCamera()
app.run()