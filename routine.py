import datetime
from utility import alarm


def gen_routine(first, last, interval, function , lista): #recebe os parametros com objetos datetine
	while last >= first:
		
		hour = datetime_hour(first)
		data = (hour, function)
		lista.append(data)
		first += interval


def datetime_hour(date): #recebe como parametro um objeto datetime.datetime e retorn string "HH:MM"
	now = str(date)
	now = now.split(' ')
	now = now[1]
	now = now.split(':')
	return (str(now[0])+':'+str(now[1]))


def gen_datetime(hour): #recebe uma string 'HH:MM' e retorna um obj datetime (dia genérico)
		hour = hour.split(':')
		hours, minutes = int(hour[0]) , int(hour[1])
		return datetime.datetime(2018, 1, 1, hours, minutes)
	
def Routine(data):

	alarms = [] #lista vazia para os alarmes
	
	pic_interval = int(data['pic_interval'])
	first_irr = data['first_irr']
	last_irr = data['last_irr']
	irr_interval = int(data['irr_interval'])
	lamps_on = data['lamps_on']
	lamps_off = data['lamps_off']


	
	#gerando os alarmes para as fotografias
	first_pic = datetime.datetime(2018, 1 , 1 , 0, 0)
	last_pic = datetime.datetime(2018, 1 , 1 , 23, 59)
	pic_interval = datetime.timedelta(minutes=pic_interval)
	gen_routine(first_pic, last_pic, pic_interval, 'picture()', alarms)
	
	#gerando ps alarmes para irrigação
	first_irr = gen_datetime(first_irr) #converte o formato 'HH:MM' para obj datetime
	last_irr = gen_datetime(last_irr)
	irr_interval = datetime.timedelta(minutes=irr_interval)
	gen_routine(first_irr, last_irr, irr_interval, 'irriga()', alarms)
	
	#gerando os alarmes para as lampadas
	alarms.append((lamps_on, 'lamps_on()'))
	alarms.append((lamps_off, 'lamps_off()'))
		
	""" #para debug
	for alarm in alarms:
		print(alarm)
	"""	
	
	data = alarm() #inicia banco de dados
	data.clean() #limpa todos os alarmes do banco de dados
	data.burn_list(alarms) #grava os alarmes gerados no banco de dados
	data.close() #fecha o banco de dados