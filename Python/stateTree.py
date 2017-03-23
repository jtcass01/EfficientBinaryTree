from heap import Heap
from state import State

class StateTree:
    #===== Initialization =====
    def __init__(self, size):
        print("Initializing Binary Tree... ")
        
        self.root = None
        binaryHeap = Heap(size)

        for value in binaryHeap.getHeap():
            self.add(value)

        print("Binary Tree successfully initialized")        

    def getRoot(self):
        return self.root

    def add(self, key):
        if(self.root == None):
            self.root = State(key)
        else:
            self._add(key, self.root)

    def _add(self, key, state):
        if(key < state.getKey()):
            if(state.getLeftChild() != None):
                self._add(key, state.getLeftChild())
            else:
                state.setLeftChild(State(key))
        else:
            if(state.getRightChild() != None):
                self._add(key, state.getRightChild())
            else:
                state.setRightChild(State(key))

    #===== SETTERS =====
    def replace(self, key, state):
        if(self.root == None):
            print("Tree is empty. Unable to perform replace.")
        else:
            if self.root.getKey() == key:
                self.root.replaceValues(state)
            else:
                self._replace(key, self.root, state)
                
    def _replace(self, key, currentState, suggestedState):
        if(currentState.getKey() == key):
            currentState.replaceValues(suggestState)
        elif(key < currentState.getKey() and currentState.getLeftChild() != None):
            self._replace(key, state.getLeftChild(), suggestState)
        elif(key < currentState.getKey() and currentState.getRightChild() != None):
            self._replace(key, state.getRightChild(), suggestState)
        else:
            print("Replacement failed.  End of chain reached.")

    #===== GETTERS =====
    def get(self, key):
        if(self.root != None):
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, state):
        if(key == state.getKey()):
            return state
        elif(key < state.getKey() and state.getLeftChild() != None):
            self._get(key, state.getLeftChild())
        elif(key > state.getKey() and state.getRightChild() != None):
            self._get(key, state.getRightChild())

    #===== DISPLAY =====
    def __str__(self):
        string = "\n\nPRINTING BINARY TREE"

        if(self.isEmpty()):
            string += "\nTree is empty."
        else:
            string += self.printBranch(self.root)

        return string

    def printBranch(self, currentState):
        string = ""
        
        if(currentState != None):
            string += self.printBranch(currentState.leftChild)
            string += str(currentState)
            string += self.printBranch(currentState.rightChild)

        return string
            

    #===== MISC =====
    def isEmpty(self):
        if(self.root == None):
            return True
        else:
            return False
