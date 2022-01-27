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
    

def pong(self):
    if self.x <= -49:
        if 