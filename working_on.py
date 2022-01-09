import math

# #############################
# #in Boids und update()
# #############################
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
    EinheitsvektorXZ = [0, 1]
    EinheitsvektorYZ = [1, 0]
    VektorXY = [self.directionX, self.directionY]
    VektorYZ = [self.directionZ, self.directionY]
    VektorXZ = [self.directionX, self.directionX]
    # VektorXY = [2, 5]
    # VektorYZ = [6, 3]
    # VektorXZ = [4, 1]
    try:
        #Berechnung von Skalarprodukt und Betragprdukt, da sonst falsches Ergebnis
        #Winkel zwischen XY
        skalarXY = VektorXY[0]*EinheitsvektorXY[0] + VektorXY[1]*EinheitsvektorXY[1]
        betragXY = math.sqrt(VektorXY[0]**2+VektorXY[1]**2)*math.sqrt(EinheitsvektorXY[0]**2+EinheitsvektorXY[1]**2)
        radXY = math.acos(skalarXY/betragXY)
        angleXY = math.degrees(radXY)
        #Winkel zwischen XZ
        skalarXZ = VektorXZ[0]*EinheitsvektorXZ[0] + VektorXZ[1]*EinheitsvektorXZ[1]
        betragXZ = math.sqrt(VektorXZ[0]**2+VektorXZ[1]**2)*math.sqrt(EinheitsvektorXZ[0]**2+EinheitsvektorXZ[1]**2)
        radXZ = math.acos(skalarXZ/betragXZ)
        angleXZ = math.degrees(radXZ)
        #Winkel zwischen YZ
        skalarYZ = VektorYZ[0]*EinheitsvektorYZ[0] + VektorYZ[1]*EinheitsvektorYZ[1]
        betragYZ = math.sqrt(VektorYZ[0]**2+VektorYZ[1]**2)*math.sqrt(EinheitsvektorYZ[0]**2+EinheitsvektorYZ[1]**2)
        radYZ = math.acos(skalarYZ/betragYZ)
        angleYZ = math.degrees(radYZ)
    except:
        pass
    #Rotieren
    if tempPosX > tempPosY and tempPosX > tempPosZ:
        #z-Rotation
        if angleXY < 0:
            self.rotation_z = -angleXY
        else:
            self.rotation_z = angleXY
        #x-Rotation
        if angleXY < 0:
            self.rotation_x = -angleYZ
        else:
            self.rotation_x = angleYZ
    if tempPosY > tempPosX and tempPosY > tempPosZ:
        #x-Rotation
        if angleXY < 0:
            self.rotation_x = -angleYZ
        else:
            self.rotation_x = angleYZ
        #y-Rotation
        if angleXZ < 0:
            self.rotation_y = -angleXZ
        else:
            self.rotation_y = angleXZ
    if tempPosZ > tempPosX and tempPosZ > tempPosY:
        #x-Rotation
        if angleXY < 0:
            self.rotation_x = -angleYZ
        else:
            self.rotation_x = angleYZ
        #z-Rotation
        if angleXY < 0:
            self.rotation_z = -angleXY
        else:
            self.rotation_z = angleXY
