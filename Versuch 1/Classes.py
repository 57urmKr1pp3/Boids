#Import
from ursina import *
import math
from working_on import eigenschaften, rotation

#Klasse
class Boid (Entity):
    #Entity https://www.ursinaengine.org/entity_basics.html 15.01.2022
    #cheat sheet https://www.ursinaengine.org/cheat_sheet_dark.html 15.01.2022

    #Konstruktor der Klasse Entity und Boid wird aufgerufen
    #Position ist ein 3 dimensioanler Vektor mit x, y und z Koordinate
    #Direction ist die Geschwindigkeit mit welcher sich der Boid bewegt, welcher ebenfalls ein 3 dimensioanler Vektor ist
    def __init__(self, posX, posY, posZ, dirX, dirY, dirZ, mode, scale):
        super().__init__()
        self.position = (posX, posY, posZ)
        self.directionX = int(dirX)
        self.directionY = int(dirY)
        self.directionZ = int(dirZ)
        self.color = color.random_color()
        self.model = 'sprites'
        self.scale = scale
        self.mode = mode
        self.collider = 'box'
        
    #Getter geben die Werte der Eigenschaft zurück
    def getPosition(self):
        return self.position

    def getDirection(self):
        return (self.directionX, self.directionY, self.directionZ)

    def getDirectionX(self):
        return self.directionX
    
    def getDirectionY(self):
        return self.directionY
    
    def getDirectionZ(self):
        return self.directionZ

    def getMode(self):
        return self.mode
    
    def getColor(self):
        return self.color
    
    def getModel(self):
        return self.model
    
    def getScale(self):
        return self.scale
    
    #Setter berschreiben die Eigenschaften mit den neuen Werten
    def setPosition(self, nPosX, nPosY, nPosZ):
        self.position =(nPosX, nPosY, nPosZ)
    
    def setDirectionX(self, nDirX):
        self.directionX = nDirX

    def setDirectionY(self, nDirY):
        self.directionY = nDirY

    def setDirectionZ(self, nDirZ):
        self.directionZ = nDirZ
        
    def setColor(self, nColor):
        self.color = color.nColor

    def setScale (self, nScale):
        self.scale = nScale

    def setModel (self, nModel):
        self.model = nModel

    def setMode(self, nMode):
        self.mode = nMode
        
    #Move-Funktion bewegt den Boid durch Addition der Position und der Richtung
    def move(self):

        #Bewegung
        #https://www.ursinaengine.org/entity_basics.html 30.12.21
        self.x += self.directionX * time.dt
        self.y += self.directionY * time.dt
        self.z += self.directionZ * time.dt

        if self.mode == 1:
            #Richtungsänderung beim Erreichen der Grenze
            #https://www.youtube.com/watch?v=NLn-hB1P9tQ 01.01.2022
            if self.x <= -49:
                self.directionX = -self.directionX
            elif self.x >= 49:
                self.directionX = -self.directionX
            if self.y <= -49:
                self.directionY = -self.directionY
            elif self.y >= 49:
                self.directionY = -self.directionY
            if self.z <= -49:
                self.directionZ = -self.directionZ
            elif self.z >= 49:
                self.directionZ = -self.directionZ

        elif self.mode == 2:
            #Teleport zur anderen Seite
            if self.x <= -50:
                self.x = 49
            if self.x >= 50:
                self.x = -49
            if self.y <= -50:
                self.y = 49
            if self.y >= 50:
                self.y = -49
            if self.z <= -50:
                self.z = 49
            if self.z >= 50:
                self.z = -49

        #Bug beim hinzufügen der Boids verursacht das Boids ausserhalb des Würfels sind
        if self.x < -50:
            self.x = -49
        elif self.x > 50:
            self.x = 49
        if self.y < -50:
            self.y = -49
        elif self.y > 50:
            self.y = 49
        if self.z < -50:
            self.z = -49
        elif self.z > 50:
            self.z = 49

        #Rotation
        rotation(self)
    

    #damit die bewegung gleichmäßig unabhängig von den aeusseren Umstaenden passiert wird mit time.dt multipliziert
    #https://www.ursinaengine.org/entity_basics.html 30.12.21
    def update(self):
        self.move()
        eigenschaften(self)
        

# #Rekursionsfehler
# class Wireframe(Entity):

#     def __init__(self, position, scale_achse, scale_wert):
#         super().__init__()

#         self.position = position

#         if scale_achse == "x":
#             self.scale_x = scale_wert
#         elif scale_achse == "y":
#             self.scale_y = scale_wert
#         elif scale_achse == "z":
#             self.scale_z = scale_wert

#         self.model = 'cube'

#     def getPosition(self):
#         return self.position

#     def setPosition(self, nPos):
#         self.position = nPos
#     def setScale(self, nScale):
#         self.scale = nScale

        