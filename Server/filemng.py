import json
import socket
import threading
import pickle
#importing stuff

class filemng():
	def __init__(self, server):
		#Variables
		self.server = server

		#Sign data variable	
		self.signindata = []

		#Login data variable
		self.logindata = []	


	def signin(self, signindata):
		self.signindata = signindata # Gets the sign in data from client
		self.username = self.signindata[1] #Seperates the username from data
		self.password = self.signindata[2] #Seperates the password from data

		with open("user_data.json", "r") as json_file: #opens the user_data.json file from the server folder
			self.file = json.load(json_file) #Loads the data into self.file variable	
		self.user_detail = {"username": self.username, "password": self.password} # Packs the data together

		# If account already exsists
		if self.username in self.file:
			self.server.sendMessage("The account you are creating already exsists!") #Sends the client a message
		else:# If account doesnot exsists	
			self.file.update({self.username: self.user_detail}) #Updates the user_data.json file
			print(self.username + " account created") #Prints the data so the server operator knows thats going on
			with open('user_data.json', 'w') as json_file:# Opens data as write
				json.dump(self.file,json_file) #Dumps the file in to the data file
			self.server.sendMessage("Your account has been created please proceed to login")#Sends the message to the client 	
				

	def login(self,logindata):
		self.logindata = logindata #Gets the login data from client
		self.username = self.logindata[1]	
		self.password = self.logindata[2]	
		with open("user_data.json", "r") as json_file: #opens the user_data.json file from the server folder
			self.file = json.load(json_file) #Loads the data into self.file variable	
		
		if self.username in self.file:
			if self.password == self.file[self.username]["password"]:
				self.server.sendMessage("You are now logged in !")#Sends the message to the client 						
			else:
				self.server.sendMessage("The password doesnot match!")#Sends the message to the client 						
		else:
			self.server.sendMessage("the username you entered doesnot exsists!")#Sends the message to the client 				
					




