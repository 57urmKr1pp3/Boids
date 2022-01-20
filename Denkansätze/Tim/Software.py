
from ursina import *
from math import *
from random import *

import abfrage_l_r
import abfrage_f_b
import abfrage_u_d

# Anzahl Boids
BOIDZ = 1    
# Geschwindigkeit    
SPEED = 20 
# Schnelligkeit der Maus      
MAUSSCHNELLIGKEIT = 22.8

class Boid(Entity):
    def __init__(self, ID, x, y, z, xr, yr, zr, colors):
        super().__init__(model='cone.blend', position=(0,0,0), rotation=(-1,270,0), scale=(.2,.2,.2) , color=colors[randint(0,8)])# , collider = 'mesh'
        self.ID = ID
        
        # self.collider = BoxCollider(self, center=(0,0,17.5), size=(1,1,35))
        # self.collider.show() 
        
    def __update__(self):
        self.position += self.forward*(SPEED/1000)
        
    def __colorupdate__(self):
        if self.x <= 0:
            farbe_von_x = 10 - (self.x * -1)
            self.color = rgb(255,farbe_von_x*12.75,0)
        else:
            self.color = rgb(255,(self.x*12.75)+127.5,0)
             
        # if self.x < -7.15:
        #     self.color = color.red
        # elif self.x < -4.3:
        #     self.color = color.orange
        # elif self.x < -1.45:
        #     self.color = color.yellow
        # elif self.x < 1.45:
        #     self.color = color.green
        # elif self.x < 4.3:
        #     self.color = color.blue
        # elif self.x < 7.15:
        #     self.color = color.magenta
        # else:
        #     self.color = color.violet
            
    def __move__(self):
        hit_info_forward = raycast(origin=self.position, direction=self.forward, distance=7, debug=False, traverse_target=scene, ignore=(self, ))
        x1 = self.world_x
        y1 = self.world_y
        z1 = self.world_z
        
        self.__update__()
        self.__colorupdate__()
        
        x2 = self.world_x
        y2 = self.world_y
        z2 = self.world_z
        
        tempx = (x2-x1)
        tempy = (y2-y1)
        tempz = (z2-z1)
        if tempx < 0:
            tempx2 = tempx *-1
        else:
            tempx2 = tempx
        if tempy < 0:
            tempy2 = tempy *-1
        else:
            tempy2 = tempy
        if tempz < 0:
            tempz2 = tempz *-1
        else:
            tempz2 = tempz

        if not (0 < self.world_rotation_x <= 360):
            if self.world_rotation_x >= 360:
                self.world_rotation_x -= 360
            else:
                self.world_rotation_x += 360  
                
        if not (0 < self.world_rotation_y <= 360):
            if self.world_rotation_y >= 360:
                self.world_rotation_y -= 360
            else:
                self.world_rotation_y += 360  
                
        if not (0 < self.world_rotation_z <= 360):
            if self.world_rotation_z >= 360:
                self.world_rotation_z -= 360
            else:
                self.world_rotation_z += 360  
                
        if hit_info_forward.hit:
            frontD = raycast(origin=(self.position+(0,0,-.01)), direction=(0,0,-1) ,distance=30, debug=False, traverse_target=scene, ignore=(self, ))
            backD = raycast(origin=(self.position+(0,0,.01)), direction=(0,0,1) ,distance=30, debug=False, traverse_target=scene, ignore=(self, ))
            leftD = raycast(origin=(self.position+(-.01,0,0)), direction=(-1,0,0) ,distance=30, debug=False, traverse_target=scene, ignore=(self, ))
            rightD = raycast(origin=(self.position+(.01,0,0)), direction=(1,0,0), distance=30, debug=False, traverse_target=scene, ignore=(self, )) 
            upD = raycast(origin=(self.position+(0,.01,0)), direction=(0,1,0), distance=30, debug=False, traverse_target=scene, ignore=(self, )) 
            downD= raycast(origin=(self.position+(0,-.01,0)), direction=(0,-1,0), distance=30, debug=False, traverse_target=scene, ignore=(self, )) 
            
            try:
                d_f = distance(self.position,frontD.world_point)
                d_b = distance(self.position,backD.world_point)
                d_l = distance(self.position,leftD.world_point)
                d_r = distance(self.position,rightD.world_point)
                d_u = distance(self.position,upD.world_point)
                d_d = distance(self.position,downD.world_point)
                
                if ((d_u <= d_d) and (d_u <= d_r) and (d_u <= d_l) and (d_u <= d_f) and (d_u <= d_b)):
                    self.world_rotation = abfrage_u_d.__testen__(self.world_z,self.world_x, self.world_rotation, self.world_rotation_x, self.world_rotation_y,SPEED,.01*SPEED,-.01*SPEED)
                        
                elif ((d_d <= d_u) and (d_d <= d_r) and (d_d <= d_l) and (d_d <= d_f) and (d_d <= d_b)):
                    self.world_rotation = abfrage_u_d.__testen__(self.world_z,self.world_x, self.world_rotation, self.world_rotation_x, self.world_rotation_y,SPEED,-.01*SPEED,.01*SPEED)
                            
                #---------------------------------------------------------------------------------------            
                            
                elif ((d_l <= d_u) and (d_l <= d_r) and (d_l <= d_d) and (d_l <= d_f) and (d_l <= d_b)):
                    self.world_rotation = abfrage_l_r.__testen__(tempz,tempx,tempy2,tempz2,self.world_y,self.world_z,self.world_x,self.world_rotation,self.world_rotation_x,self.world_rotation_y,SPEED,-.01*SPEED,.01*SPEED)
                            
                elif ((d_r <= d_u) and (d_r <= d_l) and (d_r <= d_d) and (d_r <= d_f) and (d_r <= d_b)):
                    self.world_rotation = abfrage_l_r.__testen__(tempz,tempx,tempy2,tempz2,self.world_y,self.world_z,self.world_x,self.world_rotation,self.world_rotation_x,self.world_rotation_y,SPEED,.01*SPEED,-.01*SPEED)
                                
                #---------------------------------------------------------------------------------------   
                                
                elif ((d_f <= d_u) and (d_f <= d_l) and (d_f <= d_d) and (d_f <= d_r) and (d_f <= d_b)):
                    self.world_rotation = abfrage_f_b.__testen__(tempz,tempx,tempy,tempy2,tempx2,tempz2,self.world_y,self.world_x,self.world_z,self.world_rotation,self.world_rotation_x,self.world_rotation_y,SPEED,.01*SPEED,-.01*SPEED)
                
                elif ((d_b <= d_u) and (d_b <= d_l) and (d_b <= d_d) and (d_b <= d_r) and (d_b <= d_f)):
                    self.world_rotation = abfrage_f_b.__testen__(tempz,tempx,tempy,tempy2,tempx2,tempz2,self.world_y,self.world_x,self.world_z,self.world_rotation,self.world_rotation_x,self.world_rotation_y,SPEED,-.01*SPEED,.01*SPEED)
                                
            except TypeError:
                pass
            
