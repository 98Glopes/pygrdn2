
try:
	import RPi.GPIO as GPIO
except:
	pass

	
class Rasp(object):
	""" Class for manipulate Raspberry IOs """

	def __init__(self):

		
		try:
			self.lampR = 3 #Right Lamp pin
			self.lampL = 5 #Left lamp pin
			self.water_pump = 7 # Water pupmp pin

			self.coolers = 13 #coolers pin

#			self.channel_output = (self.lampR, self.lampL, self.water_pump, self.coolers)
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BOARD) #Configure the board
			GPIO.setup(self.lampR, GPIO.OUT, initial=True)
			GPIO.setup(self.lampL, GPIO.OUT, initial=True)
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


	def irrigation_on(self):

		try:

			GPIO.output(self.water_pump, False)

		except:

			pass

	def irrigation_off(self):

		try:

			GPIO.output(self.water_pump, True)

		except:

			pass


	def invert_irrigation(self):

		try:

			GPIO.output(self.water_pump, not GPIO.input(self.water_pump))

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


