import math
from re import L
###############################
# in Main-Update()
###############################
def adaptdir(Boid1, Boid2):
    #Differenz der einzelnen Positionen
    difX = Boid1.x - Boid2.x
    difY = Boid1.y - Boid2.y
    difZ = Boid1.z - Boid2.z
    if difX < 5 and difX > 5 and difY < 5 and difY > -5 and difZ < 5 and difZ > -5:
        avDirX = (Boid1.getDirectionX + Boid2.getDirectionX)/2
        avDirY = (Boid1.getDirectionY + Boid2.getDirectionY)/2
        avDirZ = (Boid1.getDirectionZ + Boid2.getDirectionZ)/2
        Boid1.setDirectionX = avDirX
        Boid1.setDirectionYavDirY = avDirY
        Boid1.setDirectionZ = avDirZ

def checkCollision(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)-1):
            difX = Liste_Boids[i].x - Liste_Boids[j].x
            difY = Liste_Boids[i].y - Liste_Boids[j].y
            difZ = Liste_Boids[i].z - Liste_Boids[j].z
            if difX < .5 and difX > .5 and difY < .5 and difY > -.5 and difZ < .5 and difZ > -.5:
                Boid1X = Liste_Boids[i].x + .5
                Boid1Y = Liste_Boids[i].y + .5
                Boid1Z = Liste_Boids[i].z + .5
                Liste_Boids[i].setPosition(Boid1X, Boid1Y, Boid1Z)
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
    EinheitsvektorXZ = [1, 0]
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
        if VektorXY[1] < 0:
            angleXY = -(-180+math.degrees(radXY))
        else:
            angleXY = -math.degrees(radXY)
        #Winkel zwischen XZ
        skalarXZ = VektorXZ[0]*EinheitsvektorXZ[0] + VektorXZ[1]*EinheitsvektorXZ[1]
        betragXZ = math.sqrt(VektorXZ[0]**2+VektorXZ[1]**2)*math.sqrt(EinheitsvektorXZ[0]**2+EinheitsvektorXZ[1]**2)
        radXZ = math.acos(skalarXZ/betragXZ)
        if VektorXZ[1] < 0:
            angleXZ = -(-180+math.degrees(radXZ))
        else:
            angleXZ = -math.degrees(radXZ)

        #Winkel zwischen YZ
        skalarYZ = VektorYZ[0]*EinheitsvektorYZ[0] + VektorYZ[1]*EinheitsvektorYZ[1]
        betragYZ = math.sqrt(VektorYZ[0]**2+VektorYZ[1]**2)*math.sqrt(EinheitsvektorYZ[0]**2+EinheitsvektorYZ[1]**2)
        radYZ = math.acos(skalarYZ/betragYZ)
        if VektorYZ[1] < 0:
            angleYZ = -(-180+math.degrees(radYZ))
        else:
            angleYZ = -math.degrees(radYZ)
            
    except:
        pass
    #Rotieren
    try:
        if tempPosX > tempPosY and tempPosX > tempPosZ:
            #da gelegentlich ein UnboundLocalError hervortritt muss dies auch in eine try/except-Verzweigung
            #z-Rotation
            if angleXY < 0:
                self.world_rotation_z = angleXY
            else:
                self.world_rotation_z = angleXY
            #x-Rotation
            if angleXY < 0:
                self.world_rotation_x = angleYZ
            else:
                self.world_rotation_x = angleYZ
    except:
        self.world_rotation_x = 0
        self.world_rotation_y = 0
        self.world_rotation_z = 0
    try:
        if tempPosY > tempPosX and tempPosY > tempPosZ:
            #x-Rotation
            if angleXY < 0:
                self.world_rotation_x = angleYZ
            else:
                self.world_rotation_x = angleYZ
            #y-Rotation
            if angleXZ < 0:
                self.world_rotation_y = angleXZ
            else:
                self.world_rotation_y = angleXZ
    except:
        self.world_rotation_x = 0
        self.world_rotation_y = 0
        self.world_rotation_z = 0
    try:
        if tempPosZ > tempPosX and tempPosZ > tempPosY:
            #x-Rotation
            if angleXY < 0:
                self.world_rotation_x = angleYZ
            else:
                self.world_rotation_x = angleYZ
            #z-Rotation
            if angleXY < 0:
                self.world_rotation_z = angleXY
            else:
                self.world_rotation_z = angleXY
    except:
        self.world_rotation_x = 0
        self.world_rotation_y = 0
        self.world_rotation_z = 0
