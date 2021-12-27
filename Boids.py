from ursina import *

class Boids (object):

    #Initialisierung der Klasse
    def __init__ (self, pos, dir):
        self.pos = Vec3(pos)
        self.dir = Vec3(dir)

    #Getter geben den Wert der Eigenschaft zurück
    def getPos(self):
        return self.pos
    
    def getDir(self):
        return self.dir

    #Setter überschreiben die Werte der Eigenschaften
    def setPos(self, nPos):
        self.pos = Vec3(nPos)

    def setDir(self, nDir):
        self.dir = Vec3(nDir)

    def updatePos(self):
        self.pos = self.pos + self.dir
    