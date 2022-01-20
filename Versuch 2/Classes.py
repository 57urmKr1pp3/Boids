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
