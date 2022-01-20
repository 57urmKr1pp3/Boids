from ursina import *
import hit

def __testen__(wz,wx,worldr,rotx,roty,speed,wert1,wert2):
    if ((-5 < wz < 5) or (-5 < wx < 5)): 
        if (((rotx <= 90) or (270 <= rotx)) and (90 <= roty <= 270)):
            return hit.__hit__(worldr,Vec3(wert1,0,0),speed) 
        elif (((90 <= rotx <= 270) and ((roty <= 90) or (270 <= roty))) or ((90 <= rotx <= 270) and (90 <= roty <= 270))):
            return hit.__hit__(worldr,Vec3(wert2,0,0),speed)                            
        else:                                                             
            return hit.__hit__(worldr,Vec3(wert1,0,0),speed)                          
    else:
        if 90 < rotx < 270:
            return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
        else:
            return hit.__hit__(worldr,Vec3(wert1,0,0),speed)