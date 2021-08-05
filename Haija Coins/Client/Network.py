import socket
import pickle
import threading
#Importing libraries

class Network:
	def __init__(self):
		#Client variables
		self.HEADER = 64
		self.PORT = 5050
		self.FORMAT = "utf-8"
		self.DISCONNECT_MESSAGE = "disconn"
		self.SERVER = "192.168.1.8"
		self.ADDR = (self.SERVER,self.PORT)

		#Client data
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#Data package variable
		self.package = ''

		#Server message variable
		self.serverMessage = ""
		
	def connect(self): #Connects to the server
		self.client.connect(self.ADDR) # (Adress of the server)

	def send(self,msg):
		#Sending message stuff
		self.message = msg 
		self.msg_length = len(self.message)
		self.send_length = str(self.msg_length).encode(self.FORMAT)
		self.send_length += b' ' * (self.HEADER - len(self.send_length))
		self.client.send(self.send_length)
		self.client.send(self.message)		

	def rec_msg(self):
		while True:
			self.serverMessage = self.client.recv(2048).decode(self.FORMAT) #Receive message running in while loop
					

	def snd_msg(self, package):
		self.thread = threading.Thread(target = self.rec_msg, args=())
		self.thread.start()	
		self.package = package
		self.send(self.package)

	def msg_Checking(self, ui):
		self.ui = ui
		if self.serverMessage != '': #If data is not null
			print(self.serverMessage) #Prints the message
			ui.ServerMsg(self.serverMessage) #Displays the message
		else:  
			pass	