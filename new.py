from ursina import *
from random import randint
from Main import create_Boids, create_Wireframe
class Boid(Entity):
    def __init__(self, posX, posY, posZ, dirX, dirY, dirZ):
        super().__init__(model = "sprites.blend", position = (posX,posY, posZ), rotation = (dirX, dirY, dirZ), scale = .5, color = color.random_color())
    def update(self):
        self.position += self.forward*time.dt
        if self.x <= -50:
            self.directionX = -self.directionX
        if self.x >= 50:
            self.directionX = -self.directionX
        if self.y <= -50:
            self.directionY = -self.directionY
        if self.y >= 50:
            self.directionY = -self.directionY
        if self.z <= -50:
            self.directionZ = -self.directionZ
        if self.z >= 50:
            self.directionZ = -self.directionZ

app = Ursina()
create_Wireframe()
create_Boids(anzahl = 50)
camera.position = (0,10,-350)
camera.rotation_x = 30
EditorCamera()
app.run()