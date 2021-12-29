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


app = Ursina()
bereich = Space
camera.position = (0,15,-26)
camera.rotation_x = 30
#später ersetzen durch GUI User Input
count = int(input("Wieviele Boids sollen erstellt werden?"))
#speichern der Boids in einer Liste

Liste_Boids = []
for i in range(count):
    temp = Boid(i, randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
    Liste_Boids.append(temp)
print(Liste_Boids)

#while run():
#    for i in Liste_Boids:
#        i.update()
#    adaptDir(Liste_Boids)
#    checkPos(Liste_Boids)

app.run()