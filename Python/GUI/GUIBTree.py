from stateTree import StateTree
from heap import Heap
from GUInode import GUINode
import tkinter as tk


class GUIBTree:
    #===== Initialization =====
    def __init__(self, size, size_factor=1.0):
        self.size_factor = size_factor
        self.root = None
        binaryHeap = Heap(size)

        for value in binaryHeap.getHeap():
            self.add(value)

    def getRoot(self):
        return self.root

    def add(self, key):
        if(self.root == None):
            self.root = GUINode(key, size_factor = self.size_factor, use="btree")
        else:
            self._add(key, self.root)

    def _add(self, key, node):
        if(key < node.getKey()):
            if(node.getLeftChild() != None):
                self._add(key, node.getLeftChild())
            else:
                node.setLeftChild(GUINode(key, size_factor = self.size_factor, use="btree"))
        else:
            if(node.getRightChild() != None):
                self._add(key, node.getRightChild())
            else:
                node.setRightChild(GUINode(key, size_factor = self.size_factor, use="btree"))

    def draw_self(self, canvas, canvas_width, canvas_height):
        canvas.delete("all")
        self.draw_branch(canvas, self.root, canvas_width/2, 30)

    def draw_branch(self, canvas, node, x, y):
        xSpacing = 10 * self.size_factor
        ySpacing = 35 * self.size_factor
        
        if node != None:
            self.draw_node(canvas, node, x, y)
            if(node.getLeftChild() != None):
                self.draw_branch(canvas, node.getLeftChild(), x - (node.getKey() - node.getLeftChild().getKey())*25*self.size_factor, y + ySpacing)
                node.connect_the_dots(node.getLeftChild(), canvas)
            if(node.getRightChild() != None):
                self.draw_branch(canvas, node.getRightChild(), x + (node.getRightChild().getKey() - node.getKey())*25*self.size_factor, y + ySpacing)
                node.connect_the_dots(node.getRightChild(), canvas)

    def draw_node(self, canvas, node, x, y):
        node.setX(x)
        node.setY(y)
        node.draw_self(canvas)

    #===== SETTERS =====
    def replace(self, key, node):
        if(self.root == None):
            print("Tree is empty. Unable to perform replace.")
        else:
            if self.root.getKey() == key:
                self.root.replaceValues(node)
            else:
                self._replace(key, self.root, node)
                
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
        string = "\n\nPRINTING BINARY TREE\n"

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
