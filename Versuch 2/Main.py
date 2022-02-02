#Imports
from ursina import *
from random import randint, uniform


class Boid (Entity):

    def __init__ (self, posX, posY, posZ, rotX, rotY, rotZ, vel, acel, maxVel, mode, scale):
        super().__init__(model="sprites.blend", position = (posX, posY, posZ), rotation = (rotX, rotY, rotZ), color = color.random_color(), scale = scale)
        self.x = posX
        self.y = posY
        self.z = posZ
        self.vel = vel
        self.acel = acel
        self.maxVel = maxVel
        self.mode = mode
        self.collider = 'box'

    #Getter 
    #geben die Werte der Eigenschaften zurück
    def getModel(self):
        return self.model

    def getPosition(self):
        return self.position

    def getRotation(self):
        return self.rotation

    def getColor(self):
        return self.color
    
    def getScale(self):
        return self.scale
    
    def getVel(self):
        return self.vel

    def getAcel(self):
        return self.acel

    def getMaxVel(self):
        return self.maxVel

    def getMode(self):
        return self.mode

    def getCollider(self):
        return self.collider
    
    #Setter 
    #übeschreiben die Eigenschaften mit neuen Werten
    def setPosition(self, posX, posY, posZ):
        self.position = (posX, posY, posZ)
    
    def setModel(self, nModel):
        self.model = nModel
    
    def setRotation(self, rotX, rotY, rotZ):
        self.rotation = (rotX, rotY, rotZ)

    def setScale(self, nScale):
        self.scale = nScale
    
    def setVel(self, nVel):
        self.vel = nVel
    
    def setAcel(self, nAcel):
        self.acel = nAcel
    
    def setMaxVel(self, nMaxVel):
        self.maxVel = nMaxVel
    
    def setMode(self, nMode):
        self.mode = nMode

    def setCollider(self, nCollider):
        self.collider = nCollider

    #Bewegung
    def updateVel(self):
        #Die Geschwindigkeit wird durch Addition der Beschleunigung so lange erhöht bis sie das Maximum erreicht hat
        if self.vel < self.maxVel:
            self.vel += self.acel

    def closeBoids(self):
        #Diese Funktion ist dazu da um die Boids in der Nähe zu erfassen
        close = []
        #Dafür wird die Liste benutzt, die bei der Erstellung der Boids befüllt wird
        #jeder Boid außer man selbst wird in dieser for-Schleife durchgegangen
        for i in Liste_Boids:
            if i != self:
                #wenn die Distanz zwischen dem self.Boid und dem zu vergleichenden Boid unter 5 liegt wird der vergleichende Boid in die Liste mit den Boids in der Nähe hinzugefügt
                distanceBoids = distance(self.position, i.position)
                if distanceBoids < 5:
                    close.append(i)
        return close

    def alignment(self):
        #Die Boids in der Nähe werden zwischengespeichert
        proximity = self.closeBoids()
        #Die einzelnen Rotationswerte und die Geschwindigkeitswerte des self.Boids werden hier gespeichert
        Boid1XR = self.rotation_x
        Boid1YR = self.rotation_y
        Boid1ZR = self.rotation_z
        Boid1V = self.vel
        Boid1MV = self.maxVel
        Boid1A = self.acel
        for i in proximity: # für jeden Boid in der Nähe wird das Alignment-Verfahren durchgegangen
            #Rotations und Geschwindikeitswerte des zu vergleichenden Boids zwischengespeichert
            Boid2XR = i.rotation_x
            Boid2YR = i.rotation_y
            Boid2ZR = i.rotation_z
            Boid2V = i.vel
            Boid2MV = i.maxVel
            Boid2A = i.acel
            #Die Durchschnitte der einzelnen Werte werden hier berechnet
            avgXR = (Boid1XR + Boid2XR)/2
            avgYR = (Boid1YR + Boid2YR)/2
            avgZR = (Boid1ZR + Boid2ZR)/2
            avgV = (Boid1V + Boid2V)/2
            avgMV = (Boid1MV + Boid2MV)/2
            avgA = (Boid1A + Boid2A)/2
            #Die Durchschnittswerte überschreiben die Rotations und Geschwindigkeitswerte des self.Boid
            self.rotation_x = avgXR
            self.rotation_y = avgYR
            self.rotation_z = avgZR
            self.vel = avgV
            self.maxVel = avgMV
            self.acel = avgA

    def seperation(self):
        # proximity = self.closeBoids()
        # for i in proximity:
        #     if distance(self.position, i.position) < 2:
        #         self.position -= Vec3(i.position + self.position)
        #Versuch 1
        #ProxPos = []
        #for i in proximity:
        #    ProxPos.append(i.position)
        #try:
        #    center = sum(ProxPos)/len(ProxPos)
        #    if distance(self.position, center) < 1:
        #        self.position -= Vec3(self.up + Vec3(Vec3(center - self.position)-self.up))
        #except:
        #    pass

        #Versuch 2
        #Die Boids in der Nähe werden zwischengespeichert
        proximity = self.closeBoids()
        if len(proximity) > 1:
            for i in proximity:
                #wenn die Distanz zwischen dem self.Boid und des zu vergeichenden Boids <2 ist wird die Mitte zwischen den beiden Boids berechnet
                if distance(self.position, i.position) < 2:
                    center = (self.position + i.position)/2
                    #Die Differenz zwischen der Mitte und der eigenen Position wird von der Position subtrahiert um den Abstand zu erhöhen
                    self.position -= Vec3(center - self.position) * .05

    def cohesion(self):
        #Versuch 1
        #ProxPos = []
        #for i in proximity:
        #    ProxPos.append(i.position)
        #try:
        #    center = sum(ProxPos)/len(ProxPos)
        #    if distance(self.position, center) >= 2:
        #        self.position += Vec3(self.up + Vec3(Vec3(center - self.position)-self.up))
        #except:
        #    pass
        #Versuch 2
        #Die Boids in der Nähe werden gespeichert
        proximity = self.closeBoids()
        #Die Mitte aller Boids in der Nähe wird berechnet
        center = self.position
        if len(proximity) > 1:
            for i in proximity:
                center = (center + i.position)/2
        #falls die Distanz des Boids zu der Mitte groß genug ist wird der Abstand zur Mitte der Position hinzugefügt
        #damit die Boids immer in die Mitte des Flocks ziehen
        if distance(self.position, center) >= 2:
            self.position += Vec3(center - self.position) * .05



    def avoidWall(self):
        #Raycasts
        #Ein Raycast wird erzeugt der in die Bewegungsrichtung 5 Einheiten weit ausgerchtet ist 
        raycastup = raycast(origin = self.position, direction = self.up, distance = 5, traverse_target = scene, ignore = (self,), debug = True)
        #Wenn dieser Raycast etwas berührt werden weitere Raycast erstellt, die in 4 weitere Richtungen ausgerichtet sind
        if raycastup.hit:
            raycastfront = raycast(origin = self.position, direction = (self.up + self.forward), distance = 10, traverse_target = scene, ignore = (self,), debug = True)
            raycastback = raycast(origin = self.position, direction = (self.up + self.back), distance = 10, traverse_target = scene, ignore = (self,), debug = True)
            raycastleft = raycast(origin = self.position, direction = (self.up + self.left), distance = 10, traverse_target = scene, ignore = (self,), debug = True)
            raycastright = raycast(origin = self.position, direction = (self.up + self.right), distance = 10, traverse_target = scene, ignore = (self,), debug = True)
            #Die Distanz zu dem getroffenen Objektes von jedem Raycast wird gespeichert
            distance_up = raycastup.distance
            distance_front = raycastfront.distance
            distance_back = raycastback.distance
            distance_left = raycastleft.distance
            distance_right = raycastright.distance
            
            #je nach kleinster Distanz werden verschiedene Rotationsänderung durchgeführt
            #up kleinste Distanz
            if (distance_up <= distance_front) and (distance_up <= distance_back) and (distance_up <= distance_left) and (distance_up <= distance_right):
                self.rotation += self.back * self.vel

            #front kleinste Distanz
            if (distance_front <= distance_up) and (distance_front <= distance_back) and (distance_front <= distance_right) and (distance_up <= distance_left):
                self.rotation += self.back * self.vel

            #back kleinste Distanz
            if (distance_back <= distance_up) and (distance_back <= distance_front) and (distance_back <= distance_right) and (distance_back <= distance_left):
                self.rotation += self.forward * self.vel

            #left kleinste Distanz
            if (distance_left <= distance_up) and (distance_left <= distance_right) and (distance_left <= distance_back) and (distance_left <= distance_front):
                self.rotation += self.right * self.vel

            #right kleinste Distanz
            if (distance_right <= distance_left) and (distance_right <= distance_up) and (distance_right <= distance_front) and (distance_right <= distance_back):
                self.rotation += self.left * self.vel
            
    def move(self):
        #Die Posiiton wird durch Multiplikation der Geschwindigkeit und der Bewegungsrichtung verändert
        #Die Bewegungsrichtung ist hier up/hoch, da die Modeldatei danach ausgerichtet ist
        self.position += self.up * (self.vel/1000)
        self.updateVel()
        #Warp Modus

        if self.mode == 1:
            #falls die Position des Boids nach der Bewegung die der Wände überschreiten wird die Position auf die gegenüberliegende Seite gesetzt
            if self.x <= -49:
                self.x = 48
            if self.x >= 49:
                self.x = -48
            if self.y <= -49:
                self.y = 48
            if self.y >= 49:
                self.y = -48
            if self.z <= -49:
                self.z = 48
            if self.z >= 49:
                self.z = -48

        #Wändevermeidung
        elif self.mode == 2:
            #Funktion zur Wändevermeidung wird aufgerufen
            self.avoidWall()

        #Pong-Modus
        elif self.mode == 3:
            #bei Überschreitung des Bereichs soll die Rotation verändert werden
            #Problem: Rotationsordnung ist zu spezifisch sodass man es nicht allgemein verfassen kann
            #         ebenfalls funktioniert die Rechnung: Rotation*-1-180 nicht wegen ^
            if self.x <= -49:
                self.rotation_y = -self.rotation_y
            if self.x >= 49:
                self.rotation_y = -self.rotation_y
            if self.y <= -49:
                self.rotation_z = -self.rotation_z
            if self.y >= 49:
                self.rotation_z = -self.rotation_z
            if self.z <= -49:
                self.rotation_z = -self.rotation_z
            if self.z >= 49:
                self.rotation_z = -self.rotation_z

    def update(self):
        #Funktion zur Bewegung wird aufgerufen
        self.move()
        #Funktion zur Einhaltung der Regeln werden aufgerufen
        self.alignment()
        self.seperation()
        self.cohesion()

