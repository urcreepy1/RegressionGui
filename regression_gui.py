import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import Tkinter, Tkconstants, tkFileDialog


from matplotlib.figure import Figure

from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
	from Tkinter import*
	import Tkinter as Tk
    
else:
	from tkinter import*
	import tkinter as Tk
    
#########################  main window 


class m_window():
	def __init__(self,master):
		
		self.master=master
		self.master.geometry("400x500+100+200")
		self.button = Tk.Button(self.master, text='Generate', command=self.gotoGraph)  # Button for Genetating the Graph
		self.button.pack(anchor=W)

		self.button = Tk.Button(self.master, text='File', command=self.getFile)  #  Button to open file explorer
		self.button.pack(anchor=W)


	def gotoGraph(self):         # method to call the Graph class Window (Second Window that diaplays the graph)
		root2=Toplevel(self.master)
		myGui=Graph(root2)

	def getFile(self):
		main_fileName =tkFileDialog.askopenfilename(filetypes=(("csv_files","*.csv"),("All files","*.*")))  # storing the path of file in main_file Variable

		df1=pd.read_csv(main_fileName)      # reading the Csv file using pandas built in function

		columns1=df1.columns           # storing the columns list of csv file in columns1 



############################ X- cordinate Check Buttons 

		self.label1=Tk.Label(self.master,text="For X-Cordinte",fg="black",font="Sans 10 bold")     # label for X -co rodinate of the Graph
		self.label1.pack(anchor=W)


		self.vars = []	
		self.vars2=[]				# variable to store the states of check buuton as list 
		for pick in columns1:
			var = IntVar()				# variable that takes logical value of button states 
			chk1 = Checkbutton(self.master, text=pick, variable=var)     # craeting check buuton for each member of colums1
			chk1.pack(anchor=W)
			self.vars.append(var)


############################# Y- cordinates check button 

		self.label2=Tk.Label(self.master,text="For Y-Cordinte",fg="black",font="Sans 10 bold")     # label for X -co rodinate of the Graph
		self.label2.pack(anchor=W)

		for pick in columns1:
			var2 = IntVar()				# variable that takes logical value of button states 
			chk2 = Checkbutton(self.master, text=pick, variable=var2)     # craeting check buuton for each member of colums1
			chk2.pack(anchor=W)
			self.vars2.append(var2)		




################### Selection of model

		self.label2=Tk.Label(self.master,text="model",fg="black",font="Sans 10 bold")     # label for X -co rodinate of the Graph
		self.label2.pack(anchor=W)
		
		chk2 = Checkbutton(self.master, text="Linear Regression")     # craeting check buuton for each member of colums1
		chk2.pack(anchor=W)		

		chk2 = Checkbutton(self.master, text="Logistic Regression")     # craeting check buuton for each member of colums1
		chk2.pack(anchor=W)






################## Button state method
		button1= Tk.Button(self.master, text='Var',command=self.buttonState)     # button to diaplay ht button state in terminal
		button1.pack(anchor=W)

	def buttonState(self):
		print(map((lambda var: var.get()), self.vars))
		print(map((lambda var: var.get()), self.vars2))

		



#####################Graph generation class 
class Graph():
	def __init__(self,master):


		self.master=master

		def _quit():
			self.master.quit()
			self.master.destroy()
		self.button = Tk.Button(self.master, text='Quit', command=_quit)
		self.button.pack(side=Tk.BOTTOM)

		f = Figure(figsize=(5, 4), dpi=100)
		a = f.add_subplot(111)
		t = np.random.randint(low=1, high=100, size=50)
		s = sin(2*pi*t)

		a.plot(t, s)
		
		canvas = FigureCanvasTkAgg(f,self.master)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
		toolbar = NavigationToolbar2TkAgg(canvas,self.master)
		toolbar.update()
		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

		def on_key_event(event):
			print('you pressed %s' % event.key)
			key_press_handler(eventcanvas, toolbar)
		canvas.mpl_connect('key_press_event', on_key_event)
    	


######################   Root window

def main():

	root=Tk.Tk()
	root.title("Regression Gui")    
	my_m_window=m_window(root)
	root.mainloop()


if __name__=="__main__":
	main()