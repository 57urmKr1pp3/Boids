#Imports
from ursina import *
from random import randint
from Classes import Boid
#Funktionen
def checkCollision(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)-1):
            difX = Liste_Boids[i].x - Liste_Boids[j].x
            difY = Liste_Boids[i].y - Liste_Boids[j].y
            difZ = Liste_Boids[i].z - Liste_Boids[j].z
            if difX < .5 and difX > .5 and difY < .5 and difY > -.5 and difZ < .5 and difZ > -.5:
                print("True")
                Boid1X = Liste_Boids[i].x + .5
                Boid1Y = Liste_Boids[i].y + .5
                Boid1Z = Liste_Boids[i].z + .5
                Liste_Boids[i].setPosition(Boid1X, Boid1Y, Boid1Z)
def adaptdir(Boid1, Boid2):
    #Differenz der einzelnen Positionen
    difX = Boid1.x - Boid2.x
    difY = Boid1.y - Boid2.y
    difZ = Boid1.z - Boid2.z
    if (difX < 5 and difX > 5) or (difY < 5 and difY > -5) or (difZ < 5 and difZ > -5):
        Boid1dirX = Boid1.getDirectionX
        print(Boid1dirX)
        Boid1dirY = Boid1.getDirectionY
        Boid1dirZ = Boid1.getDirectionZ
        Boid2dirX = Boid2.getDirectionX
        Boid2dirY = Boid2.getDirectionY
        Boid2dirZ = Boid2.getDirectionZ
        avDirX = (Boid1dirX + Boid2dirX)/2
        avDirY = (Boid1dirY + Boid2dirY)/2
        avDirZ = (Boid1dirZ + Boid2dirZ)/2
        Boid1.setDirectionX = avDirX
        Boid1.setDirectionYavDirY = avDirY
        Boid1.setDirectionZ = avDirZ
def create_Wireframe():
    #Wireframe
    wf1 = Entity(model = "cube", position = (0, -51, -51), scale_x = 102)
    wf2 = Entity(model = "cube", position = (-51, -51, 0), scale_z = 102)
    wf3 = Entity(model = "cube", position = (0, -51, 51), scale_x = 102)
    wf4 = Entity(model = "cube", position = (51, -51, 0), scale_z = 102)
    wf5 = Entity(model = "cube", position = (51, 0, 51), scale_y = 102)
    wf6 = Entity(model = "cube", position = (51, 0, -51), scale_y = -102)
    wf7 = Entity(model = "cube", position = (-51, 0, 51), scale_y = 102)
    wf8 = Entity(model = "cube", position = (-51, 0, -51), scale_y = 102)
    wf9 = Entity(model = "cube", position = (-51, 51, 0), scale_z = -102)
    wf10 = Entity(model = "cube", position =(0, 51, 51), scale_x = -102)
    wf11 = Entity(model = "cube", position =(51, 51, 0), scale_z = 102)
    wf12 = Entity(model = "cube", position =(0, 51, -51), scale_x = -102)
def create_Boids(anzahl, liste):
    #Erstellen und speichern der Boids in einer Liste
    for i in range(anzahl):
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20), 1, 7)
        Liste_Boids.append(temp)
def update():
    checkCollision(Liste_Boids)
    for i in range(len(Liste_Boids)-1):
        if i != len(Liste_Boids)-1:
            adaptdir(Liste_Boids[i], Liste_Boids[i+1])

def input(key):

    if held_keys["+"]:
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20), 1, 5)
        Liste_Boids.append(temp)
    if held_keys["-"]:
        Liste_Boids[len(Liste_Boids)-1].disable()
        Liste_Boids.pop()
    if held_keys["1"]:
        for i in Liste_Boids:
            i.setMode(1)
    if held_keys["2"]:
        for i in Liste_Boids:
            i.setMode(2)
#Anwendung
app = Ursina()
#Fenster
window.title = "Boids Simulation"
#Kamera
camera.position = (0,10,-350)
EditorCamera()

#Erstellen
#Wireframe
create_Wireframe()
#Boids

######################################################################################################################################
anzahl = 50
######################################################################################################################################
Liste_Boids = []
create_Boids(anzahl, Liste_Boids)

app.run()