def createWireframe():
    #05.01.2022
    #Wireframe
    #Erzeugung des Würfels
    wf1 = Entity(model = "cube", collider = 'box', position = (0, -51, -51), scale_x = 102)
    wf2 = Entity(model = "cube", collider = 'box', position = (-51, -51, 0), scale_z = 102)
    wf3 = Entity(model = "cube", collider = 'box', position = (0, -51, 51), scale_x = 102)
    wf4 = Entity(model = "cube", collider = 'box', position = (51, -51, 0), scale_z = 102)
    wf5 = Entity(model = "cube", collider = 'box', position = (51, 0, 51), scale_y = 102)
    wf6 = Entity(model = "cube", collider = 'box', position = (51, 0, -51), scale_y = -102)
    wf7 = Entity(model = "cube", collider = 'box', position = (-51, 0, 51), scale_y = 102)
    wf8 = Entity(model = "cube", collider = 'box', position = (-51, 0, -51), scale_y = 102)
    wf9 = Entity(model = "cube", collider = 'box', position = (-51, 51, 0), scale_z = -102)
    wf10 = Entity(model = "cube", collider = 'box', position =(0, 51, 51), scale_x = -102)
    wf11 = Entity(model = "cube", collider = 'box', position =(51, 51, 0), scale_z = 102)
    wf12 = Entity(model = "cube", collider = 'box', position =(0, 51, -51), scale_x = -102)
    w1 = Entity(model = 'cube', collider = 'box', position = (0,0,-52),scale=(101,101,0), color = color.red, alpha = 0)
    w2 = Entity(model='cube', collider = 'box', position = (0,0,52), scale = (101,101,0), color = color.red, alpha = 0)
    w3 = Entity(model='cube', collider = 'box', position = (-52, 0,0), scale = (0, 101, 101), color = color.red, alpha = 0)
    w4 = Entity(model='cube', collider = 'box', position = (52, 0,0), scale = (0, 101, 101), color = color.red, alpha = 0)
    w5 = Entity(model = 'cube', collider = 'box', position = (0,-52,0), scale = (101,0,101), color = color.red, alpha = 0)
    w5 = Entity(model = 'cube', collider = 'box', position = (0,52,0), scale = (101,0,101), color = color.red, alpha = 0)

