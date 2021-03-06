import time
import datetime

from utility import *
import rasp


def clock(board):

	while True:
	
		
		hora_atual = datetime_hour(datetime.datetime.now())
		#instancia classe para abrir o banco de dados na tabela 'alarm'
		data = alarm() 
		search = data.search(hora_atual)
		
		#executa as funções referentes aos alarmes
		for behavior in search:
			
			print(hora_atual)
			eval('board.'behavior[0])
		
		#finaliza conexão com o banco de dados
		data.close() 
		print(hora_atual)
		time.sleep(60)


if __name__ == '__main__':

	board = rasp.Rasp()
	clock(board)