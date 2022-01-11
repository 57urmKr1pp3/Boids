from ursina import *
import hit

def __testen__(tz,tx,ty2,tz2,wy,wz,wx,worldr,rotx,roty,speed,wert1,wert2):
    if ((tz2 < ty2) or ((5 < wy) or (wy < -5)) and (-5 < wz < 5)):
        if roty <= 180:
            if (rotx <= 180):
                if (wy <= -5 and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
            else:
                if (5 <= wy and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)   
        else:
            if (rotx <= 180):
                if (wy <= -5 and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
            else:
                if (5 <= wy and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(wert2,0,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(wert1,0,0),speed)                            
    else:
        if 0 < wx:
            if 0 < tx:
                if (5 < wz and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)
                elif (wz < -5 and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                elif 0 < tz:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)   
            else:
                if tz < 0:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed) 
                else:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)  
        else:
            if tx < 0:
                if (5 < wz and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)
                elif (wz < -5 and ((tx < 0 and wx < 0 ) or (0 < tx and 0 < wx))):
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                elif 0 < tz:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)
                else:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed)   
            else:
                if tz < 0:
                    return hit.__hit__(worldr,Vec3(0,wert1,0),speed) 
                else:
                    return hit.__hit__(worldr,Vec3(0,wert2,0),speed)  