from Classes import Boid
from ursina import *
from random import randint
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
        temp = Boid(i, randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20))
        Liste_Boids.append(temp)

def input(key):
    #Kamerabewegung
    #rechts, links
    if held_keys["d"]:
        camera.position += (time.dt*1000, 0, 0)
    if held_keys["a"]:
        camera.position -= (time.dt*1000, 0, 0)
    #hoch, runter
    if held_keys["space"]:
        camera.position += (0, time.dt*1000, 0)
    if held_keys["left_control"]:
        camera.position -= (0, time.dt*1000, 0)
    #vorwaerts, rueckwaerts
    if held_keys["w"]:
        camera.z += time.dt*1000
    if held_keys["s"]:
        camera.z -= time.dt*1000

app = Ursina()
#Fenster
window.title = "Boids Simulation"
#Kamera
camera.position = (0,10,-350)
camera.rotation_x = 30
EditorCamera()
#Wireframe
create_Wireframe()
#Erstellen der Boids
######################################################################################################################################
anzahl = 20
######################################################################################################################################
Liste_Boids = []
create_Boids(anzahl, Liste_Boids)
print(Liste_Boids)


app.run()