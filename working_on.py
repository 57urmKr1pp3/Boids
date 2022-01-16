import math

###############################
# in Main-Update()
###############################

def adaptdir(Boid1, Boid2):

    #Differenz der einzelnen Positionen
    difX = Boid1.x - Boid2.x
    difY = Boid1.y - Boid2.y
    difZ = Boid1.z - Boid2.z
    if difX < 5 and difX > 5 and difY < 5 and difY > -5 and difZ < 5 and difZ > -5:
        avDirX = (Boid1.getDirectionX() + Boid2.getDirectionX())/2
        avDirY = (Boid1.getDirectionY() + Boid2.getDirectionY())/2
        avDirZ = (Boid1.getDirectionZ() + Boid2.getDirectionZ())/2
        Boid1.setDirectionX(avDirX)
        Boid1.setDirectionYavDirY(avDirY)
        Boid1.setDirectionZ(avDirZ)

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

    tempPosX = self.x
    tempPosY = self.y
    tempPosZ = self.z
    
    #Matrix: https://stackoverflow.com/questions/14607640/rotating-a-vector-in-3d-space
    #Berechnung: https://www.mathebibel.de/winkel-zwischen-zwei-vektoren
    #math docs.python.org/3/library/math.html 10.01.2022
    #Rotation https://www.ursinaengine.org/coordinate_system.html 15.01.2022
    #Berechnung
    #bei der Berechnung benutze ich 2D-Vektoren um die einzelnen Winkel zu berechnen
    EinheitsvektorXY = [1, 0]
    EinheitsvektorXZ = [0, 1]
    EinheitsvektorYZ = [1, 0]
    VektorXY = [self.directionX, self.directionY]
    VektorYZ = [self.directionZ, self.directionY]
    VektorXZ = [self.directionX, self.directionX]
    #Testvektoren
    # VektorXY = [2, 5]
    # VektorYZ = [6, 3]
    # VektorXZ = [4, 1]

    #try/except weil de Chance besteht dass im Nenner eine Null vorkommt
    try:
        #Berechnung von Skalarprodukt und Betragprdukt, da sonst falsches Ergebnis
        #Winkel zwischen XY
        skalarXY = VektorXY[0]*EinheitsvektorXY[0] + VektorXY[1]*EinheitsvektorXY[1]
        betragXY = math.sqrt(VektorXY[0]**2+VektorXY[1]**2)*math.sqrt(EinheitsvektorXY[0]**2+EinheitsvektorXY[1]**2)
        radXY = math.acos(skalarXY/betragXY)
        if VektorXY[1] < 0:
            thetaXY = -(-180+math.degrees(radXY))
        else:
            thetaXY = -math.degrees(radXY)
    except:
        thetaXY = 0
    try:
        #Winkel zwischen XZ
        skalarXZ = VektorXZ[0]*EinheitsvektorXZ[0] + VektorXZ[1]*EinheitsvektorXZ[1]
        betragXZ = math.sqrt(VektorXZ[0]**2+VektorXZ[1]**2)*math.sqrt(EinheitsvektorXZ[0]**2+EinheitsvektorXZ[1]**2)
        radXZ = math.acos(skalarXZ/betragXZ)
        if VektorXZ[1] < 0:
            thetaXZ = -(-180+math.degrees(radXZ))
        else:
            thetaXZ = -math.degrees(radXZ)
    except:
        thetaXZ = 0
    try:
        #Winkel zwischen YZ
        skalarYZ = VektorYZ[0]*EinheitsvektorYZ[0] + VektorYZ[1]*EinheitsvektorYZ[1]
        betragYZ = math.sqrt(VektorYZ[0]**2+VektorYZ[1]**2)*math.sqrt(EinheitsvektorYZ[0]**2+EinheitsvektorYZ[1]**2)
        radYZ = math.acos(skalarYZ/betragYZ)
        if VektorYZ[1] < 0:
            thetaYZ = -(-180+math.degrees(radYZ))
        else:
            thetaYZ = -math.degrees(radYZ)
    except:
        thetaYZ = 0

    #Rotieren
    if tempPosX > tempPosY and tempPosX > tempPosZ:
        #da gelegentlich ein UnboundLocalError hervortritt muss dies auch in eine try/except-Verzweigung
        #z-Rotation
        if thetaXY < 0:
            self.world_rotation_z = thetaXY
        else:
            self.world_rotation_z = thetaXY
        #x-Rotation
        if thetaXY < 0:
            self.world_rotation_x = thetaYZ
        else:
            self.world_rotation_x = thetaYZ
    if tempPosY > tempPosX and tempPosY > tempPosZ:
        #x-Rotation
        if thetaXY < 0:
            self.world_rotation_x = thetaYZ
        else:
            self.world_rotation_x = thetaYZ
        #y-Rotation
        if thetaXZ < 0:
            self.world_rotation_y = thetaXZ
        else:
            self.world_rotation_y = thetaXZ
    if tempPosZ > tempPosX and tempPosZ > tempPosY:
        #x-Rotation
        if thetaXY < 0:
            self.world_rotation_x = thetaYZ
        else:
            self.world_rotation_x = thetaYZ
        #z-Rotation
        if thetaXY < 0:
            self.world_rotation_z = thetaXY
        else:
            self.world_rotation_z = thetaXY