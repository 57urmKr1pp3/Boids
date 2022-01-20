#Imports
from ursina import *
from random import randint, uniform
from Classes import Boid

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
    w1 = Entity(model = 'cube', position = (0,0,-51),scale=(101,101,0.001), color = color.red, alpha = 0)
    w2 = Entity(model='cube', position = (0,0,51), scale = (101,101,0.001), color = color.red, alpha = 0)
    w3 = Entity(model='cube', position = (-51, 0,0), scale = (0.001, 101, 101), color = color.red, alpha = 0)
    w4 = Entity(model='cube', position = (51, 0,0), scale = (0.001, 101, 101), color = color.red, alpha = 0)
    w5 = Entity(model = 'cube', position = (0,-51,0), scale = (101,0.001,101), color = color.red, alpha = 0)
    w5 = Entity(model = 'cube', position = (0,51,0), scale = (101,0.001,101), color = color.red, alpha = 0)
def create_boids(anzahl):
    for i in range(anzahl):
        temp = Boid(randint(-10,10), randint(-10,10), randint(-10, 10), randint(0,360), randint(0,360), randint(0,360), uniform(0.0, 100.0), uniform(0.0, 10.0), 150.00, 2, groesse)
        Liste_Boids.append(temp)

def input(key):
    #https://www.ursinaengine.org/entity_basics.html 10.01.2022
    #10.01.2022
    if held_keys["+"]:
        temp = Boid(randint(-10,10), randint(-10,10), randint(-10, 10), randint(0,360), randint(0,360), randint(0,360), uniform(0.0, 100.0), uniform(0.0, 10.0), 150.00, 2, groesse)
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
groesse = 5
######################################################################################################################################

Liste_Boids = []
create_boids(anzahl)

app.run()