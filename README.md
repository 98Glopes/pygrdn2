## PyGRDN2 

### O projeto:

PyGRDN2 é um estudo sobre estufas para cultivo de plantas utilizando iluminação artificial. No Brasil ainda existem poucas iniciativas nesta área, tanto no âmbito acadêmico como no universo maker. O projeto foi pensado e projetado para ser autônomo utilizando-se de um Raspberry Pi 3 para controlar as variáveis do ambiente. A monitoração foi feita utilizando os sensores da Libelium com o kit Smart Agriculture, cedido pelo Nucles Smart Campus da Facudade de Engenharia de Sorocaba (FACENS). Toda parte estrutural foi feita em MDF cortado a laser no FABLAB Facens.

![Desenho em 3D da estufa](https://github.com/98Glopes/pygrdn2/blob/master/static/img/grow.png)

### Parametrização e Configuração:

Para realizar a parametrização dos sistema de controle da estufa, foi criado uma pagina web utilizando o micro framework para a linguagem python Flask (app.py). No momento é possivel controlar e configurar as seguintes variaveis:
* Hora e intervalo das irrigações;
* Intervalo entre as fotografias da estufa;
* Inicio e fim do periodo luminoso.

![Configuração do sistema](https://github.com/98Glopes/pygrdn2/blob/master/static/img/config.png)

### Dashboard e vizualiação dos dados.

Para realizar a vizualição dos dados, foi criado uma Dashboard usando uma combinação entre Flask e ChartJS (Javascript), onde é exibido um gráfico referente a um periodo especificado pelo usuario, onde é possivel ver as seguintes variaveis: Temperatura, Umidade e Luminosidade). Além dessas variaveis ainda é possivel integrar aos graficos as seguintes leituras obitadas através do Smart Agriculture: Umidade do solo (Vaso 1 e 2) e pressão atmosférica.

![Dashboard](https://github.com/98Glopes/pygrdn2/blob/master/static/img/dash.png)

![Tela inicial](https://github.com/98Glopes/pygrdn2/blob/master/static/img/home.png)


Para maiores informações: gabriel.lopes@outlook.com
