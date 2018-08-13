import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import csv

from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

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
		self.x_coordinate=[]
		self.y_coordinate=[]

		self.master=master
		self.master.geometry("400x500+100+200")
#		self.button = Tk.Button(self.master, text='Generate', command=self.gotoGraph)  # Button for Genetating the Graph
#		self.button.pack(anchor=W)

		self.button = Tk.Button(self.master, text='File', command=self.getFile)  #  Button to open file explorer
		self.button.pack(anchor=W)


	def linear_model_window(self):         # method to call the Graph class Window (Second Window that diaplays the graph)
		root2=Toplevel(self.master)
		myGui=linear_model(root2,self.x_co,self.y_co)

	def log_model_window(self):         # method to call the Graph class Window (Second Window that diaplays the graph)
		root3=Toplevel(self.master)
		myGui=logistic_model(root3,self.x_co,self.y_co)

	def getFile(self):
		main_fileName =tkFileDialog.askopenfilename(filetypes=(("csv_files","*.csv"),("All files","*.*")))  # storing the path of file in main_file Variable
		self.csv_file=pd.read_csv(main_fileName)
		with open(main_fileName) as f:
			reader=csv.reader(f)
			self.columns1 =reader.next()

############################ X- cordinate Check Buttons 

		self.label1=Tk.Label(self.master,text="For X-Cordinte",fg="black",font="Sans 10 bold")     # label for X -co rodinate of the Graph
		self.label1.pack(anchor=W)


		self.vars = []	
		self.vars2=[]				# variable to store the states of check buuton as list 
		for pick in self.columns1:
			var = IntVar()				# variable that takes logical value of button states 
			chk1 = Checkbutton(self.master, text=pick, variable=var)     # craeting check buuton for each member of colums1
			chk1.pack(anchor=W)
			self.vars.append(var)


############################# Y- cordinates check button 

		self.label2=Tk.Label(self.master,text="For Y-Cordinte",fg="black",font="Sans 10 bold")     # label for X -co rodinate of the Graph
		self.label2.pack(anchor=W)

		for pick in self.columns1:
			var2 = IntVar()				# variable that takes logical value of button states 
			chk2 = Checkbutton(self.master, text=pick, variable=var2)     # craeting check buuton for each member of colums1
			chk2.pack(anchor=W)
			self.vars2.append(var2)	



################## Assing the x and y coordinate to the variables
		
		assign=Tk.Button(self.master,text="Assign",command=self.assign1)
		assign.pack(anchor=W)

############# Assign button 

	def assign1(self):

		selector1=(map((lambda var: var.get()), self.vars))
		selector2=(map((lambda var: var.get()), self.vars2))
			
			
		for i in range(0,len(selector1)):
			if selector1[i:(i+1)] == [1]:
				self.x_coordinate=self.x_coordinate+(self.columns1[i:(i+1)])

		for i in range(0,len(selector2)):
			if selector2[i:(i+1)] == [1]:
				self.y_coordinate=self.y_coordinate+(self.columns1[i:(i+1)])

		self.x_co=self.csv_file[self.x_coordinate]
		self.y_co=self.csv_file[self.y_coordinate]


		self.Linear_regession_button=Tk.Button(self.master,text="Linear Regression",command=self.linear_model_window)
		self.Linear_regession_button.pack(anchor=W)

		self.Logistic_regession_button=Tk.Button(self.master,text="Logistic Regression",command=self.log_model_window)
		self.Logistic_regession_button.pack(anchor=W)
			







############### Function forf linear Regression model
class linear_model():
	def __init__(self,master,x_co,y_co):

		self.master=master
		self.x_co=x_co
		self.y_co=y_co
		def _quit():
			self.master.quit()
			self.master.destroy()


		X_train,X_test,y_train,y_test=train_test_split(self.x_co,self.y_co,test_size=0.4,random_state=101)
		lm=LinearRegression()
		lm.fit(X_train,y_train)
		pridiction=lm.predict(X_test)

		f = Figure(figsize=(5, 4), dpi=100)
		a = f.add_subplot(111)
		t = pridiction
		s = y_test
		a.scatter(t, s)
			
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

		self.button = Tk.Button(self.master, text='Quit', command=_quit)
		self.button.pack(side=Tk.BOTTOM)



class logistic_model():
	def __init__(self,master,x_co,y_co):
		self.master=master
		self.x_co=x_co
		self.y_co=y_co
		def _quit():
			self.master.quit()
			self.master.destroy()

		X_train,X_test,y_train,y_test=train_test_split(self.x_co,self.y_co,test_size=0.4,random_state=101)

		log_model=LogisticRegression()
		log_model.fit(X_train,y_train)
		pridiction2=log_model.predict(X_test)
		f = Figure(figsize=(5, 4), dpi=100)

			
		def _quit():
			self.master.quit()
			self.master.destroy()



		a = f.add_subplot(111)
		t = pridiction
		s = y_test
		a.scatter(t, s)
			
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

		self.button = Tk.Button(self.master, text='Quit', command=_quit)
		self.button.pack(side=Tk.BOTTOM)



######################   Root window

def main():

	root=Tk.Tk()
	root.title("Regression Gui")    
	my_m_window=m_window(root)
	root.mainloop()


if __name__=="__main__":
	main()