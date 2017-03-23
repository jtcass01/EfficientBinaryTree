from math import ceil

class Heap:
    def __init__(self, size=0):
        self.BinaryHeap = [None]*size
        self.getBinaryHeap()

    def __str__(self):
        string = "["

        for value_i in range(0, len(self.BinaryHeap)):
            if(value_i == self.size()-1):
                string += str(self.get(value_i)) + "]"
            else:
                string += str(self.get(value_i)) + ","
                
        return string

    def getHeap(self):
        return self.BinaryHeap

    def get(self, index):
        return self.BinaryHeap[int(index)]

    def push(self, value):
        self.BinaryHeap.append(value)
        return self

    def set(self, index, value):
        self.BinaryHeap[int(index)] = int(value)
        return self

    def size(self):
        return len(self.BinaryHeap)

    def zeroOutHeap(self):
        for value in self.BinaryHeap:
            value = 0
        return self

    def getBinaryHeap(self):
        print("Building binary heap...")
        capacity = self.size()
        mid = capacity / 2
        i=1
        j=0

        self.zeroOutHeap()

        self.set(0, mid)

#        print(self)

        while(i<capacity):
            nextLower = self.getNextLower(self.get(j), j)
#            print("nextLower", nextLower)
            nextUpper = self.getNextUpper(self.get(j), j)
#            print("nextUpper", nextUpper)

            if(self.hasLeft(self.get(j), nextLower)):
#                print("\nInserting {} at left node.\ti = {}\tj={}".format(self.getLeft(self.get(j), nextLower), i, j))
                self.set(i, self.getLeft(self.get(j), nextLower))
                i += 1
            if(self.hasRight(self.get(j), nextUpper)):
#                print("\nInserting {} at right node.\ti = {}\tj={}".format(self.getRight(self.get(j), nextUpper), i, j))
                self.set(i, self.getRight(self.get(j), nextUpper))
                i += 1                

            j += 1
#            print(self)

        if(self.checkRepresentation()):
            print("\nRepresentation checked.  All position values are included in binary heap.")
        else:
            print("\nRepresentation check failed.  Find programming error!")

        return self

    def getNextLower(self, value, index):
#        print(value)
#        print(type(value))
#        print("index", index)
        while(index > 0):
            index -= 1
            index = int(index / 2)

            if(self.get(index) < int(value)):
                return self.get(index)

        return 0

    def getNextUpper(self, value, index):
        while(index > 0):
            index -= 1
            index /= 2

            if(self.get(index) > int(value)):
               return self.get(index)
        return self.size()

    def hasLeft(self, value, minimum):
        possibility = int((value-minimum)/2)
        possibility = value - possibility

        if(possibility == 0):
            return 0
        else:
            if(self.isNew(possibility)):
#                print("\nLeft node possibilty confirmed! New left node = {}".format(possibility));
                return True
            else:
#                print("\nLeft node possibilty denied! Attempted left node = {}".format(possibility));
                return False

    def hasRight(self, value, maximum):
        possibility = int(ceil((maximum-value)/2))
        possibility += value

        if(value == maximum-1):
            if(self.isNew(possibility)):
                return True
            else:
                return False

        if(possibility == 0):
            return False
        else:
            if(self.isNew(possibility)):
                return True
            else:
                return False

    def isNew(self, possibility):
        for value in self.BinaryHeap:
            if value == possibility:
                return False
        return True

    def getLeft(self, value, minimum):
        possibility = int((value-minimum)/2)
        return value - possibility

    def getRight(self, value, maximum):
        possibility = int(ceil((maximum-value)/2))
        return value + possibility

    def checkRepresentation(self):
        test = [None]*self.size()
        i = 1
        found = False

        for value_i in range(1, self.size()+1):
            test[value_i-1] = value_i 

        for value in self.BinaryHeap:
            for val in test:
                if value == val:
                    found = True
            if(found == False):
                print("Failed value:",value)
                print("BinaryHeap:",self)
                print("test:",test)
                return False
            found = False
        return True
