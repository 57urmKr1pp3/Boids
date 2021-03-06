#Imports
from ursina import *
from random import randint, uniform


class Boid (Entity):
    def __init__ (self, posX, posY, posZ, rotX, rotY, rotZ, vel, acel, maxVel, mode, groesse):
        super().__init__(model="sprites.blend", position = (posX, posY, posZ), rotation = (rotX, rotY, rotZ), color = color.random_color(), scale = groesse)
        self.x = posX
        self.y = posY
        self.z = posZ
        self.vel = vel
        self.acel = acel
        self.maxVel = maxVel
        self.mode = mode
        self.collider = 'box'

    #Getter 
    #geben die Werte der Eigenschaften zurueck
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
    #uebeschreiben die Eigenschaften mit neuen Werten
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
        #Die Geschwindigkeit wird durch Addition der Beschleunigung so lange erhoeht bis sie das Maximum erreicht hat
        if self.vel < self.maxVel:
            self.vel += self.acel

    def closeBoids(self):
        #Diese Funktion ist dazu da um die Boids in der Naehe zu erfassen
        close = []
        #Dafuer wird die Liste benutzt, die bei der Erstellung der Boids befuellt wird
        #jeder Boid au??er man selbst wird in dieser for-Schleife durchgegangen
        for i in Liste_Boids:
            if i != self:
                #wenn die Distanz zwischen dem self.Boid und dem zu vergleichenden Boid unter 5 liegt wird der vergleichende Boid in die Liste mit den Boids in der Naehe hinzugefuegt
                distanceBoids = distance(self.position, i.position)
                if distanceBoids < 6:
                    close.append(i)
        return close

    def alignment(self):
        #Die Boids in der Naehe werden zwischengespeichert
        proximity = self.closeBoids()
        #Die einzelnen Rotationswerte und die Geschwindigkeitswerte des self.Boids werden hier gespeichert
        Boid1XR = self.rotation_x
        Boid1YR = self.rotation_y
        Boid1ZR = self.rotation_z
        Boid1V = self.vel
        Boid1MV = self.maxVel
        Boid1A = self.acel
        for i in proximity: # fuer jeden Boid in der Naehe wird das Alignment-Verfahren durchgegangen
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
            #Die Durchschnittswerte ueberschreiben die Rotations und Geschwindigkeitswerte des self.Boid
            self.rotation_x = avgXR
            self.rotation_y = avgYR
            self.rotation_z = avgZR
            self.vel = avgV
            self.maxVel = avgMV
            self.acel = avgA

    def seperation(self):#sparrend fehlerhaft
        #Versuch 1 fehlerhaft
        #Die Boids in der Naehe werden zwischengespeichert
        proximity = self.closeBoids()
        if len(proximity) > 1:
            for i in proximity:
                #wenn die Distanz zwischen dem self.Boid und des zu vergeichenden Boids <2 ist wird die Mitte zwischen den beiden Boids berechnet
                if distance(self.position, i.position) < 2:
                    center = (self.position + i.position)/2
                    #Die Differenz zwischen der Mitte und der eigenen Position wird von der Position subtrahiert um den Abstand zu erhoehen
                    self.position += Vec3(center - self.position) *.05
                    
    def cohesion(self):
        #Die Boids in der Naehe werden gespeichert
        proximity = self.closeBoids()
        #Die Mitte aller Boids in der Naehe wird berechnet
        center = self.position
        if len(proximity) > 1:
            for i in proximity:
                center = (center + i.position)/2
        #falls die Distanz des Boids zu der Mitte gro?? genug ist wird der Abstand zur Mitte der Position hinzugefuegt
        #damit die Boids immer in die Mitte des Flocks ziehen
        if distance(self.position, center) >= 2:
            self.position -= Vec3(center - self.position) *.05


    def seperationCohesion(self):
        #Versuch 2 resourcenfressend
        #Raycast werden erstellt die in 5 Richtungen gerichtet sind, eine Distanz von 5 haben, und die W??nde ignorieren
        raycastup = raycast(origin = self.position, direction = self.up, distance = 5, traverse_target = scene, ignore = (Wireframe,))
        raycastright = raycast(origin = self.position, direction = self.right, distance = 5, traverse_target = scene, ignore = (Wireframe,))
        raycastleft = raycast(origin = self.position, direction = self.left, distance = 5, traverse_target = scene, ignore = (Wireframe,))
        raycastback = raycast(origin = self.position, direction = self.back, distance = 5, traverse_target = scene, ignore = (Wireframe,))
        raycastforward = raycast(origin = self.position, direction = self.forward, distance = 5, traverse_target = scene, ignore = (Wireframe,))

        #Falls einer der Raycasts einen Boid ber??hrt, wird die Distanz gespeichert
        # Falls diese Distanz kleiner als 2 ist dreht der Boid weg
        # Falls diese Distanz gr????er als 2 ist dreht der Boid hin
    
        if raycastup.hit:
            distance_up = raycastup.distance
            if distance_up < 2:
                self.rotation += self.back * self.vel/1000
            if distance_up > 2:
                self.rotation += self.back * self.vel/1000

        if raycastright.hit:
            distance_right = raycastright.distance
            if distance_right < 2:
                self.rotation += self.left * self.vel/1000
            if distance_right > 2:
                self.rotation += self.right * self.vel/1000

        if raycastleft.hit:
            distance_left = raycastleft.distance
            if distance_left < 2:
                self.rotation += self.right * self.vel/1000
            if distance_left > 2:
                self.rotation += self.left * self.vel/1000

        if raycastback.hit:
            distance_back = raycastback.distance
            if distance_back < 2:
                self.rotation += self.forward * self.vel/1000
            if distance_back > 2:
                self.rotation += self.back * self.vel/1000

        if raycastforward.hit:
            distance_forward = raycastforward.distance
            if distance_forward < 2:
                self.rotation += self.back * self.vel/1000
            if distance_forward > 2:
                self.rotation += self.forward * self.vel/1000
        

    def avoidWall(self):
        #Raycasts
        #Ein Raycast wird erzeugt der in die Bewegungsrichtung 5 Einheiten weit ausgerchtet ist 
        raycastup = raycast(origin = self.position, direction = self.up, distance = 7, traverse_target = scene, ignore = (self,), debug = True)
        #Wenn dieser Raycast etwas beruehrt werden weitere Raycast erstellt, die in 4 weitere Richtungen ausgerichtet sind
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
            
            #je nach kleinster Distanz werden verschiedene Rotationsaenderung durchgefuehrt
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
        #Die Posiiton wird durch Multiplikation der Geschwindigkeit und der Bewegungsrichtung veraendert
        #Die Bewegungsrichtung ist hier up/hoch, da die Modeldatei danach ausgerichtet ist
        self.position += self.up * (self.vel/1000)
        self.updateVel()
        #Warp Modus

        if self.mode == 1:
            #falls die Position des Boids nach der Bewegung die der Waende ueberschreiten wird die Position auf die gegenueberliegende Seite gesetzt
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

        #Waendevermeidung
        elif self.mode == 2:
            #Funktion zur Waendevermeidung wird aufgerufen
            self.avoidWall()

        #Pong-Modus
        elif self.mode == 3:
            #bei ueberschreitung des Bereichs soll die Rotation veraendert werden
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
        #ressourcensparend
        #self.cohesion()
        #self.seperation()
        #ressourcenfressend
        self.seperationCohesion()

