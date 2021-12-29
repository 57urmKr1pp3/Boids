from ursina import *

class Boid (Entity):
    #Konstruktor der Klasse Entity und Boid wird aufgerufen
    #Position ist ein § dimensioanler Vektor mit x, y und z Koordinate
    #Direction ist die Geschwindigkeit mit welcher sich der Boid bewegt, welcher ebenfalls ein 3 dimensioanler Vektor ist
    def __init__(self, posX, posY, posZ, dirX, dirY, dirZ, color):
        super().__init__()
        self.position = Vec3(posX, posY, posZ)
        self.direction = Vec3(dirX, dirY, dirZ)
        self.color = color.random_color()

    #Getter geben die Werte der Eigenschaft zurück
    def getPos(self):
        return self.position

    def getDir(self):
        return self.direction

    #Setter berschreiben die Eigenschaften mit den neuen Werten
    def setPos (self, nPosX, nPosY, nPosZ):
        self.position = Vec3(nPosX, nPosY, nPosZ)
    
    def setDir(self, nDirX, nDirY, nDirZ):
        self.direction = Vec3(nDirX, nDirY, nDirZ)

    #Update-Funktion bewegt den Boid durch Vektoraddition der Position und der Richtung
    #damit die bewegung gleichmäßig unabhängig von den aeusseren Umstaenden passiert wird mit time.dt multipliziert
    def update(self):
        self.position += self.direction * time.dt

