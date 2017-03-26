from GUInode import GUINode

class GUIArray:
    def __init__(self, size):
        self.array = []
        
        for i in range(1, size+1):
            self.array.append(GUINode(i, use="array"))

    def __str__(self):
        string = ""

        for val in self.array:
            string += str(val)

        return string

    def draw_self(self, canvas, canvas_width, canvas_height):
        x = 20
        y = canvas_height/2-5

        for node_i in range(0, len(self.array)-1):
            self.array[node_i].setX(x)
            self.array[node_i].setY(y)

            self.array[node_i+1].setX(x+40)
            self.array[node_i+1].setY(y)

            self.array[node_i].connect_the_dots(self.array[node_i+1], canvas)
            x+= 40