# -----Funktionen-----
            
def create1():
    return Entity(model='cube', color=color.black, scale=(0.1,20,0.1), alpha=180)
def create2():
    return Entity(model='cube', color=color.black, scale=(20,0.1,0.1), alpha=180)
def create3():
    return Entity(model='cube', color=color.black, scale=(0.1,0.1,20), alpha=180)

def einstellungen():
    close.enabled = not close.enabled
    controls.enabled = not controls.enabled
    settings.visible = not settings.visible
    settings2.visible = not settings2.visible
    back.enabled = not back.enabled
    if window.fullscreen == True:
        bgon.enabled = True
        bgoff.enabled = False
    else:
        bgon.enabled = False
        bgoff.enabled = True
    if window.fps_counter.enabled == True:
        fpson.enabled = True
        fpsoff.enabled = False
    else:
        fpson.enabled = False
        fpsoff.enabled = True
    if settings2.visible == False:
        bgon.enabled = False
        bgoff.enabled = False
        fpson.enabled = False
        fpsoff.enabled = False
    
def escape():
    window.exit_button.visible = not window.exit_button.visible
    mouse.visible = not mouse.visible
    mouse.position = (0,0,0)
    mouse.locked = not mouse.locked
    menue.visible = not menue.visible
    settings.visible = not settings.visible
    close.enabled = not close.enabled
    controls.enabled = not controls.enabled
    cursor.visible = not cursor.visible

   
    if window.exit_button.visible == False:
        cursor.visible = True
        close.enabled = False
        controls.enabled = False
        settings.visible = False
        settings2.visible = False
        menue.visible = False
        back.enabled = False
        bgon.enabled = False
        bgoff.enabled = False
        fpson.enabled = False
        fpsoff.enabled = False
    
