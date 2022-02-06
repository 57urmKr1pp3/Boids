from ursina import *
import sys
from random import randint
from ursina import collider

from ursina.color import random_color



app = Ursina()

boids_anzahl = 1
boids = []
cameraE = Entity(model='cube', scale=(0.1,0.1,0.1), alpha=100, position=(0,0,-50), visible=False)

camera.position = cameraE.position



def cameraUser():

    if held_keys['w']:
        cameraE.rotation = camera.rotation
        cameraE.position += (cameraE.forward)*15
        camera.position = cameraE.position
    if held_keys['s']:
        cameraE.rotation = camera.rotation
        cameraE.position += (cameraE.back)*15
        camera.position = cameraE.position

    if held_keys['d']:
        cameraE.rotation = camera.rotation
        cameraE.position += (cameraE.right)*15
        camera.position = cameraE.position
    if held_keys['a']:
        cameraE.rotation = camera.rotation
        cameraE.position += (cameraE.left)*15
        camera.position = cameraE.position  

    if mouse.left == False and mouse.visible == False:
        camera.rotation_x += mouse.y * -20
        camera.rotation_y += mouse.x * 20


def input(key):
    if key == 'alt':
        mouse.visible = not mouse.visible
        mouse.locked = True
        mouse.position = (0,0,0)

    if key == 'escape':
        mouse.visible = True
        mouse.locked = False
    #print('Position camera:' , camera.x, camera.y, camera.z)

def create1():
    return Entity(model='cube', color=color.black, scale=(0.1,20,0.1), alpha=180)
def create2():
    return Entity(model='cube', color=color.black, scale=(20,0.1,0.1), alpha=180)
def create3():
    return Entity(model='cube', color=color.black, scale=(0.1,0.1,20), alpha=180)

w_vorne = Entity(model='cube', color=color.black, scale=(20,20,0), alpha=100, position=(0,0,0))
w_vorne.collider = 'mesh'
w_hinten = Entity(model='cube', color=color.black, scale=(20,20,0), alpha=100, position=(0,0,-20))
w_hinten.collider = 'mesh'
w_unten = Entity(model='cube', color=color.black, scale=(20,0,20), alpha=100, position=(0,-10,-10))
w_unten.collider = 'mesh'
w_oben = Entity(model='cube', color=color.black, scale=(20,0,20), alpha=100, position=(0,10,-10))
w_oben.collider = 'mesh'
w_links = Entity(model='cube', color=color.black, scale=(0,20,20), alpha=100, position=(10,0,-10))
w_links.collider = 'mesh'
w_rechts = Entity(model='cube', color=color.black, scale=(0,20,20), alpha=100, position=(-10,0,-10))
w_rechts.collider = 'mesh'

raster_vorn_links = create1()
raster_vorn_rechts = create1()
raster_hinten_links = create1()
raster_hinten_rechts = create1()
raster_vorn_oben = create2()
raster_vorn_unten = create2()
raster_hinten_oben = create2()
raster_hinten_unten = create2()
raster_oben_links = create3()
raster_oben_rechts = create3()
raster_unten_links = create3()
raster_unten_rechts = create3()

raster_vorn_links.position = (-10,0,0)
raster_vorn_rechts.position = (10,0,0)
raster_hinten_links.position = (-10,0,-20)
raster_hinten_rechts.position = (10,0,-20)
raster_vorn_oben.position = (0,10,0)
raster_vorn_unten.position = (0,-10,0)
raster_hinten_oben.position = (0,10,-20)
raster_hinten_unten.position = (0,-10,-20)
raster_oben_links.position = (-10,10,-10)
raster_oben_rechts.position = (10,10,-10)
raster_unten_links.position = (-10,-10,-10)
raster_unten_rechts.position = (10,-10,-10)




