import tkinter as tk
from GUInode import GUINode
from GUIBTree import GUIBTree
from GUIArray import GUIArray

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.size_factor = 1
        self.n = 16

    def create_widgets(self):
        bottom_frame = self.build_bottom_frame()        

        self.build_canvases()
        self.configure(background="black")


    def build_bottom_frame(self):
        frame = tk.Frame(self)
        frame.pack(side="bottom")
        frame.configure(background="#000000")
        
        self.start_button = tk.Button(frame, fg="#0B3D91", bg="#000000", command = self.start_program)
        self.quit = tk.Button(frame, text="QUIT", fg="#0B3D91", bg="#000000", command=root.destroy)

        self.start_button["text"] = "Start"
        self.start_button.config(height=3, width=9)

        self.quit.config(height=3, width=9)

        self.config_button = tk.Button(frame, text ="Config Mode", fg="#0B3D91", bg="#000000", height = 3, width = 9, command = self.configure_mode)

        self.config_button.pack(side="right")
        self.start_button.pack(side="right", expand=1)
        self.quit.pack(side="left", expand=1)

        return frame

    def configure_mode(self):
        if(self.config_button["text"] == "Config Mode"):
            self.config_button["text"] = "Test Mode"
            self.start_button["text"] = "Update Config"
            self.binaryCanvas.pack_forget()
            self.arrayCanvas.pack_forget()
            self.build_configure_panel()
        else:
            self.config_panel.pack_forget()
            self.config_panel.labels.pack_forget()
            self.config_panel.entrys.pack_forget()
            self.config_button["text"] = "Config Mode"
            self.start_button["text"] = "Start"
            self.binaryCanvas.pack(side="top")
            self.arrayCanvas.pack(side="top")

    def build_configure_panel(self):
        self.config_panel = tk.Frame(self, width = 1300, height=250)
        self.config_panel.pack(side="top")
        self.config_panel.configure(background="black")

        self.config_panel.labels = self.build_config("left")
        self.config_panel.entrys = self.build_config("right")

        #Insert default values/update to current.
        self.config_panel.sizeEntry.insert(0, str(self.size_factor))
        self.config_panel.nEntry.insert(0, str(self.n))

    def build_config(self, side):
        column = tk.Frame(self)
        column.pack(side=side)
        column.configure(background="black")

        if side == "left":
            #Label for self.size_factor
            self.config_panel.sizeLabel = tk.Label(column, text="Size %: ", fg="#0B3D91", bg="#000000")

            #Label for self.n
            self.config_panel.nLabel = tk.Label(column, fg="#0B3D91", bg="#000000", text="How large do you want the data structure to be?")

            #pack
            self.config_panel.sizeLabel.pack(side="top")
            self.config_panel.nLabel.pack(side="top")

        else:
            self.config_panel.sizeEntry = tk.Entry(column)

            self.config_panel.nEntry = tk.Entry(column)

            self.config_panel.sizeEntry.pack(side="top")
            self.config_panel.nEntry.pack(side="top")

        return column
            
        
    def build_canvases(self):
        self.binaryCanvas = tk.Canvas(self, width = 1300, height=250)
        self.binaryCanvas.configure(background="black")

        self.arrayCanvas = tk.Canvas(self, width = 1300, height=50)
        self.arrayCanvas.configure(background="black")

        self.binaryCanvas.pack(side="top", expand=1)
        self.arrayCanvas.pack(side="top")

    def draw_array(self, canvas_height, canvas_width, n):
        array = GUIArray(n)
        array.draw_self(self.arrayCanvas, canvas_width, canvas_height)


    def draw_binary_tree(self, canvas_height, canvas_width, n):
        binaryTree = GUIBTree(n, self.size_factor)
        binaryTree.draw_self(self.binaryCanvas, canvas_width, canvas_height)
        print(binaryTree)

    def update_configuration(self):
        self.size_factor = float(self.config_panel.sizeEntry.get())
        self.n = int(self.config_panel.nEntry.get())

    def start_program(self):
        if(self.start_button["text"] == "Start"):
            self.draw_binary_tree(250, 1300, self.n)
            self.draw_array(50,1300, self.n)
        else:
            self.update_configuration()

root = tk.Tk()
root.title("Efficient Binary Tree Display")
root.geometry("1400x350")
root.configure(background="#000000")
app = Application(master=root)
app.mainloop()
