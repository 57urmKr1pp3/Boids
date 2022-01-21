from ursina import *

class Boid (Entity):

    def __init__ (self, posX, posY, posZ, rotX, rotY, rotZ, vel, acel, maxVel, mode, scale):
        super().__init__(model="sprites.blend", position = (posX, posY, posZ), rotation = (rotX, rotY, rotZ), color = color.random_color(), scale = scale)
        self.x = posX
        self.y = posY
        self.z = posZ
        self.vel = vel
        self.acel = acel
        self.maxVel = maxVel
        self.mode = mode
        self.collider = 'mesh'

    #Getter
    def getModel(self):
        return self.model

    def getPosition(self):
        return self.position

    def getRotation(self):
        return self.rotation

    def getColor(self):
        return self.color
    
    def getScale(self):
        return self.scale
    
    def getVel(self):
        return self.vel

    def getAcel(self):
        return self.acel

    def getMaxVel(self):
        return self.maxVel

    def getMode(self):
        return self.mode

    def getCollider(self):
        return self.collider
    
    #Setter
    def setPosition(self, posX, posY, posZ):
        self.position = (posX, posY, posZ)
    
    def setModel(self, nModel):
        self.model = nModel
    
    def setRotation(self, rotX, rotY, rotZ):
        self.rotation = (rotX, rotY, rotZ)

    def setScale(self, nScale):
        self.scale = nScale
    
    def setVel(self, nVel):
        self.vel = nVel
    
    def setAcel(self, nAcel):
        self.acel = nAcel
    
    def setMaxVel(self, nMaxVel):
        self.maxVel = nMaxVel
    
    def setMode(self, nMode):
        self.mode = nMode

    def setCollider(self, nCollider):
        self.collider = nCollider
        
    def updateVel(self):
        if self.vel < self.maxVel:
            self.vel += self.acel

    def move(self):
        self.position += self.up * (self.vel/10000)
        self.updateVel()
        #Warp Modus
        if self.mode == 1:
            if self.x <= -50:
                self.x = 49
            if self.x >= 50:
                self.x = -49
            if self.y <= -50:
                self.y = 49
            if self.y >= 50:
                self.y = 50
            if self.z <= -50:
                self.z = 49
            if self.z >= 50:
                self.z = -49
        #Pong-Modus
        if self.mode == 2:
            if self.x <= -49:
                self.rotation_y = -self.rotation_y
            if self.x >= 49:
                self.rotation_y = -self.rotation_y
            if self.y <= -49:
                self.rotation_z = -self.rotation_z
            if self.y >= 49:
                self.rotation_z = -self.rotation_z
            if self.z <= -49:
                self.rotation_z = -self.rotation_z
            if self.z >= 49:
                self.rotation_z = -self.rotation_z

    def update(self):
        self.move()
