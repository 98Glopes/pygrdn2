try:
	import RPi.GPIO as GPIO
except:
	pass

import time
import threading
import datetime
import cv2
import sqlite3
import utility







	
class Rasp(object):
	""" Class for manipulate Raspberry IOs """

	def __init__(self, tempo):

		db = alarm()
		lamps_on, lamps_off = db.lamps()
		now = datetime.datetime.now()
		now = utility.datetime_hour(now)
		print(now)
		if now > lamps_on and now < lamps_off:

			self.lamps_state = True
			print(self.lamps_state)

		else:

			self.lamps_state = False
			print(self.lamps_state)

		try:
			self.time = tempo
			self.lampR = 3 #Right Lamp pin
			self.lampL = 5 #Left lamp pin
			self.water_pump = 7 # Water pupmp pin

			self.coolers = 13 #coolers pin

#			self.channel_output = (self.lampR, self.lampL, self.water_pump, self.coolers)
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BOARD) #Configure the board
			GPIO.setup(self.lampR, GPIO.OUT, initial=self.lamps_state)
			GPIO.setup(self.lampL, GPIO.OUT, initial=self.lamps_state)
			GPIO.setup(self.water_pump, GPIO.OUT, initial=True)
			GPIO.setup(self.coolers, GPIO.OUT, initial=False)

		except:
			pass


	def lamps_on(self):

		try:

			GPIO.output(self.lampR, False)
			GPIO.output(self.lampL, False)

		except:

			return print("Can't possible turn on the lights")


	def lamps_off(self):

		try:

			GPIO.output(self.lampR, True)
			GPIO.output(self.lampL, True)

		except:

			return print("Can't possible turn of the lights")


	def invert_lamps(self): # Invert the lamps state

		try:

			GPIO.output(self.lampR, not GPIO.input(self.lampR))
			GPIO.output(self.lampL, not GPIO.input(self.lampL)) 

		except:

			return print("Can't possible invert the lamps state")


	def irriga(self):

		try:

			GPIO.output(self.water_pump, False)
			time.sleep(self.time)
			GPIO.output(self.water_pump, True)
			return print("Irrigando")

		except:

			pass




	def invert_coolers(self):

		try:

			GPIO.output(self.coolers, not GPIO.input(self.coolers))

		except:

			pass


	def current_state(self):

		self.state = {
			'lamps': GPIO.input(self.lampR) and GPIO.input(self.lampL),
			'water_pump': GPIO.input(self.water_pump),
			'coolers': GPIO.input(self.coolers)
		}

		return self.current_state

	def picture(self):
		def take_picture():
			
			name = picture_name()
			cam  = cv2.VideoCapture(0) #0 é a webcam do notebook
			success , img = cam.read()
			if success == True:
				cv2.imwrite('./static/img/pictures/'+name.replace(':','-'), img)
				print(name)
				
		thread = threading.Thread(target=take_picture)
		thread.start()


def picture_name(): #retorna uma string com a data atual sem os segundos
		name = datetime.datetime.now()
		name = str(name).split(':')
		name = name[0]+':'+name[1]+'.jpg'		
		return name

class dataBase(object): #classe Pai para iniciar o banco de dados
	
	def __init__(self):
	
		try:
			self.conn = sqlite3.connect('database.db')
			self.cursor = self.conn.cursor()
		except:
			return print('Nao foi possiel se conectar ao BD')
	
	def close(self):
		self.conn.close()


class alarm(dataBase): #classe filha da classe dataBase

	def __init__(self):
		super().__init__()

	def lamps(self):

		self.sql = """
		SELECT hour FROM alarm WHERE behavior = 'lamps_on()' or behavior = 'lamps_off()'
		"""
		self.cursor.execute(self.sql)
		self.search = self.cursor.fetchall()
		return self.search[0][0], self.search[1][0]