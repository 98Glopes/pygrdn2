Scripts:m


	clock.py: verifica se na hora atual existe algum alarme programado no banco de dados

	behaviors.py: funções que acionam os atuadores da estufa

	database.py: script provisório para colocar informações dentro do database

Tabelas da database:

	alarmes:
		colunas: id, horario, ação
	
	parametros:
		colunas: id, humidade máxima (solo), humidade minima(solo), temperatura máxima,
			temperatura minima, humidade do ar minima, humidade do ar maxima, iomo
			
	
	log de erros:
		colunas: id, código de erro, descrição do erro , observações

