Scripts:m


	clock.py: verifica se na hora atual existe algum alarme programado no banco de dados

	behaviors.py: fun��es que acionam os atuadores da estufa

	database.py: script provis�rio para colocar informa��es dentro do database

Tabelas da database:

	alarmes:
		colunas: id, horario, a��o
	
	parametros:
		colunas: id, humidade m�xima (solo), humidade minima(solo), temperatura m�xima,
			temperatura minima, humidade do ar minima, humidade do ar maxima, iomo
			
	
	log de erros:
		colunas: id, c�digo de erro, descri��o do erro , observa��es

