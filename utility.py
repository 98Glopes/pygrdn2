import datetime
import threading
import time
import sqlite3
import cv2


def irriga():
	return print('Irrigando')
	
def lamps_on():
	return print('Ligando as luzes')
	
def lamps_off():
	return print('Apagando as luzes')
	
def picture():
	def take_picture():
		
		name = picture_name()
		cam  = cv2.VideoCapture(0) #0 é a webcam do notebook
		success , img = cam.read()
		if success == True:
			cv2.imwrite('./static/img/pictures/'+name.replace(':','-'), img)
			print(name)
			database = db_pictures('database.db')
			database.burn(name.replace(':','-'))
			database.close()
	
	thread = threading.Thread(target=take_picture)
	thread.start()
	

def picture_name(): #retorna uma string com a data atual sem os segundos
		name = datetime.datetime.now()
		name = str(name).split(':')
		name = name[0]+':'+name[1]+'.jpg'		
		return name


def date_parser(timestamp): #Recebe uma str e retorna um date time
	""" Recebe uma string no formato AAAA-MM-DD HH:MM"""

	timestamp = timestamp.split(' ')
	data = timestamp[0]
	hora = timestamp[1]
	data = data.split('-')
	hora = hora.split(':')
	year, month, day = int(data[0]), int(data[1]), int(data[2])
	hour, minute = int(hora[0]), int(hora[1])

	return datetime.datetime(year, month, day, hour, minute)
	
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
	
		
	def burn_list(self, list): #recebe uma lista de tulas ('HH:MM' , ação())
			
		self.sql = """
		INSERT INTO alarm (hour , behavior)
		VALUES (? , ?)
		"""
		for alarmes in list:
			self.cursor.execute(self.sql, alarmes)
			
		self.conn.commit()
		print('burn')
		
		
	def clean(self):
		
		self.sql = """
		DELETE FROM alarm
		"""
		self.cursor.execute(self.sql)
		self.conn.commit()
		
		
	def search(self, hour): #recebe uma hora em formato string 'HH:MM'
		
		self.sql = """
		SELECT behavior FROM alarm WHERE hour = ?
		"""
		self.cursor.execute(self.sql, (hour,))
		return self.cursor.fetchall()
		
		
	def all(self):
	
		self.sql = """
		SELECT * FROM alarm
		"""
		self.cursor.execute(self.sql)
		self.search = self.cursor.fetchall()
		for self.linha in self.search:
			print(self.linha)


class db_pictures(dataBase):

	def __init__(self):
		super().__init__()


	def burn(self, pic_name):

		self.pic_name = pic_name

		self.sql = """
		INSERT INTO pictures (picutre)
		VALUES ?
		"""
		self.cursor.execute(sql, (self.pic_name,))
		self.conn.commit()


	def read():

		self.sql = """
		SELECT picture FROM pictures
		ORDER BY id DESC
		LIMIT 1
		"""
		self.cursor.execute()
		return self.cursor.fetchone()


def datetime_hour(date): #recebe como parametro um objeto datetime.datetime
	now = str(date)
	now = now.split(' ')
	now = now[1]
	now = now.split(':')
	return (str(now[0])+':'+str(now[1]))



def clock():

	while True:
	
		
		hora_atual = datetime_hour(datetime.datetime.now())
		#instancia classe para abrir o banco de dados na tabela 'alarm'
		data = alarm() 
		search = data.search(hora_atual)
		
		#executa as funções referentes aos alarmes
		for behavior in search:
			
			print(hora_atual)
			eval(behavior[0])
		
		#finaliza conexão com o banco de dados
		data.close() 
		
		time.sleep(60)
		
		
		
		