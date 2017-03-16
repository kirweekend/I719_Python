from Tkinter import *
import webbrowser

class Application(Frame):

	def __init__(self, master = None):
		if master == None:
			pass

		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		# Title label
		self.instruction = Label(self, text = "Caesar GUI", font=("arial",17,"bold"))
		self.instruction.grid(row = 1, column = 0, columnspan = 2, padx = 22, sticky = W)

		# Method label
		self.method = Label(self, text = "Choose method:")
		self.method.grid(row = 2, column = 0, columnspan = 2, padx = 22, sticky = W)

		# Method options
		self.var1 = IntVar()

		self.option = Radiobutton(self, text="Encrypt", pady = 5, variable=self.var1, value=1)
		self.option.grid(row = 3, column = 0, columnspan = 1, padx = 22, sticky = W)

		self.option = Radiobutton(self, text="Decrypt", pady = 5, variable=self.var1, value=2)
		self.option.grid(row = 3, column = 1, columnspan = 1, padx = 5, sticky = W)

		# Message label
		self.instruction = Label(self, text = "Enter message: ")
		self.instruction.grid(row = 4, column = 0, columnspan = 150, padx = 22, sticky = W)

		# Message entry
		self.message= Entry(self)
		self.message.grid(row = 5, column = 0, padx = 22, sticky = W)

		# Key label
		self.instruction = Label(self, text = "Enter key (1-26): ")
		self.instruction.grid(row = 6, column = 0, columnspan = 2, padx = 22, sticky = W)

		# Key entry
		self.key= Entry(self)
		self.key.grid(row = 7, column = 0, padx = 22, sticky = W)

		# Submit
		self.submit_button = Button(self, text = "Submit", command = self.call_caesar)
		self.submit_button.grid(row = 8, column = 0, padx = 22, sticky = W)

		# Result label
		self.instruction = Label(self, text = "Result", font=("arial",14,"bold"))
		self.instruction.grid(row = 9, column = 0, columnspan = 2, padx = 23, sticky = W)

		# Result
		self.result = Text(self, width = 45, height = 6, wrap = WORD)
		self.result.grid(row = 10, column = 0, columnspan = 3, padx = 22, sticky = W)

		#Github label
		self.github = Label(self, text = "Fork it at http://github.com/kirweekend", cursor="hand2")
		self.github.bind("<Button-1>", self.githubLink)
		self.github.grid(row = 11, column = 0, columnspan = 3, padx = 23, sticky = W)

	def githubLink(self, event):
		webbrowser.open_new(r"http://github.com/kirweekend")

	def call_caesar(self):
		m = self.message.get()
		k = int(self.key.get())
		n = self.var1.get()

		return self.caesar(m, k, n)

	def caesar(self, m, k, n):
		if n == 2:
			k = -k

		# Empty text container
		text = ''

		for symbol in m:

			if symbol.isalpha():
				num = ord(symbol) + k

				if symbol.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26

				elif symbol.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26

				text  += chr(num)
			else:
				text += symbol

		self.result.delete(0.0, END)
		self.option.deselect()
		self.result.insert(0.0, text )

		return text

if __name__ == "__main__":
	root = Tk()
	root.title("Caesar GUI")
	root.geometry("370x350+600+300")
	app = Application(root)
	root.mainloop()
