from Tkinter import *
import webbrowser

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "Caesar", font = ("arial", 18,"bold"))
        self.instruction.grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = W)

root = Tk()
root.title("Caesar")
root.geometry("400x360+600+300")
app = Application(root)
root.mainloop()
