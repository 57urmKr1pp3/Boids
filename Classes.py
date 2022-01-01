from ursina import *

class Boid (Entity):
    #Konstruktor der Klasse Entity und Boid wird aufgerufen
    #Position ist ein 3 dimensioanler Vektor mit x, y und z Koordinate
    #Direction ist die Geschwindigkeit mit welcher sich der Boid bewegt, welcher ebenfalls ein 3 dimensioanler Vektor ist
    def __init__(self, index, posX, posY, posZ, dirX, dirY, dirZ):
        super().__init__()
        self.index = index
        self.position = (posX, posY, posZ)
        self.directionX = dirX
        self.directionY = dirY
        self.directionZ = dirZ
        self.color = color.random_color()
        self.model = 'sprites'
        self.scale = 1
        self.collider = "boxes"

        
    #Getter geben die Werte der Eigenschaft zurück
    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction

    #Setter berschreiben die Eigenschaften mit den neuen Werten
    def setPosition(self, nPosX, nPosY, nPosZ):
        self.position =(nPosX, nPosY, nPosZ)
    
    def setDirection(self, nDirX, nDirY, nDirZ):
        self.direction = (nDirX, nDirY, nDirZ)

    #Update-Funktion bewegt den Boid durch Vektoraddition der Position und der Richtung
    #damit die bewegung gleichmäßig unabhängig von den aeusseren Umstaenden passiert wird mit time.dt multipliziert
    def update(self):
        #Bewegung
        self.x += self.directionX * time.dt
        self.y += self.directionY * time.dt
        self.z += self.directionZ * time.dt
        #Richtungsänderung beim Erreichen der Grenze
        if self.x <= -50:
            self.directionX = -self.directionX
        if self.x >= 50:
            self.directionX = -self.directionX
        if self.y <= -50:
            self.directionY = -self.directionY
        if self.y >= 50:
            self.directionY = -self.directionY
        if self.z <= -50:
            self.directionZ = -self.directionZ
        if self.z >= 50:
            self.directionZ = -self.directionZ
        #Rotation
        #self.rotation_x = self.directionX * time.dt
        #self.rotation_y = self.directionY * time.dt
        #self.rotation_z = self.directionZ * time.dt
        