import sqlite3 as pymysql 
import datetime as dt

class meshliumDB(object): #Class for open the MeshliumDB
	"""Clas for open Meshlium database"""

	def __init__ (self, host, user, passw, database):
		""" Args: Host, User, Passw, Database 
			The time interval between the consults
			can be change by the properties inf_limit and sup_limit

		"""

		self.database = database
		self.host = host
		self.user = user
		self.passw = passw
		self.inf_limit = dt.datetime(2018,5,4,16,15)
		self.sup_limit = dt.datetime.now()

		try:

			self.conn = pymysql.connect('meshlium.db')
			self.cursor = self.conn.cursor()
			return print('Database connected')

		except:

			return print("Can't possible connect to database")


	def read_all(self):

		self.sql = """
		SELECT id, id_wasp, sensor, value, timestamp FROM sensorParser
		"""
		self.cursor.execute(self.sql)
		return self.cursor.fetchall()


	def read_sensor(self, sensor):
		""" Returns a list with the selected sensor values ​​from a certain date
			Args: Sensor """
		
		self.value = []
		self.date = []
		self.sql = """
		SELECT value, timestamp FROM sensorParser
		WHERE timestamp > ? and timestamp < ? and sensor = ?
		ORDER BY timestamp ASC
		"""
		self.cursor.execute(self.sql, (self.inf_limit, self.sup_limit, sensor))
		self.search = self.cursor.fetchall()

		for linha in self.search:
			self.value.append(float(linha[0]))
			self.date.append(str(linha[1]))

		return self.value, self.date


	def read_msensors(self, sensors=['TC', 'PAR', 'HUM', 'BAT']): #Read mutiples sensors
		""" Return one list about each sensor, all in a list"""

		self.sensors = sensors
		self.result = []

		for self.sensor in self.sensors:

			self.data, self.date = self.read_sensor(self.sensor) # Call the read_sensor method
			self.result.append(self.data)

		return self.result, self.date


	def read_moment(self):
		"""  Return the most atual sensors state"""


		self.sql = """
		SELECT sensor, value FROM sensorParser
		ORDER BY id DESC
		LIMIT 7
		"""
		self.cursor.execute(self.sql)
		self.search = self.cursor.fetchall()

		self.data = {
			'PAR': self.search[0][1],
			'PRES': self.search[1][1],
			'HUM': self.search[2][1],
			'TC': self.search[3][1],
			'SOIL_C': self.search[4][1],
			'SOIL_E': self.search[5][1],
			'BAT': self.search[6][1] 
		}
		return self.data

	def close(self):

		return self.conn.close()




#some tests
if __name__ == '__main__':

	meshlium = meshliumDB('192.168.1.100', 'root', 'libelium2007', 'MeshliumDB')

	meshlium.inf_limit = dt.datetime(2018,5,4,16,15)
	meshlium.sup_limit = dt.datetime.now()
	print(meshlium.read_moment())
