from ursina import *

def __hit__(worldr,dir,speed):
        worldr += dir * .1*speed
        return worldr