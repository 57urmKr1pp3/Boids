from ursina import *
from Main import Liste_Boids
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

    #Bewegung
    def updateVel(self):
        if self.vel < self.maxVel:
            self.vel += self.acel

    def closeBoids(self):
        close = []
        for i in Liste_Boids:
            if i != self:
                distanceBoids = distance(self.position, i.position)
                if distanceBoids < 5:
                    close.append(i)
        return close

    def alignment(self):
        closeOne = self.closeBoids()
        Boid1XR = self.rotation_x
        Boid1YR = self.rotation_y
        Boid1ZR = self.rotation_z
        for i in closeOne:
            Boid2XR = i.rotation_x
            Boid2YR = i.rotation_y
            Boid2ZR = i.rotation_z
            avgXR = (Boid1XR+Boid2XR)/2
            avgYR = (Boid1YR + Boid2YR)/2
            avgZR = (Boid1ZR + Boid2ZR)/2
            self.rotation_x = avgXR
            self.rotation_y = avgYR
            self.rotation_z = avgZR

    def seperation(self):
        HitInfo = raycast(origin = self.position, direction = self.up, distance = 5, traverse_target = scene)
        while HitInfo.hit:
            self.rotation = self.right * self.vel

    def avoidWall(self):
        #Raycasts
        raycastup = raycast(origin = self.position, direction = self.up, distance = 5, traverse_target = scene, ignore = (self,), debug = True)
        if raycastup.hit:
            raycastfront = raycast(origin = self.position, direction = self.forward, distance = inf, traverse_target = scene, ignore = (self,), debug = True)
            raycastback = raycast(origin = self.position, direction = self.back, distance = inf, traverse_target = scene, ignore = (self,), debug = True)
            raycastleft = raycast(origin = self.position, direction = self.left, distance = inf, traverse_target = scene, ignore = (self,), debug = True)
            raycastright = raycast(origin = self.position, direction = self.right, distance = inf, traverse_target = scene, ignore = (self,), debug = True)

            distance_up = raycastup.distance
            distance_front = raycastfront.distance
            distance_back = raycastback.distance
            distance_left = raycastleft.distance
            distance_right = raycastright.distance

            #up kleinste Distanz
            if (distance_up <= distance_front) and (distance_up <= distance_back) and (distance_up <= distance_left) and (distance_up <= distance_right):
                self.rotation += self.back * (self.vel/10)

            #front kleinste Distanz
            if (distance_front <= distance_up) and (distance_front <= distance_back) and (distance_front <= distance_right) and (distance_up <= distance_left):
                self.rotation += self.back * (self.vel/10)

            #back kleinste Distanz
            if (distance_back <= distance_up) and (distance_back <= distance_front) and (distance_back <= distance_right) and (distance_back <= distance_left):
                self.rotation += self.forward * (self.vel/10)

            #left kleinste Distanz
            if (distance_left <= distance_up) and (distance_left <= distance_right) and (distance_left <= distance_back) and (distance_left <= distance_front):
                self.rotation += self.right * (self.vel/10)

            #right kleinste Distanz
            if (distance_right <= distance_left) and (distance_right <= distance_up) and (distance_right <= distance_front) and (distance_right <= distance_back):
                self.rotation += self.left * (self.vel/10)
            
    def move(self):
        self.position += self.up * (self.vel/1000)
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
                self.y = -50
            if self.z <= -50:
                self.z = 49
            if self.z >= 50:
                self.z = -49

        #Wändevermeidung
        if self.mode == 2:
            self.avoidWall()

        #Pong-Modus
        if self.mode == 3:
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
        self.alignment()
        self.seperation()
        
