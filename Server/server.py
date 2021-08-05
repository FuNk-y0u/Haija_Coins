# Importing stuff
import socket
import threading
import pickle
import os
from os import path
import json
from filemng import*

#Server
class server():
	def __init__(self):
		#Server_Variables
		self.HEADER = 64
		self.PORT = 5050
		self.SERVER = socket.gethostbyname(socket.gethostname())
		self.ADDR = (self.SERVER, self.PORT)
		self.FORMAT = "utf-8"
		self.DISCONNECT_MESSAGE = "disconn"
		self.balance_client = 0

		#Connection Variables
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.ADDR)

		#File Management Stuff
		self.filemng = filemng(self)

			
	#Handeling Client Stuff	
	def handle_client(self,conn, addr):
		print(f"NEW CONNECTION:  {self.addr} CONNECTED! ")
		self.connected = True

		#Runs the code while connected
		while self.connected:
			self.msg_length = conn.recv(self.HEADER).decode(self.FORMAT) #Gets Message
			if self.msg_length:
				#Message_Variables
				self.msg_length = int(self.msg_length)
				self.msg = conn.recv(self.msg_length)
				self.msg = pickle.loads(self.msg)

				#Data Checking
				if self.msg == self.DISCONNECT_MESSAGE:#Disconnect message
					self.connected = False#Disables Connection

				# Sign in Checking ['si','username','password']	
				if self.msg[0] == "si":
					self.filemng.signin(self.msg) #Signin stuff

				#Log in Checking ['log','username','password']	
				if self.msg[0] == "log":
					self.filemng.login(self.msg)

				print(f"[{self.addr}]: {self.msg}")#Prints the data and location		
				
		conn.close()	
	
	#Server Starting Defination	
	def start(self):
		self.server.listen()
		print(f"Server is listening on {self.SERVER}")
		while True:
			self.conn, self.addr = self.server.accept()
			self.thread = threading.Thread(target = self.handle_client, args=(self.conn, self.addr))
			self.thread.start()
			print(f"ACTIVE CONNECTIONS:  {threading.activeCount() - 1}") #Shows active connections
			

	#Sends Message to client		
	def sendMessage(self,Message):
		self.Message = Message
		self.conn.send(self.Message.encode(self.FORMAT))