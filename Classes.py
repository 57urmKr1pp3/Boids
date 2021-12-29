from ursina import *

class Boid (Entity):
    #Konstruktor der Klasse Entity und Boid wird aufgerufen
    #Position ist ein 3 dimensioanler Vektor mit x, y und z Koordinate
    #Direction ist die Geschwindigkeit mit welcher sich der Boid bewegt, welcher ebenfalls ein 3 dimensioanler Vektor ist
    def __init__(self, index, posX, posY, posZ, dirX, dirY, dirZ):
        super().__init__(2)
#        self.parent = parent
        self.index = index
#        self.position = Vec3(posX, posY, posZ)
        self.X = posX
        self.Y = posY
        self.Z = posZ
#        self.direction = Vec3(dirX, dirY, dirZ)
#        self.directionX = dirX
#        self.directionY = dirY
#        self.directionZ = dirZ
        self.color = color.random_color()
        self.model = 'sprites'
        self.scale = .1
        self.collider = "sprites"
#        self.rotation_directions = 

    #Getter geben die Werte der Eigenschaft zurück
    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction

    #Setter berschreiben die Eigenschaften mit den neuen Werten
    def setPosition(self, nPosX, nPosY, nPosZ):
        self.position = Vec3(nPosX, nPosY, nPosZ)
    
    def setDirection(self, nDirX, nDirY, nDirZ):
        self.direction = Vec3(nDirX, nDirY, nDirZ)

    #Update-Funktion bewegt den Boid durch Vektoraddition der Position und der Richtung
    #damit die bewegung gleichmäßig unabhängig von den aeusseren Umstaenden passiert wird mit time.dt multipliziert
    def update(self):
        self.X += 5
        self.Y += 5
        self.Z += 5
        
class Space(Entity):
    
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.scale = 100
        self.color = color.transperent
        self.position = (0,0,0)