def createBoids(anzahl):
    #Boids werden erstellt und in der Liste gespeichert
    for i in range(anzahl):
        temp = Boid(randint(-30,30), randint(-30,30), randint(-30, 30), randint(0,360), randint(0,360), randint(0,360), uniform(0.0, 100.0), uniform(0.0, 10.0), 300.0, 1, groesse)
        Liste_Boids.append(temp)

def input(key):
    #https://www.ursinaengine.org/entity_basics.html 10.01.2022
    #10.01.2022
    if held_keys["+"]:
        #Boid wird erstellt und der Liste hinzugefügt
        temp = Boid(randint(-30,30), randint(-30,30), randint(-30, 30), randint(0,360), randint(0,360), randint(0,360), uniform(50.0, 300.0), uniform(0.0, 10.0), 300.0, 1, groesse)
        Liste_Boids.append(temp)

    if held_keys["-"]:
        #Der letzte Boid wird deaktiviert um ihn nicht mehr zu sehen
        Liste_Boids[len(Liste_Boids)-1].disable()
        #letzter Boid wird aus der Liste entfernt
        Liste_Boids.pop()

    #Der Modus jedes Boids wird geändert
    if held_keys["1"]:
        for i in Liste_Boids:
            i.setMode(1)
    if held_keys["2"]:
        for i in Liste_Boids:
            i.setMode(2)
    if held_keys["3"]:
        for i in Liste_Boids:
            i.setMode(3)

