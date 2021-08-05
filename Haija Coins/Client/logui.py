import tkinter as tk
from tkinter import messagebox
import pickle
from tkinter import ttk
import time
import pyglet

class logui:
	def __init__(self):
		pyglet.font.add_file('res/Ui/font/Roboto-Thin.ttf')
		self.window = tk.Tk( className="Haija Coins" )

		self.label =  tk.Label(text = "test")#Test Label

		#Tabs stuff
		self.notebook = ttk.Notebook(self.window)
		self.frame1 = tk.Frame(self.notebook, width = 1100, 	height = 700, bg = "#202124")
		self.frame2 = tk.Frame(self.notebook, width = 1100, 	height = 700, bg = "#202124")
		self.frame3 = tk.Frame(self.notebook, width = 1100, 	height = 700, bg = "#202124") 

		#Home
		self.Title_home = tk.Label(self.frame1, text = "Home", font = ("Roboto-Thin.ttf", 40), bg = "#202124", fg = "white")
		self.About_home = tk.Label(self.frame1, text = "Thankyou! for signing into Haija Coins,\n Hope you have a fantastic time earning!\n         -With love and care <3, Robesckey 2021\n", font = ("Roboto-Thin.ttf", 10), bg = "#202124", fg = "#e67e7e")
		self.Updates_home = tk.Label(self.frame1, text = "Updates Log:\n 1> Created This Menu(Thursday, August 5, 2021)", font = ("Roboto-Thin.ttf", 20), bg = "#202124", fg = "White")


	def draw_ui(self):
		self.notebook.pack() # Note book stuff
		# Tabs stuff
		self.frame1.place(relx=.5, rely=.5, anchor="center",)
		self.frame2.place(relx=.5, rely=.5, anchor="center")
		self.notebook.add(self.frame1, text = "Home") #Tab 1
		self.notebook.add(self.frame2, text = "Earning Details") # Tab 2
		self.notebook.add(self.frame3, text = "Account Details") # Tab 3

		#Home
		self.Title_home.place(x = 0, y = 0)
		self.Updates_home.place(x = 0, y = 80)
		self.About_home.place(x = 0, y = 600)

		

	def ui_win(self):
		# Window stuff	
		self.window.geometry("1100x700") #Window resolution
		self.window.resizable(0,0) #Disables full sceen 
		self.window.wm_iconbitmap('res/Ui/img/logo.ico') #Sets Icon
		self.window.mainloop()	#Stats the main window loop	



