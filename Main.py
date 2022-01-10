#Imports
from ursina import *
from random import randint
from Classes import Boid
#Funktionen
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
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20), 1)
        Liste_Boids.append(temp)
def input(key):

    if held_keys["+"]:
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20))
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
anzahl = 1
######################################################################################################################################
Liste_Boids = []
create_Boids(anzahl, Liste_Boids)
print(Liste_Boids)

app.run()