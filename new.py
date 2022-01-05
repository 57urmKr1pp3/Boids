from ursina import *
from random import randint
from Main import create_Wireframe

def create_Boids(anzahl, liste):
    #Erstellen und speichern der Boids in einer Liste
    for i in range(anzahl):
        temp = Boid(i, randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20))
        Liste_Boids.append(temp)
class Boid(Entity):
    def __init__(self, posX, posY, posZ, dirForward, rotX, rotY, rotZ):
        super().__init__(model = "sprites.blend", position = (posX,posY, posZ), rotation = (rotX, rotY, rotZ), scale = .5, color = color.random_color())
        self.dirforward = dirForward
        
    def update(self):
        self.position += self.forward*self.dirforward*time.dt
        # if self.x <= -50:
        #     self.directionX = -self.directionX
        # if self.x >= 50:
        #     self.directionX = -self.directionX
        # if self.y <= -50:
        #     self.directionY = -self.directionY
        # if self.y >= 50:
        #     self.directionY = -self.directionY
        # if self.z <= -50:
        #     self.directionZ = -self.directionZ
        # if self.z >= 50:
        #     self.directionZ = -self.directionZ

app = Ursina()
Liste_Boids=[]
anzahl = 50 
create_Wireframe()
create_Boids(anzahl, Liste_Boids)
camera.position = (0,10,-350)
camera.rotation_x = 30
EditorCamera()
app.run()