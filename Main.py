#Imports
from ursina import *
from random import randint
from Classes import Boid, Wireframe

#Funktionen
def Eigenschaften(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)-1):
            difX = Liste_Boids[i].x - Liste_Boids[j].x
            difY = Liste_Boids[i].y - Liste_Boids[j].y
            difZ = Liste_Boids[i].z - Liste_Boids[j].z
            if difX < 6.5 and difX > 6.5 and difY < 6.5 and difY > -6.5 and difZ < 6.5 and difZ > -6.5:
                print("True")
                Boid1X = Liste_Boids[i].x + .5
                Boid1Y = Liste_Boids[i].y + .5
                Boid1Z = Liste_Boids[i].z + .5
                Liste_Boids[i].setPosition(Boid1X, Boid1Y, Boid1Z)

            if (difX < 30 and difX > 30) or (difY < 30 and difY > -30) or (difZ < 30 and difZ > -30):
                Boid1dirX = Liste_Boids[i].directionX
                Boid1dirY = Liste_Boids[i].directionY
                Boid1dirZ = Liste_Boids[i].directionZ
                Boid2dirX = Liste_Boids[j].directionX
                Boid2dirY = Liste_Boids[j].directionY
                Boid2dirZ = Liste_Boids[j].directionZ
                avDirX = (Boid1dirX + Boid2dirX)/2
                avDirY = (Boid1dirY + Boid2dirY)/2
                avDirZ = (Boid1dirZ + Boid2dirZ)/2
                Liste_Boids[i].setDirectionX = avDirX
                Liste_Boids[i].setDirectionY = avDirY
                Liste_Boids[i].setDirectionZ = avDirZ

def create_Wireframe():
    #Wireframe
    wf1 = Entity(model = "cube", position = (0, -51, -51), scale = (102,1,1))
    wf2 = Entity(model = "cube", position = (-51, -51, 0), scale = (1,1,102))
    wf3 = Entity(model = "cube", position = (0, -51, 51), scale = (102,1,1))
    wf4 = Entity(model = "cube", position = (51, -51, 0), scale = (1,1,102))
    wf5 = Entity(model = "cube", position = (51, 0, 51), scale = (1,102,1))
    wf6 = Entity(model = "cube", position = (51, 0, -51), scale = (1,-102,1))
    wf7 = Entity(model = "cube", position = (-51, 0, 51), scale = (1,102,1))
    wf8 = Entity(model = "cube", position = (-51, 0, -51), scale = (1,102,1))
    wf9 = Entity(model = "cube", position = (-51, 51, 0), scale = (1,1,-102))
    wf10 = Entity(model = "cube", position =(0, 51, 51), scale = (-102,1,1))
    wf11 = Entity(model = "cube", position =(51, 51, 0), scale = (1,1,102))
    wf12 = Entity(model = "cube", position =(0, 51, -51), scale = (-102,1,1))

def create_Boids(anzahl, liste):
    #Erstellen und speichern der Boids in einer Liste
    for i in range(anzahl):
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), 1, 15)
        Liste_Boids.append(temp)

def update():
    Eigenschaften(Liste_Boids)

def input(key):
    if held_keys["+"]:
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), 1, 15)
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
anzahl = 2
######################################################################################################################################

Liste_Boids = []
create_Boids(anzahl, Liste_Boids)

app.run()