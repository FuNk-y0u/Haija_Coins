import socket
import pickle
import threading
import tkinter as tk
#Importing libraries

from ui import *
from Network import *
from logui import*
#Importing from other .py files
'''
network = Network() #Defining Network
ui = ui(network) #Defining ui with network


try: #Trys to connect 
	network.connect()
	ui.drawUI() #Drawing ui
	ui.ui_win() #Window loop
except Exception as e: #Server connection error 
	print(e)
	ui.serverError() #Shows server error from ui.py
'''
logui = logui()
logui.draw_ui()
logui.ui_win()	  



