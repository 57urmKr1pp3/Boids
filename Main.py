from ursina import entity
from Classes import Boid
from Classes import Space
from ursina import *
from random import randint

#Angleichung der Geschwindigkeit/Direction
def adaptDir(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)-1):
            difPos = [0, 0 ,0]
            difPos[0] = Liste_Boids[i].getPosition()[0] - Liste_Boids[j].getPosition()[0]
            difPos[1] = Liste_Boids[i].getPosition()[1] - Liste_Boids[j].getPosition()[1]
            difPos[2] = Liste_Boids[i].getPosition()[2] - Liste_Boids[j].getPosition()[2]
            if difPos[0] < 5 and difPos[0] > -5 and difPos[1] < 5 and difPos[1] > -5 and difPos[2] < 5 and difPos[2] > -5:
                averageDir = [0, 0, 0]
                averageDir[0] = (Liste_Boids[i].getPosition()[0] + Liste_Boids[j].getPosition()[0]) / 2
                averageDir[1] = (Liste_Boids[i].getPosition()[1] + Liste_Boids[j].getPosition()[1]) / 2
                averageDir[2] = (Liste_Boids[i].getPosition()[2] + Liste_Boids[j].getPosition()[2]) / 2
                Liste_Boids[i].setDirection(averageDir[0], averageDir[1], averageDir[2])
                Liste_Boids[j].setDirection(averageDir[0], averageDir[1], averageDir[2])

#versetzt Boid wenn er auf einem anderen ist
def checkPos(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(len(Liste_Boids)-1):
            if Liste_Boids[i].getPosition() == Liste_Boids[j].getPosition():
                nPos=[Liste_Boids[i].getPosition()[0] + 5, Liste_Boids[i].getPosition()[1] + 5, Liste_Boids[i].getPosition()[2] + 5]
                Liste_Boids[i].setPosition(nPos[0], nPos[1], nPos[2])

def input(keys):
    #Kamerabewegung
    #rechts, links
    if held_keys["d"]:
        camera.position += (time.dt, 0, 0)
    if held_keys["a"]:
        camera.position -= (time.dt, 0, 0)
    #hoch, runter
    if held_keys["space"]:
        camera.position += (0, time.dt, 0)
    if held_keys["left_control"]:
        camera.position -= (0, time.dt, 0)
    #vorwaerts, rueckwaerts
    if held_keys["w"]:
        camera.position += (0, 0, time.dt)
    if held_keys["s"]:
        camera.position -= (0, 0, time.dt)

app = Ursina()
#Fenster
window.title = "Boids Simulation"
#Kamera
camera.position = (0,10,-350)
camera.rotation_x = 30
EditorCamera()
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

#Erstellen der Boids
count = 500
#speichern der Boids in einer Liste
Liste_Boids = []
for i in range(count):
    temp = Boid(i, randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-49, 49), randint(-49, 49), randint(-49, 49))
    Liste_Boids.append(temp)
print(Liste_Boids)


app.run()