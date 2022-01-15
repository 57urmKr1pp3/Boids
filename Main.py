#Imports
from ursina import *
from random import randint
from Classes import Boid

#Funktionen
def eigenschaften(Liste_Boids):
    for i in range(len(Liste_Boids)-1):
        for j in range(i, len(Liste_Boids)-1):
            difX = Liste_Boids[i].x - Liste_Boids[j].x
            difY = Liste_Boids[i].y - Liste_Boids[j].y
            difZ = Liste_Boids[i].z - Liste_Boids[j].z
            if difX < 6.5 and difX > 6.5 and difY < 6.5 and difY > -6.5 and difZ < 6.5 and difZ > -6.5:
                print("True")
                Boid1X = Liste_Boids[i].x + .5
                Boid1Y = Liste_Boids[i].y + .5
                Boid1Z = Liste_Boids[i].z + .5
                Liste_Boids[i].setPosition(Boid1X, Boid1Y, Boid1Z)

            if (difX < 30 and difX > 30) or (difY < 30 and difY > -30) or (difZ < 30 and difZ > -30):
                Boid1dirX = Liste_Boids[i].directionX
                Boid1dirY = Liste_Boids[i].directionY
                Boid1dirZ = Liste_Boids[i].directionZ
                Boid2dirX = Liste_Boids[j].directionX
                Boid2dirY = Liste_Boids[j].directionY
                Boid2dirZ = Liste_Boids[j].directionZ
                avDirX = (Boid1dirX + Boid2dirX)/2
                avDirY = (Boid1dirY + Boid2dirY)/2
                avDirZ = (Boid1dirZ + Boid2dirZ)/2
                Liste_Boids[i].setDirectionX = avDirX
                Liste_Boids[i].setDirectionY = avDirY
                Liste_Boids[i].setDirectionZ = avDirZ

def create_wireframe():
    #05.01.2022
    #Wireframe
    wf1 = Entity(model = "cube", position = (0, -51, -51), scale_x = 102)
    wf2 = Entity(model = "cube", position = (-51, -51, 0), scale_z = 102)
    wf3 = Entity(model = "cube", position = (0, -51, 51), scale_x = 102)
    wf4 = Entity(model = "cube", position = (51, -51, 0), scale_z = 102)
    wf5 = Entity(model = "cube", position = (51, 0, 51), scale_y = 102)
    wf6 = Entity(model = "cube", position = (51, 0, -51), scale_y = -102)
    wf7 = Entity(model = "cube", position = (-51, 0, 51), scale_y = 102)
    wf8 = Entity(model = "cube", position = (-51, 0, -51), scale_y = 102)
    wf9 = Entity(model = "cube", position = (-51, 51, 0), scale_z = -102)
    wf10 = Entity(model = "cube", position =(0, 51, 51), scale_x = -102)
    wf11 = Entity(model = "cube", position =(51, 51, 0), scale_z = 102)
    wf12 = Entity(model = "cube", position =(0, 51, -51), scale_x = -102)
    

def create_boids(anzahl, liste):
    #Erstellen und speichern der Boids in einer Liste
    #05.01.2022
    for i in range(anzahl):
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), 1, 15)
        Liste_Boids.append(temp)

def update():
    #https://www.ursinaengine.org/entity_basics.html 10.01.2022
    eigenschaften(Liste_Boids)

def input(key):
    #https://www.ursinaengine.org/entity_basics.html 10.01.2022
    #10.01.2022
    if held_keys["+"]:
        temp = Boid(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), 1, 15)
        Liste_Boids.append(temp)
    if held_keys["-"]:
        Liste_Boids[len(Liste_Boids)-1].disable()
        Liste_Boids.pop()
    if held_keys["1"]:
        for i in Liste_Boids:
            i.setMode(1)
    if held_keys["2"]:
        for i in Liste_Boids:
            i.setMode(2)

def create_instruction():
    #https://www.youtube.com/watch?v=kb2wJYTwTHw 15.01.2022
    text_Beschreibung = '''Kamera drehen:
                            \nRechtsklick + Mausbewegen
                            \n\nKamerabewegen:
                            \nRechtsklick +
                            \nrechts:                [A]
                            \nlinks:                   [D]
                            \nvorwärts:           [W]
                            \nrückwärts:          [S]
                            \nhoch:                   [E]
                            \nrunter:                [Q]
                            \n\nBoidanzahl ändern:
                            \nmehr:                  [+]
                            \nweniger:              [-]
                            \n\nBoidverhalten:
                            \nAbprallen:           [1]
                            \nWarp:                   [2]


                        '''
    beschreibung = Text(text_Beschreibung, line_height = 0.5, scale = 0.7, x = -.8, y = -.12, color = color.white)

#Anwendung 
#https://www.ursinaengine.org/cheat_sheet.html#window 28.12.2021
app = Ursina()

#Fenster
window.title = "Boids Simulation"

#Kamera
#https://www.ursinaengine.org/cheat_sheet.html#camera 30.12.2021
camera.position = (0,10,-350)
EditorCamera()

#Erstellen
#Wireframe
create_wireframe()
create_instruction()
#Boids
######################################################################################################################################
anzahl = 2
######################################################################################################################################

Liste_Boids = []
create_boids(anzahl, Liste_Boids)

app.run()