class Wireframe (Entity):
    def __init__(self):
        #05.01.2022
        #Wireframe
        #Erzeugung des Wuerfels
        self.wf1 = Entity(model = "cube", collider = 'box', position = (0, -51, -51), scale_x = 102)
        self.wf2 = Entity(model = "cube", collider = 'box', position = (-51, -51, 0), scale_z = 102)
        self.wf3 = Entity(model = "cube", collider = 'box', position = (0, -51, 51), scale_x = 102)
        self.wf4 = Entity(model = "cube", collider = 'box', position = (51, -51, 0), scale_z = 102)
        self.wf5 = Entity(model = "cube", collider = 'box', position = (51, 0, 51), scale_y = 102)
        self.wf6 = Entity(model = "cube", collider = 'box', position = (51, 0, -51), scale_y = -102)
        self.wf7 = Entity(model = "cube", collider = 'box', position = (-51, 0, 51), scale_y = 102)
        self.wf8 = Entity(model = "cube", collider = 'box', position = (-51, 0, -51), scale_y = 102)
        self.wf9 = Entity(model = "cube", collider = 'box', position = (-51, 51, 0), scale_z = -102)
        self.wf10 = Entity(model = "cube", collider = 'box', position =(0, 51, 51), scale_x = -102)
        self.wf11 = Entity(model = "cube", collider = 'box', position =(51, 51, 0), scale_z = 102)
        self.wf12 = Entity(model = "cube", collider = 'box', position =(0, 51, -51), scale_x = -102)
        #Erzeugung der Waende
        self.w1 = Entity(model = 'cube', collider = 'box', position = (0,0,-52),scale=(110,110,0), color = color.red, alpha = 0)
        self.w2 = Entity(model='cube', collider = 'box', position = (0,0,52), scale = (110,110,0), color = color.red, alpha = 0)
        self.w3 = Entity(model='cube', collider = 'box', position = (-52, 0,0), scale = (0, 110, 110), color = color.red, alpha = 0)
        self.w4 = Entity(model='cube', collider = 'box', position = (52, 0,0), scale = (0, 110, 110), color = color.red, alpha = 0)
        self.w5 = Entity(model = 'cube', collider = 'box', position = (0,-52,0), scale = (110,0,110), color = color.red, alpha = 0)
        self.w6 = Entity(model = 'cube', collider = 'box', position = (0,52,0), scale = (110,0,110), color = color.red, alpha = 0)

    #Getter
    def getWF1(self):
        return self.wf1
    def getWF2(self):
        return self.wf2
    def getWF3(self):
        return self.wf3
    def getWF4(self):
        return self.wf4
    def getWF5(self):
        return self.wf5
    def getWF6(self):
        return self.wf6
    def getWF7(self):
        return self.wf7
    def getWF8(self):
        return self.wf8
    def getWF9(self):
        return self.wf9
    def getWF10(self):
        return self.wf10
    def getWF11(self):
        return self.wf11
    def getWF12(self):
        return self.wf12
    def getW1(self):
        return self.w1
    def getW2(self):
        return self.w2
    def getW3(self):
        return self.w3
    def getW4(self):
        return self.w4
    def getW5(self):
        return self.w5
    def getW6(self):
        return self.w6
        
    #Setter
    def setWF1(self, nWF):
        self.wf1 = nWF    
    def setWF2(self, nWF):
        self.wf2 = nWF
    def setWF3(self, nWF):
        self.wf3 = nWF
    def setWF4(self, nWF):
        self.wf4 = nWF
    def setWF5(self, nWF):
        self.wf5 = nWF
    def setWF6(self, nWF):
        self.wf6 = nWF
    def setWF7(self, nWF):
        self.wf7 = nWF
    def setWF8(self, nWF):
        self.wf8 = nWF
    def setWF9(self, nWF):
        self.wf9 = nWF
    def setWF10(self, nWF):
        self.wf10 = nWF
    def setWF11(self, nWF):
        self.wf11 = nWF
    def setWF12(self, nWF):
        self.wf12 = nWF
    def setW1(self, nW):
        self.w1 = nW
    def setW2(self, nW):
        self.w2 = nW
    def setW3(self, nW):
        self.w3 = nW
    def setW4(self, nW):
        self.w4 = nW
    def setW5(self, nW):
        self.w5 = nW
    def setW6(self, nW):
        self.w6 = nW