class Boid(Entity):
    def __init__(self, ID, x, y, z, xr, yr, zr, speed, grenze, variable):
        super().__init__(model='entity', position=(x,y,z), rotation=(xr,yr,zr), scale=(.2,.2,.2) , color=color.white)

        self.ID = ID

        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        self.grenze = grenze
        self.variable = variable
        self.wand_colision = False

    def getID(self):
        return self.ID

    def bewegen(self):
        self.position += self.up*(self.speed/1000)

    def bewegen1(self):
        hit_info_up = boxcast(origin=self.position, direction=(self.up), thickness=(3,3), distance=3, debug=False, traverse_target=scene, ignore=(self,))
        hit_info_left = boxcast(origin=self.position, direction=(self.left), thickness=(3,3), distance=3, debug=False, traverse_target=scene, ignore=(self,))
        hit_info_right = boxcast(origin=self.position, direction=(self.right), thickness=(3,3), distance=3, debug=False, traverse_target=scene, ignore=(self,))
        hit_info_forward = boxcast(origin=self.position, direction=(self.forward), thickness=(3,3), distance=3, debug=False, traverse_target=scene, ignore=(self,))
        hit_info_back = boxcast(origin=self.position, direction=(self.back), thickness=(3,3), distance=3, debug=False, traverse_target=scene, ignore=(self,))
        x1 = self.position[0]
        y1 = self.position[1]
        z1 = self.position[2]
        self.update()
        x2 = self.position[0]
        y2 = self.position[1]
        z2 = self.position[2]

        temprechnenx = (x2-x1)
        if temprechnenx < 0:
            rechnenx = temprechnenx*-1
        else:
            rechnenx = temprechnenx 
        temprechneny = (y2-y1)
        if temprechneny < 0:
            rechneny = temprechneny*-1
        else:
            rechneny = temprechneny
        temprechnenz = (z2-z1)
        if temprechnenz < 0:
            rechnenz = temprechnenz*-1
        else:
            rechnenz = temprechnenz

    def wandVermeiden1(self):
        hit_info = raycast(self.position, self.up, ignore=(self,), distance = inf, debug = False)
        hit_info_right = raycast(origin=(self.position), direction=self.right, ignore=(self,), distance = 4, debug = True)
        hit_info_left = raycast(origin=(self.position), direction=self.left, ignore=(self,), distance = 4, debug = True)
        hit_info_forward = raycast(origin=(self.position), direction=self.forward, ignore=(self,), distance = 4, debug = True)
        hit_info_back = raycast(origin=(self.position), direction=self.back, ignore=(self,), distance = 4, debug = True)

        distanz = hit_info.distance

        # if hit_info.hit:
        #     self.rotation += self.left * self.speed/5



        # if hit_info_right.hit:
        #     self.rotation += self.left * self.speed/5
        # if hit_info_left.hit:
        #     self.rotation += self.right * self.speed/5
        # if hit_info_forward.hit:
        #     self.rotation += self.back * self.speed/5
        # if hit_info_back.hit:
        #     self.rotation += self.forward * self.speed/5




        # if hit_info_right.hit:
        #     self.rotation += self.left * self.speed/5
        
        # if hit_info_right.hit and hit_info_forward.hit:
        #     self.rotation += self.back * self.speed/5

        # if 

    
        






        # if hit_info.hit and hit_info_forward.hit:
        #     self.rotation += self.back * self.speed/5
        
        # if hit_info.hit and hit_info_back.hit:
        #     self.rotation += self.forward * self.speed/5





        #     if hit_info_right.hit:
        #         self.rotation += self.left * self.speed/5

        #     elif hit_info_right.hit and hit_info_forward.hit:
        #         self.rotation += self.left * self.speed/5

        #     elif hit_info_right.hit and hit_info_back.hit:
        #         self.rotation += self.forward * self.speed/5
            

            
        #     elif hit_info_left.hit:
        #         self.rotation += self.right * self.speed/5

        #     elif hit_info_left.hit and hit_info_back.hit:
        #         self.rotation += self.right * self.speed/5

        #     elif hit_info_left.hit and hit_info_forward.hit:
        #         self.rotation += self.back * self.speed/5

        #     elif hit_info_forward.hit:
        #         self.rotation += self.back * self.speed/5

        #     elif hit_info_back.hit:
        #         self.rotation += self.forward * self.speed/5
                



        #     elif hit_info_right.hit and hit_info_forward.hit and hit_info_back.hit:
        #         self.rotation += self.left * self.speed/5

        #     elif hit_info_left.hit and hit_info_forward.hit and hit_info_back.hit:
        #         self.rotation += self.right * self.speed/5

        #     elif hit_info_back.hit and hit_info_left.hit and hit_info_right.hit:
        #         self.rotation += self.forward * self.speed/5

        #     elif hit_info_forward and hit_info_left and hit_info_right:
        #         self.rotation += self.back * self.speed/5   


            # if hit_info_forward.hit:
            #     self.rotation += self.back * self.speed/5
            #     if hit_info_right.hit:
            #         self.rotation += self.left * self.speed/5
            #     if hit_info_left.hit:
            #         self.rotation += self.back * self.speed/5                   

        # if hit_info.hit:
        #     self.rotation += self.right * self.speed/5
        # if hit_info_right.hit:
        #     self.rotation += self.up *self.speed/5
        # if hit_info_left.hit:
        #     self.rotation += self.up *self.speed/5

        # if hit_info.hit and hit_info_right.hit:
        #     self.rotation += self.left * self.speed
        # if hit_info.hit and hit_info_left.hit:
        #     self.rotation += self.left * self.speed
        # if hit_info_right.hit and hit_info_left.hit:
        #     self.bewegen()

    def wand_vermeiden(self):

        variable = 1
        a = False

        self.bewegen()

        hit_info = raycast(origin=(self.position), direction=self.up, ignore=(self,), distance = 6, debug = True)
        distanz_up = hit_info.distance
        #print(distanz_up)

        steering_right = False
        steering_left = False
        steering_back = False
        steering_forward = False




        if not hit_info.hit:



            hit_info_right1 = raycast(origin=(self.position), direction=self.right, ignore=(self,), distance = 1, debug = False)
            hit_info_left1 = raycast(origin=(self.position), direction=self.left, ignore=(self,), distance = 1, debug = False)
            hit_info_forward1 = raycast(origin=(self.position), direction=self.forward, ignore=(self,), distance = 1, debug = False)
            hit_info_back1 = raycast(origin=(self.position), direction=self.back, ignore=(self,), distance = 1, debug = False)

            if hit_info_right1.hit and not hit_info_left1.hit and not hit_info_forward1.hit and not hit_info_back1.hit:
                self.rotation += self.left * self.speed/2
            if hit_info_left1.hit and not hit_info_right1.hit and not hit_info_forward1.hit and not hit_info_back1.hit:
                self.rotation += self.right * self.speed/2
            if hit_info_forward1.hit and not hit_info_left1.hit and not hit_info_right1.hit and not hit_info_back1.hit:
                self.rotation += self.back * self.speed/2
            if hit_info_back1.hit and not hit_info_left1.hit and not hit_info_forward1.hit and not hit_info_right1.hit:
                self.rotation += self.forward * self.speed/2


        # if hit_info == False:
        #     self.distanz = 3
        #     print('ok')
        #     self.variable = 1        
        if hit_info.hit:

            # if self.distanz >=0 and self.variable >= 0:
            #     self.distanz -= .1
            #     print('Distanz',self.distanz)
            #     self.variable += 1
            #     print('Variable',self.variable)

            hit_info_right = raycast(origin=(self.position), direction=(self.up+self.back), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_left = raycast(origin=(self.position), direction=(self.up+self.forward), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_forward = raycast(origin=(self.position), direction=(self.up+self.left), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_back = raycast(origin=(self.position), direction=(self.up+self.right), ignore=(self,), distance = inf, debug = True, traverse_target=scene)




        
            distanz_right = hit_info_right.distance
            distanz_left = hit_info_left.distance
            distanz_forward = hit_info_forward.distance
            distanz_back = hit_info_back.distance

            print(distanz_right, distanz_left, distanz_forward, distanz_back)


            if distanz_right < distanz_left and distanz_right < distanz_forward and distanz_right < distanz_back:
                self.rotation += self.left * self.speed
                #steering_right = True  
                #print('right')

            if distanz_left < distanz_right and distanz_left < distanz_forward and distanz_left < distanz_back:
                self.rotation += self.right * self.speed
                #steering_left = True
                #print('left')

            if distanz_forward < distanz_right and distanz_forward < distanz_left and distanz_forward < distanz_back:
                self.rotation += self.back * self.speed
                #steering_forward = True
                #print('forward')

            if distanz_back < distanz_left and distanz_back < distanz_right and distanz_back < distanz_forward:
                self.rotation += self.forward * self.speed
                #steering_back = True
                #print('back')
            
            # if distanz_right == distanz_left and distanz_right == distanz_forward and distanz_right == distanz_back and distanz_left == distanz_forward and distanz_left == distanz_back and distanz_forward == distanz_back:
            #     self.rotation += self.right * self.speed/10


        # if steering_right == True:
            
        # if steering_left == True:
            
        # if steering_forward == True:
            
        # if steering_back == True:
            

            

        #     if distanz_back > 0:
        #         a = True
        #         distanz_back = 0

        # if a == True:
        #     self.rotation += self.back * self.speed/5

    def wandVermeiden(self):

        hit_info = boxcast(self.position, self.up, ignore=(self,), distance = 3, debug = True)
        hit_info_right = boxcast(self.position, self.right, ignore=(self,), distance = 1, debug = False)
        hit_info_left = boxcast(self.position, self.left, ignore=(self,), distance = 1, debug = False)
        hit_info_forward = boxcast(self.position, direction=self.forward, ignore=(self,), distance = 1, debug = True)
        hit_info_back = boxcast(self.position, direction=self.back, ignore=(self,), distance = 1, debug = True)


        if hit_info.hit:
            self.wand_colision = True
            self.rotation += self.right * self.speed/5

            if hit_info_right.hit:
                self.rotation += self.left * self.speed/5 

            elif hit_info_left.hit:
                self.rotation += self.right * self.speed/5

            elif hit_info_forward.hit:
                self.rotation += self.back * self.speed/5
            
            elif hit_info_back.hit:
                self.rotation += self.forward * self.speed/5

        elif hit_info_left.hit:
            self.rotation += self.right * self.speed/5
            
        elif hit_info_right.hit:
            self.rotation += self.left * self.speed/5 
            
        elif hit_info_forward.hit:
            self.rotation += self.back * self.speed/5

        elif hit_info_back.hit:
            self.rotation += self.right * self.speed/5
        
        else:
            self.wand_colision = False

        #print(self.wand_colision)
            

    def wandVermeiden_v213123(self):


        hit_info = raycast(origin=(self.position), direction=self.up, ignore=(self,), distance = 7, debug = True)
        distanz_up = hit_info.distance
        print(distanz_up)


        # if hit_info == False:
        #     self.distanz = 3
        #     print('ok')
        #     self.variable = 1        
        if hit_info.hit:
            # if self.distanz >=0 and self.variable >= 0:
            #     self.distanz -= .1
            #     print('Distanz',self.distanz)
            #     self.variable += 1
            #     print('Variable',self.variable)

            hit_info_right = raycast(origin=(self.position), direction=(self.up+self.back), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_left = raycast(origin=(self.position), direction=(self.up+self.forward), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_forward = raycast(origin=(self.position), direction=(self.up+self.left), ignore=(self,), distance = inf, debug = True, traverse_target=scene)
            hit_info_back = raycast(origin=(self.position), direction=(self.up+self.right), ignore=(self,), distance = inf, debug = True, traverse_target=scene)

        
            distanz_right = hit_info_right.distance
            distanz_left = hit_info_left.distance
            distanz_forward = hit_info_forward.distance
            distanz_back = hit_info_back.distance

            print(distanz_right, distanz_left, distanz_forward, distanz_back)


            if ((distanz_right <= distanz_left) and (distanz_right <= distanz_forward) and (distanz_right <= distanz_back)):
                self.rotation += self.left * self.speed/5
                #steering_right = True  
                #print('right')

            elif ((distanz_left <= distanz_right) and (distanz_left <= distanz_forward) and (distanz_left <= distanz_back)):
                self.rotation += self.right * self.speed/5
                #steering_left = True
                #print('left')

            elif ((distanz_forward <= distanz_right) and (distanz_forward <= distanz_left) and (distanz_forward <= distanz_back)):
                self.rotation += self.back * self.speed/5
                #steering_forward = True
                #print('forward')

            elif ((distanz_back <= distanz_left) and (distanz_back <= distanz_right) and (distanz_back <= distanz_forward)):
                self.rotation += self.forward * self.speed/5
                #steering_back = True
                #print('back')



        # if hit_info.hit:
        #     self.wand_colision = True
        #     self.rotation += self.right * self.speed
        # else:
        #     self.wand_colision = False
        # if hit_info_right.hit:
        #     self.wand_colision = True
        #     self.rotation += self.up * .1
        # else:
        #     self.wand_colision = False
        # if hit_info_left.hit:
        #     self.wand_colision = True
        #     self.rotation += self.up * .1
        # else:
        #     self.wand_colision = False

        # if hit_info.hit and hit_info_right.hit:
        #     self.wand_colision = True
        #     self.rotation += self.left * self.speed
        # else:
        #     self.wand_colision = False
        # if hit_info.hit and hit_info_left.hit:
        #     self.wand_colision = True
        #     self.rotation += self.left * self.speed
        # else:
        #     self.wand_colision = False
        # if hit_info_right.hit and hit_info_left.hit:
        #     pass

    def separation(self, neighbors):
        pass

        # for boid in neighbors:
        #     x1 = int(self.x - boid.x)
        #     y1 = int(self.y - boid.y)
        #     z1 = int(self.z - boid.z)



            # print(direction)


            # x2 = int(self.x - boid.x)
            # y2 = int(self.y - boid.y)
            # z2 = int(self.z - boid.z)

            # print(x1, x2)


                

    def alignment(self, neighbors):
        liste_direction = []
        #print(neighbors)

        for i in range(len(neighbors)):
            direction = neighbors[i].rotation 
            liste_direction.append(direction)
        
        try:
            direction_durchnitt = sum(liste_direction)/len(liste_direction)
            self.rotation = direction_durchnitt            
        except ZeroDivisionError:
            print('man teilt durch null')

        #print('ich:',self.rotation)


    def get_neighbors(self):

        group = [self]

#Astatz 1

        for boid in boids:
            if boid != self:
                dist = distance(self.position, boid.position)
                if dist < 3:
                    group.append(boid)
        

### Ansatz 2 (funktioniert nicht keine Ahnung warum)
        # for boid in boids:
        #     if sicht.entity == boid:
        #         if boid != self:
        #             group.append(boid)
        #         else:
        #             pass
        
        
        # if len(group) > 0:
        #     print(group)
###
        return group
    
    def zusammenfuegen(self):
        self.bewegen()
        neighbors = self.get_neighbors()
        self.wandVermeiden()
        if self.wand_colision == False:
            self.separation(neighbors)
            self.alignment(neighbors)


    def test(self):
        neue_position = Vec3(0,0,0)
        self.up += neue_position * self.speed/5
        self.position += self.up*(self.speed/1000) 
        
        print(self.position)

for i in range(boids_anzahl):
    x = randint(-9,9)
    y = randint(-9,9)
    z = randint(-19, 0)

    xr = randint(0,360)
    yr = randint(0,360)
    zr = randint(0,360)
    speed = 360
    grenze = 3
    variable = 1
    boids.append(Boid(i, x, y, z, xr, yr, zr, speed, grenze, variable))




def update():   # update gets automatically called.
    cameraUser()

    for boid in boids:
        boid.zusammenfuegen()
        if boid.x > 9:
            boid.x = -9
        if boid.x < -9:
            boid.x = 9

        if boid.y > 9:
            boid.y = -9
        if boid.y < -9:
            boid.y = 9

        if boid.z > -1:
            boid.z = -19
        if boid.z < -19:
            boid.z = -1 


app.run()   # opens a window and starts the game.