def changebg():
    bgon.enabled = not bgon.enabled
    bgoff.enabled = not bgoff.enabled
    if bgon.enabled == True:
        window.fullscreen = True
    else:
        window.fullscreen = False
        
def changefps():
    fpson.enabled = not fpson.enabled
    fpsoff.enabled = not fpsoff.enabled
    if fpson.enabled == True:
        window.fps_counter.enabled = True
    else:
        window.fps_counter.enabled = False
    
def __camera__():
    if window.exit_button.visible == False:
        if held_keys['w']:
            cameraE.rotation = camera.rotation
            cameraE.position += cameraE.forward * .03*SPEED
            camera.position = cameraE.position
        if held_keys['s']:
            cameraE.rotation = camera.rotation
            cameraE.position += cameraE.back * .03*SPEED
            camera.position = cameraE.position
            
        if held_keys['d']:
            cameraE.rotation = camera.rotation
            cameraE.position += cameraE.right * .03*SPEED
            camera.position = cameraE.position
        if held_keys['a']:
            cameraE.rotation = camera.rotation
            cameraE.position += cameraE.left * .03*SPEED
            camera.position = cameraE.position
            
        if held_keys['left shift']:
            cameraE.position += cameraE.up*.5  * .03*SPEED
            camera.position = cameraE.position
        if held_keys['left control']:
            cameraE.position += cameraE.down*.5 * .03*SPEED
            camera.position = cameraE.position
        if held_keys['q']:        
            cameraE.rotation_y -= 1  * .006*SPEED
            camera.rotation = cameraE.rotation        
        if held_keys['e']:                               
            cameraE.rotation_y += 1  * .006*SPEED
            camera.rotation = cameraE.rotation  
            
        if mouse.left == False and mouse.visible == False:
            if not(90 < camera.rotation_x < 270):
                camera.rotation_x += mouse.y*-MAUSSCHNELLIGKEIT
            elif 90 < camera.rotation_x < 130:
                camera.rotation_x = 90
            else:
                camera.rotation_x = 270         
            camera.rotation_y += mouse.x*MAUSSCHNELLIGKEIT  
            
        if not (0 < camera.rotation_x <= 360):
            if camera.rotation_x >= 360:
                camera.rotation_x -= 360
            else:
                camera.rotation_x += 360  
                
        if not (0 < camera.rotation_y <= 360):
            if camera.rotation_y >= 360:
                camera.rotation_y -= 360
            else:
                camera.rotation_y += 360  
 
        # arrow.rotation_x = camera.rotation_x*-1 
        # arrow.rotation_y = camera.rotation_y*-1 
        # arrow_raender.rotation_x = camera.rotation_x*-1
        # arrow_raender.rotation_y = camera.rotation_y*-1
        
def denkansatz_Pfeil():
    if camera.x < camera.z: # Winkel ist < 45°
        if camera.z < 0:
            
            pass
        else:
            pass
    if camera.x > camera.z: #
        pass 
   
def update():   
    __camera__()
    for i in boids:
        i.__move__()           
        
def input(key):
    menue.rotation = camera.rotation
    if key == 'alt' and window.exit_button.visible == False:
        mouse.visible = not mouse.visible
        mouse.locked = not mouse.locked
        mouse.position = (0,0,0)
    if key == 'escape':
        window.exit_button.visible = not window.exit_button.visible
        if window.exit_button.visible == True:
            if mouse.visible == True:
                mouse.visible = False
            if mouse.locked == False:
                mouse.locked = True
            window.exit_button.visible = not window.exit_button.visible
            menue.position = [camera.world_x,camera.world_y,camera.world_z+1]
            escape()    

        if window.exit_button.visible == False:
            window.exit_button.visible = not window.exit_button.visible
            escape()

