import tkinter as tk

class GUINode:
    def __init__(self, key, diameter=20, x=250, y=250, text="1"):
        self.diameter = diameter
        self.radius = diameter/2
        self.x = x
        self.y = y
        self.text = str(key)
        self.key = int(key)
        self.time = 0
        self.alt = 0
        self.vel = 0
        self.accel = 0
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return self.text + "\n"

    def draw_self(self, canvas):
        canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill="#0B3D91")
        canvas.create_text(self.x, self.y, fill="#FFFFFF", text = str(self.text), width = self.diameter)

    def connect_the_dots(self, otherNode, canvas):
        canvas.create_line(self.x,self.y, otherNode.getX(), otherNode.getY(), fill="#FC3D21")
        self.draw_self(canvas)
        otherNode.draw_self(canvas)

    def replaceValues(self, newNode):
        self.setTime(newNode.getTime())
        self.setAltitude(newNode.getAltitude())
        self.setVelocity(newNode.getVelocity())
        self.setAcceleration(newNode.getAcceleration())

    # ===== GETTERS =====
    def getRadius(self):
        return self.radius
    def getDiameter(self):
        return self.diameter
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getText(self):
        return self.text
    def getKey(self):
        return self.key
    def getTime(self):
        return self.time
    def getAltitude(self):
        return self.alt
    def getVelocity(self):
        return self.vel
    def getAcceleration(self):
        return self.accel
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    # ===== SETTERS =====
    def setDiameter(self, diameter):
        self.diameter = diameter
    def setRadius(self, radius):
        self.radius = radius
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setText(self, text):
        self.text = text
    def setKey(self, newKey):
        self.key = newKey
        return self
    def setTime(self, newTime):
        self.time = newTime
        return self
    def setAltitude(self, newAltitude):
        self.alt = newAltitude
        return self
    def setVelocity(self, newVelocity):
        self.vel = newVelocity
        return self
    def setAcceleration(self, newAcceleration):
        self.accel = newAcceleration
        return self
    def setLeftChild(self, newChild):
        self.leftChild = newChild
        return self
    def setRightChild(self, newChild):
        self.rightChild = newChild
        return self