def createBoids(anzahl):
    #Boids werden erstellt und in der Liste gespeichert
    for i in range(anzahl):
        temp = Boid(randint(-30,30), randint(-30,30), randint(-30, 30), randint(0,360), randint(0,360), randint(0,360), uniform(0.0, 100.0), uniform(0.0, 10.0), 300.0, 1, groesse)
        Liste_Boids.append(temp)

def input(key):
    #https://www.ursinaengine.org/entity_basics.html 10.01.2022
    #10.01.2022
    if held_keys["+"]:
        #Boid wird erstellt und der Liste hinzugefuegt
        temp = Boid(randint(-30,30), randint(-30,30), randint(-30, 30), randint(0,360), randint(0,360), randint(0,360), uniform(50.0, 300.0), uniform(0.0, 10.0), 300.0, 1, groesse)
        Liste_Boids.append(temp)

    if held_keys["-"]:
        #Der letzte Boid wird deaktiviert um nicht mehr angezeigt zu werden
        Liste_Boids[len(Liste_Boids)-1].disable()
        #letzter Boid wird aus der Liste entfernt
        Liste_Boids.pop()

    #Der Modus jedes Boids wird geaendert
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
                            \nvorwaerts:                 [W]
                            \nrueckwaerts:                [S]
                            \nhoch:                         [E]
                            \nrunter:                      [Q]
                            \n\nBoidanzahl aendern:
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
#Kameraposition wird veraendert um den Bereich von Anfang an zu sehen
camera.position = (0,10,-350)
#EditorCamera ermoeglicht die Veraenderung der Kamera
EditorCamera()

#Erstellen
#Wireframe
wireframe = Wireframe()
#Anleitung
createInstruction()
#Boids
######################################################################################################################################
anzahl = 1
groesse = (500,500,500)
######################################################################################################################################

Liste_Boids = []
createBoids(anzahl)

#Fenster wird ausgefuehrt
app.run()