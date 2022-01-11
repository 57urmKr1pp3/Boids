from ursina import *
import hit

def __testen__(tz,tx,ty,ty2,tx2,tz2,wy,wx,wz,worldr,rotx,roty,speed,wert1,wert2):
    if ((tx2 < ty2) or ((5 < wy) or (wy < -5)) and (-5 < wx < 5)):
        if 90 <= roty < 270:
            if (rotx <= 180):
                if (wy <= -5 and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
            else:
                if (5 <= wy and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)   
        else:
            if (rotx <= 180):
                if (wy <= -5 and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
            else:
                if (5 <= wy and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)                     
    else:
        if 0 < wz: 
            if tz < 0 :
                if (5 < wx and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                elif (wx < -5 and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)
                elif 0 < tx:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)   
            else:
                if tx < 0:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed) 
                else:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
        else:
            if 0 < tz:
                if (5 < wx and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                elif (wx < -5 and ((tz < 0 and wz < 0 ) or (0 < tz and 0 < wz))):
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)
                elif 0 < tx:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)   
            else:
                if tx < 0:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed) 
                else:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)