if __name__ == '__main__':
    app = Ursina()
    
    cursor = Entity(parent=camera.ui, model='cursor.blend', color=color.gray, scale=.008, rotation_z=45)
    window.title = 'Boids'
    window.borderless = False
    window.exit_button.visible = False
    window.fps_counter.enabled = True
    mouse.visible = False
    mouse.locked = True

    settings = Text(text=dedent('''\n\n<scale:2.5><orange>                           Menu                            \n\n\n\n\n\n\n\n'''), origin=(0,0), background = True)
    settings2 = Text(text=dedent('''\n\n<scale:2.5><orange>                           Menu                            
                                \n<scale:1><white>Show FPS:                                             
                                \n<scale:1><white>Fullscreen:                                             \n\n\n\n'''), origin=(0,0), background = True)

    menue = Entity(model='cube', color=color.black, scale=(1000,1000,0.2), alpha=150)
    w_vorne =  Entity(model='cube', color=color.black, scale=(20,20,0.1), alpha=100, position=(0,0,-10), collider = 'box')
    w_hinten = Entity(model='cube', color=color.black, scale=(20,20,0.1), alpha=100, position=(0,0,10), collider = 'box')
    w_unten =  Entity(model='cube', color=color.black, scale=(20,0.1,20), alpha=100, position=(0,-10,0), collider = 'box')
    w_oben =   Entity(model='cube', color=color.black, scale=(20,0.1,20), alpha=100, position=(0,10,0), collider = 'box')
    w_rechts = Entity(model='cube', color=color.black, scale=(0.1,20,20), alpha=100, position=(10,0,0), collider = 'box')
    w_links =  Entity(model='cube', color=color.black, scale=(0.1,20,20), alpha=100, position=(-10,0,0), collider = 'box')
    cameraE =  Entity(model='cube', scale=(0.1,0.1,0.1), alpha=100, position=(0,0,-50), visible=False)
    
    # arrow = Entity(parent=(camera.ui), model='arrow.blend', position=(0,.38,0) ,color=color.gray, scale=.08, rotation = cameraE.rotation*-1)
    # arrow_raender = Entity(parent=(camera.ui), model='arrow_raender.blend', position=(0,.38,0) ,color=color.black, scale=.08, rotation = cameraE.rotation*-1)

    colors = [color.red,color.orange,color.yellow,color.green,color.turquoise,color.cyan,color.blue,color.violet,color.pink]
    boids = []
            
    for i in range(BOIDZ):
        x = randint(-7,7)
        y = randint(-7,7)
        z = randint(-7,7)
        
        xr = randint(0,359)
        yr = randint(0,359)
        zr = randint(0,359)
        boids.append(Boid(i, x, y, z, xr, yr, zr, colors))
        
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

    raster_vorn_links.position = (-10,0,10)
    raster_vorn_rechts.position = (10,0,10)
    raster_hinten_links.position = (-10,0,-10)
    raster_hinten_rechts.position = (10,0,-10)
    raster_vorn_oben.position = (0,10,10)
    raster_vorn_unten.position = (0,-10,10)
    raster_hinten_oben.position = (0,10,-10)
    raster_hinten_unten.position = (0,-10,-10)
    raster_oben_links.position = (-10,10,0)
    raster_oben_rechts.position = (10,10,0)
    raster_unten_links.position = (-10,-10,0)
    raster_unten_rechts.position = (10,-10,0)

    menue.z -= 50
    camera.position = cameraE.position
    menue.visible = False
    settings.visible = False
    settings2.visible = False
        
    close = Button(text=' Close ', color=color.gray, scale=.1, text_origin=(0,0), position=(0,-0.1,0), enabled=False)
    close.fit_to_text(radius=.1)
    controls = Button(text='Controls', color=color.gray, scale=.1, text_origin=(0,0), position=(0,-0.03,0), enabled=False)
    controls.fit_to_text(radius=.1)
    back = Button(text='Back', color=color.gray, scale=.1, text_origin=(0,0), position=(0,-0.1,0), enabled=False)
    back.fit_to_text(radius=.1)
    bgon = Button(text=' On ', color=color.gray, scale=.1, text_origin=(0,0), position=(0.1,-0.04,0), enabled=False)
    bgon.fit_to_text(radius=.1)
    bgoff = Button(text=' Off ', color=color.gray, scale=.1, text_origin=(0,0), position=(0.1,-0.04,0), enabled=False)
    bgoff.fit_to_text(radius=.1)
    fpson = Button(text=' On ', color=color.gray, scale=.1, text_origin=(0,0), position=(0.1,0.01,0), enabled=False)
    fpson.fit_to_text(radius=.1)
    fpsoff = Button(text=' Off ', color=color.gray, scale=.1, text_origin=(0,0), position=(0.1,0.01,0), enabled=False)
    fpsoff.fit_to_text(radius=.1)

    close.on_click = escape
    controls.on_click = einstellungen
    back.on_click = einstellungen
    bgon.on_click = changebg
    bgoff.on_click = changebg
    fpson.on_click = changefps
    fpsoff.on_click = changefps
        
    app.run()   # opens a window and starts the game.