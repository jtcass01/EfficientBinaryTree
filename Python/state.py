class State:
    def __init__(self, key):
        self.key = key
        self.time = 0
        self.alt = 0
        self.vel = 0
        self.accel = 0
        self.leftChild = None
        self.rightChild = None
        
    def __str__(self):
        string = ""
        string += "\n\n----- Printing State -----"
        string += "\nKey = " + str(self.key)
        if(self.time != 0):
            string += "\nTime = " + str(self.time)
        if(self.alt != 0):
            string += "\nAltitude = " + str(self.alt)
        if(self.vel != 0):
            string += "\nVelocity = " + str(self.vel)
        if(self.accel != 0):
            string += "\nAcceleration = " + str(self.accel)
        if(self.leftChild == None):
            string += "\nleftChild = None"
        else:
            string += "\nleftChild = " + str(self.leftChild.getKey())
        if(self.rightChild == None):
            string += "\nrightChild = None"
        else:
            string += "\nrightChild = " + str(self.rightChild.getKey())
        return string

    #Getters
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

    #Setters
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

    def replaceValues(self, state):
        self.setTime(state.getTime())
        self.setAltitude(state.getAltitude())
        self.setVelocity(state.getVelocity())
        self.setAcceleration(state.getAcceleration())

