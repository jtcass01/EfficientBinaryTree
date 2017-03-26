import tkinter as tk
from GUInode import GUINode
from GUIBTree import GUIBTree


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width = 500, height=500)
        self.canvas.configure(background="black")
        bottom_frame = self.build_bottom_frame()        

        self.build_binary_canvas()

    def build_bottom_frame(self):
        frame = tk.Frame(self)
        frame.pack(side="bottom")
        frame.configure(background="#000000")
        
        self.valueEntry = tk.Entry(frame)
        self.label = tk.Label(frame, fg="#FFFFFF", bg="#000000", text="How large do you want the data structure to be?")
        self.start_button = tk.Button(frame, fg="#0B3D91", bg="#000000", command = self.start_program)
        self.quit = tk.Button(frame, text="QUIT", fg="#0B3D91", bg="#000000", command=root.destroy)

        self.valueEntry.insert(0,"16")

        self.start_button["text"] = "Start"
        self.start_button.config(height=3, width=9)

        self.quit.config(height=3, width=9)

        self.start_button.pack(side="right", expand=1)
        self.quit.pack(side="left", expand=1)
        self.valueEntry.pack(side="bottom", expand=1)
        self.label.pack(side="top", expand=1)

        return frame

    def build_binary_canvas(self):
        width = 500
        height = 500

#        centerNode = GUINode(20, width/2, 20, "8")
#        leftNode = GUINode(20, width/4, height/2, "4")
#        rightNode = GUINode(20, width*3/4, height/2, "12")

#        centerNode.draw_self(canvas)
#        leftNode.draw_self(canvas)
#        rightNode.draw_self(canvas)

 #       centerNode.connect_the_dots(leftNode, canvas)
 #       centerNode.connect_the_dots(rightNode, canvas)
        
        self.canvas.pack(side="top", expand=1)

    def draw_binary_tree(self, canvas_width, canvas_height, n):
        binaryTree = GUIBTree(n)
        binaryTree.draw_self(self.canvas, 500, 500)
        print(binaryTree)

    def start_program(self):
        print("TEST")
        if(self.valueEntry.get().isdigit()):
            n = int(self.valueEntry.get())
            self.draw_binary_tree(500, 500, n)
        else:
            self.label.set(text="Please be sure to enter an integer and try again.")

root = tk.Tk()
root.title("Efficient Binary Tree Display")
root.geometry("600x600")
root.configure(background="#000000")
app = Application(master=root)
app.mainloop()
