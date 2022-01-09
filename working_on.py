import math
from random import randint

from Main import Liste_Boids
#############################
#in Main.py
#############################
def input(key):
    if held_keys["+"]:
        temp = Boid(i, randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-20, 20), randint(-20, 20), randint(-20, 20))
        Liste_Boids.append(temp)
    if held_keys["-"]:
        Liste_Boids[len(Liste_Boids)-1].disable()
        Liste_Boids.pop()

#############################
#in Boids und update()
#############################
def rotation(self):
    #Rotation davor
    tempRotX = self.rotation_x
    tempRotY = self.rotation_y
    tempRotZ = self.rotation_z
    #Position davor
    tempPosX = self.x
    tempPosY = self.y
    tempPosZ = self.z
    #Betrag
    if tempPosX < 0:
        valueX = -tempPosX
    else:
        valueX = tempPosX

    if tempPosY < 0:
        valueY = -tempPosY

    else:
        valueY = tempPosY

    if tempPosZ < 0:
        valueZ = -tempPosZ
    else:
        valueZ = tempPosZ
    #Berechnung
    #bei der Berechnung benutze ich 2D-Vektoren um die einzelnen Winkel zu berechnen
    EinheitsvektorXY = [1, 0]
    EinheitsvektorYXZ = [0, 1]
    EinheitsvektorZY = [1, 0]
    VektorXY = [self.directionX, self.directionY]
    VektorZY = [self.directionZ, self.directionY]
    VektorXZ = [self.directionX, self.directionX]
    angleXY
    angleZX
    angleYZ
    #Rotieren