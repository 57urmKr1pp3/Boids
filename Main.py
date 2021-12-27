from Boids import Boid
from ursina import *
from random import randint

def adaptDir(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)):
            difPos = [0, 0 ,0]
            difPos[0] = Liste_Boids[i].getPos()[0] - Liste_Boids[j].getPos()[0]
            difPos[1] = Liste_Boids[i].getPos()[1] - Liste_Boids[j].getPos()[1]
            difPos[2] = Liste_Boids[i].getPos()[2] - Liste_Boids[j].getPos()[2]
            if difPos[0] < 5 and difPos[0] > -5 and difPos[1] < 5 and difPos[1] > -5 and difPos[2] < 5 and difPos[2] > -5:
                averageDir = [0, 0, 0]
                averageDir[0] = (Liste_Boids[i].getPos()[0] + Liste_Boids[j].getPos()[0]) / 2
                averageDir[1] = (Liste_Boids[i].getPos()[1] + Liste_Boids[j].getPos()[1]) / 2
                averageDir[2] = (Liste_Boids[i].getPos()[2] + Liste_Boids[j].getPos()[2]) / 2
                Liste_Boids[i].setDir(averageDir)
                Liste_Boids[j].setDir(averageDir)

def checkPos(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(len(Liste_Boids)-1):
            if Liste_Boids[i].getPos() == Liste_Boids[j].getPos():
                nPos=(Liste_Boids[i].getPos()[0] + 5, Liste_Boids[i].getPos()[1] + 5, Liste_Boids[i].getPos()[2] + 5)
                Liste_Boids[i].setPos(nPos)
            
