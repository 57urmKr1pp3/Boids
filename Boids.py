from ursina import *

class Boid (object):

    #Initialisierung der Klasse
    def __init__ (self, posX, posY, posZ, dirX, dirY, dirZ):
        self.pos = Vec3(posX, posY, posZ)
        self.dir = Vec3(dirX, dirY, dirZ)

    #Getter geben den Wert der Eigenschaft zurück
    def getPos(self):
        return self.pos
    
    def getDir(self):
        return self.dir

    #Setter überschreiben die Werte der Eigenschaften
    def setPos(self, nPosX, nPosY, nPosZ):
        self.pos = Vec3(nPosX, nPosY, nPosZ)

    def setDir(self, nDirX, nDirY, nDirZ):
        self.dir = Vec3(nDirX, nDirY, nDirZ)

    #Aktualisiert die Position mithilfe der Vektoraddition von Position und Geschwindigkeit
    def updatePos(self):
        self.pos = self.pos + self.dir