def createInstruction():
    #https://www.youtube.com/watch?v=kb2wJYTwTHw 15.01.2022
    #Anleitung wird erstellt
    text_Beschreibung = '''Kamera drehen:
                            \nRechtsklick + Mausbewegen
                            \n\nZoom: Mausrad
                            \n\nKamerabewegen:
                            \nRechtsklick +
                            \nrechts:                      [A]
                            \nlinks:                         [D]
                            \nvorwärts:                 [W]
                            \nrückwärts:                [S]
                            \nhoch:                         [E]
                            \nrunter:                      [Q]
                            \n\nBoidanzahl ändern:
                            \nmehr:                        [+]
                            \nweniger:                    [-]
                            \n\nBoidverhalten:
                            \nWarp:                         [1]
                            \nWaende vermeiden [2]
                            \nAbprallen:                 [3]


                        '''
    #Textobjekt wird erstellt, skaliert und positioniert
    beschreibung = Text(text_Beschreibung, line_height = 0.5, scale = 0.7, x = -.8, y = -.12, color = color.white)

#Anwendung 
#https://www.ursinaengine.org/cheat_sheet.html#window 28.12.2021
#Fenster wird erstellt
app = Ursina()

#Fenster
#Fenstertitel wird festgelegt
window.title = "Boids Simulation"

#Kamera
#https://www.ursinaengine.org/cheat_sheet.html#camera 30.12.2021
#Kameraposition wird verändert um den Bereich von Anfang an zu sehen
camera.position = (0,10,-350)
#EditorCamera ermöglicht die Veränderung der Kamera
EditorCamera()

#Erstellen
#Wireframe
createWireframe()
#Anleitung
createInstruction()
#Boids
######################################################################################################################################
anzahl = 25
groesse = 30
######################################################################################################################################

Liste_Boids = []
createBoids(anzahl)

#Fenster wird ausgeführt
app.run()