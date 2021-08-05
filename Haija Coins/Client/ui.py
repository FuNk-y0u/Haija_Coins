import tkinter as tk
from tkinter import messagebox
import pickle
from Network import*
from tkinter import ttk
import time
#Importing stuff

class ui:
	def __init__(self,nt):
		#Image importing stuff
		self.window = tk.Tk( className="Haija Coins" )
		self.bg = tk.PhotoImage(file = "res/Ui/img/bg.png")
		self.button_img = tk.PhotoImage(file = "res/Ui/img/button.png")
		self.buton_img_pressed = tk.PhotoImage(file = "res/Ui/img/button_pressed.png")
		self.logo_img = tk.PhotoImage(file = "res/Ui/img/logo2.png") 
		self.check_box_img = tk.PhotoImage(file = 'res/Ui/img/check_box.png')
		self.check_box_pressed_img = tk.PhotoImage(file = 'res/Ui/img/check_box_pressed.png')
		self.checked = False

		#Background stuff
		self.image = tk.Label( image = self.bg, width = 900, height = 500) # Background Image
		self.logo = tk.Label(image = self.logo_img) # Back Ground Image
		
		#Tabs stuff
		self.notebook = ttk.Notebook(self.window)
		self.frame1 = tk.Frame(self.notebook, width = 350, 	height = 400, bg = "white")
		self.frame2 = tk.Frame(self.notebook, width = 350, 	height = 400, bg = "white")

		#Login
		self.button = tk.Button(self.frame1, image = self.button_img, command = self.login, borderwidth = 0, relief='sunken') #Login button
		self.title = tk.Label(self.frame1, text = "Haija Coins", font = ("segoe ui", 30), bg = "white") # Title
		self.user_name_entry = tk.Entry(self.frame1, width = 30, borderwidth = 0, bg = '#d6d6d6', font = ("segoe ui", 15)) #Username entry box
		self.password_entry = tk.Entry(self.frame1 , width = 30, borderwidth = 0, bg = '#d6d6d6', font = ("segoe ui", 15), show = '*') # Password Entry Box
		self.titleA = tk.Label(self.frame1, text = "Your user name?", font = ("segoe ui", 10), bg = "white") # User Name Label
		self.titleB = tk.Label(self.frame1, text = "Your password?", font = ("segoe ui", 10), bg = "white") # Password Name Label
		self.checkBox = tk.Button(self.frame1, image = self.check_box_img, borderwidth = 0, relief='sunken', command = self.show_pass ) # Show pass button 
		self.label_showPas = tk.Label(self.frame1, text = "Show Password", font = ("segoe ui", 10), bg = "white") # Show pass button label

		#Signup
		self.button_si = tk.Button(self.frame2, image = self.button_img, command = self.signup, borderwidth = 0, relief='sunken') #sign up button
		self.singup_title = tk.Label(self.frame2, text = "Signup", font = ("segoe ui", 30), bg = "white") # Sign up title
		self.user_name_entry_si = tk.Entry(self.frame2, width = 30, borderwidth = 0, bg = '#d6d6d6', font = ("segoe ui", 15)) #Username singup entry box
		self.titleA_si = tk.Label(self.frame2, text = "Your user name?", font = ("segoe ui", 10), bg = "white") # User Name Signup Label
		self.titleB_si = tk.Label(self.frame2, text = "Your password?", font = ("segoe ui", 10), bg = "white") # Password Name signup Label
		self.password_entry_si = tk.Entry(self.frame2 , width = 30, borderwidth = 0, bg = '#d6d6d6', font = ("segoe ui", 15), show = '*') # Password Entry Box
		self.password_rentry_si = tk.Entry(self.frame2 , width = 30, borderwidth = 0, bg = '#d6d6d6', font = ("segoe ui", 15), show = '*') # Password Entry Box
		self.titleC_si = tk.Label(self.frame2, text = "Repeat your password:", font = ("segoe ui", 10), bg = "white") # Password Name signup Label
		

		self.nt = nt # Networking stuff

		self.user_detail = [] # User_details stuff

		self.serverMessage = '' #Server message received


	def login(self):
		# Login stuff
		self.button.config(image = self.buton_img_pressed) #Button pressed Image
		self.user_name = self.user_name_entry.get() #Gets Username
		self.password = self.password_entry.get() #Gets Password
		self.user_detail = ["log",self.user_name, self.password] #Packs the data into 1 variable
		self.package = pickle.dumps(self.user_detail) #Encryps the data
		self.nt.snd_msg(self.package) #Sends the data to server
		time.sleep(1) #Waits for the responce
		self.nt.msg_Checking(self) #Checks the data
		self.button_si.config(image = self.button_img)


	def signup(self):
		self.button_si.config(image = self.buton_img_pressed) #Button pressed Image
		self.user_name_si = self.user_name_entry_si.get() #Gets Username
		self.password_si = self.password_entry_si.get() #Gets Password
		self.rentry_password_si = self.password_rentry_si.get()  #Gets re-entered password
		
		################ password and username validation ###############################
		if self.password_si != "" and self.user_name_si != "": #Checks wether the data is empty or not
			if len(self.user_name_si) >= 3 and len(self.password_si) > 3: # Checks wether the password and username are longer than 3 letters
				if self.user_name_si.lower() not in self.password_si.lower(): #Checks if there is password in the username	
					if self.rentry_password_si == self.password_si:# Checks if the password and re entered password are equal
						print("Data is conformed now sending the data") #Prints after conforming the data
						try: #Trys to send data
							self.si_details = ["si",self.user_name_si, self.password_si] # Puts data into 1 variable
							self.si_package = pickle.dumps(self.si_details) #Encryps the data
							self.nt.snd_msg(self.si_package) #Sends the data to the server
							time.sleep(1) #Waits for the responce
							self.nt.msg_Checking(self) #Checks the data
							self.button_si.config(image = self.button_img)# Turns the button back to normal
						except Exception as e: # Stores error as e	
							print(e) #Prints error
							tk.messagebox.showerror("error", "Cannot connect to server please try again") #Login error
							self.button_si.config(image = self.button_img) #Returns the button to normal	
							pass 
					else:
						tk.messagebox.showerror("error", "Your password do not match") #Login error	
						self.button_si.config(image = self.button_img) #Returns the button to normal
						pass	
				else:
					tk.messagebox.showerror("error", "Your username is included in your password please  make a new one") #Login error
					self.button_si.config(image = self.button_img) #Returns the button to normal
					pass
			else:
				tk.messagebox.showerror("error", "Your user name and password length should be longer that 3") #Login error
				self.button_si.config(image = self.button_img) #Returns the button to normal
				pass
		else:
			tk.messagebox.showerror("error", "Either your Username or passowrd is empty") #Login error
			self.button_si.config(image = self.button_img) #Returns the button to normal
			pass

	def show_pass(self): #Password Showing Defination
		if self.checked == False:
			#If button is not checked
			self.checkBox.config(image = self.check_box_pressed_img)#Updates ui
			self.password_entry.config(show = "") # Shows the data un-censored
			self.checked = True # Sets the button to checked
		elif self.checked == True:
			#If button is checked
			self.checkBox.config(image = self.check_box_img) #Updates ui
			self.password_entry.config(show = "*") #Censores the password
			self.checked = False	#Sets the password to unchecked

	def drawUI(self):
		self.notebook.pack() # Note book stuff

		self.image.place(x = 0, y = 0) # Background Image 
		self.logo.place(x = 410, y = 30) # Logo placing

		# Login
		self.title.place(x = 70, y = 60) # Haija Coins title
		self.user_name_entry.place(relx=0.5, rely=0.4, anchor='center', height = 50 ) # User name entry
		self.password_entry.place(relx=0.5, rely=0.6, anchor='center', height = 50 )  # Password Entry
		self.titleA.place(relx=0.18, rely=0.3, anchor='center') # User name entry label
		self.titleB.place(relx=0.18, rely=0.5, anchor='center') # Password entry label
		self.checkBox.place(relx=0.15, rely=0.72, anchor='center' ) # Show pass word check box
		self.label_showPas.place(relx=0.35, rely=0.72, anchor='center') # Show pass word label
		self.button.place(relx=0.495, rely=0.85, anchor='center') # Login Button

		#Signup
		self.button_si.place(relx=0.495, rely=0.85, anchor='center') # Login Button	
		self.singup_title.place(x = 110, y = 5) # Sign up title
		self.titleA_si.place(relx=0.18, rely=0.2, anchor='center') # User name entry label
		self.user_name_entry_si.place(relx=0.5, rely=0.3, anchor='center', height = 50 ) # User name entry Signup
		self.password_entry_si.place(relx=0.5, rely=0.5, anchor='center', height = 50 )  # Password Entry Signup
		self.titleB_si.place(relx=0.18, rely=0.4, anchor='center') # User name entry label
		self.password_rentry_si.place(relx=0.5, rely=0.7, anchor='center', height = 50 )  # Password re-Entry Signup
		self.titleC_si.place(relx=0.23, rely=0.6, anchor='center') # User password re-entry label

		# Tabs stuff
		self.frame1.place(relx=.5, rely=.5, anchor="center")
		self.frame2.place(relx=.5, rely=.5, anchor="center")
		self.notebook.add(self.frame1, text = "Login") #Tab 1
		self.notebook.add(self.frame2, text = "Signup") # Tab 2

		

	def ui_win(self):
		# Window stuff	
		self.window.geometry("840x470") #Window resolution
		self.window.resizable(0,0) #Disables full sceen 
		self.window.wm_iconbitmap('res/Ui/img/logo.ico') #Sets Icon
		self.window.mainloop()	#Stats the main window loop

	def serverError(self):
		tk.messagebox.showerror("error", "couldnt connect to server please try again!") #Server connection error
	
	def ServerMsg(self, serverMessage):
		#Defines the data
		self.serverMessage = serverMessage
		tk.messagebox.showinfo(message = self.serverMessage) #Sets shows the message	

