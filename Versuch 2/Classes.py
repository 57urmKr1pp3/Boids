from pyexpat import model
from turtle import position
from ursina import *

class Boid (Entity):

    def __init__ (self, posX, posY, posZ, rotX, rotY, rotZ, mode, scale):
        super().__init__(model="\Sprites\sprites.blend", position = (posX, posY, posZ), rotation = (rotX, rotY, rotZ), color = color.random_color())