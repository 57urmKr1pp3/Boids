from ursina import *
def eigenschaften(self):
    #proximity
    proximity = []
    for i in Liste_Boids:
        if i != self:
            distanceBoids = distance(self.position, i.position)
            if distanceBoids < 5:
                proximity.append(i)
    #alignment
    Boid1XR = self.rotation_x
    Boid1YR = self.rotation_y
    Boid1ZR = self.rotation_z
    for i in proximity:
        Boid2XR = i.rotation_x
        Boid2YR = i.rotation_y
        Boid2ZR = i.rotation_z
        avgXR = (Boid1XR + Boid2XR)/2
        avgYR = (Boid1YR + Boid2YR)/2
        avgZR = (Boid1ZR + Boid2ZR)/2
        self.rotation_x = avgXR
        self.rotation_y = avgYR
        self.rotation_z = avgZR

    #seperation
    HitInfo = raycast(position = self.position, direction = self.up, distance = 5, traverse_target = scene, ignore = ())
    if HitInfo.hit:
        self.rotation = self.right * self.vel

    #cohesion    
#raycastfront = raycast(origin = self.position, direction = (self.up + self.forward), distance = 10, traverse_target = scene, ignore = (self,), debug = True)
def seperation(self):
    raycastup = raycast(origin = self.position, direction = self.up, distance = 2, traverse_target = scene)
    raycastright = raycast(origin = self.position, direction = self.right, distance = 2, traverse_target = scene)
    raycastleft = raycast(origin = self.position, direction = self.left, distance = 2, traverse_target = scene)
    raycastback = raycast(origin = self.position, direction = self.back, distance = 2, traverse_target = scene)
    raycastforward = raycast(origin = self.position, direction = self.forward, distance = 2, traverse_target = scene)
    if raycastup.hit:
        self.position += self.back * self.vel/100
    if raycastback.hit:
        self.position += self.forward * self.vel/100
    if raycastforward.hit:
        self.position += self.back * self.vel/100
    if raycastright.hit:
        self.position += self.left * self.vel/100
    if raycastleft.hit:
        self.position += self.right * self.vel/100

def pong(self):
    if self.x <= -49:
        if 