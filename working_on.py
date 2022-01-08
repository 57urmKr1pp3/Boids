import math

def rotation(self):
    #Betrag
    tempX = self.x
    tempY = self.y
    tempZ = self.z
    if tempX < 0:
        valueX = -tempX
    else:
        valueX = tempX

    if tempY < 0:
        valueY = -tempY

    else:
        valueY = tempY

    if tempZ < 0:
        valueZ = -tempZ
    else:
        valueZ = tempZ
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