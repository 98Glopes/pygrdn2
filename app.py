import threading
from flask import Flask, jsonify, render_template, request
import json
import datetime as dt
import glob
from meshlium import meshliumDB
from routine import Routine
from clock import clock

import utility
import rasp


app = Flask(__name__)




@app.route('/config')
def config():
    return render_template('config.html' , header='Configurações', title='PyGRDN2 - Config')

	
@app.route('/routine', methods=['POST'])
def routine():
	Routine(request.form)
	return config()


@app.route('/')
def home():

	meshlium = meshliumDB('172.16.232.105', 'root', 'libelium2007','MeshliumDB')
	link = glob.glob('./static/img/pictures/*.jpg')
	link = link[-1]
	
	data = meshlium.read_moment()
	return render_template('home.html', header="PyGRDN2 - Acompanhe em tempo real",
							title='PyGRDN2' , data=data, link=link)



@app.route('/dash', methods=['POST','GET']) 
def dash():	

	meshlium = meshliumDB('172.16.232.105', 'root', 'libelium2007','MeshliumDB')
	if request.form:
		print(request.form)
		
		meshlium.inf_limit = request.form['first_hour']
		meshlium.sup_limit = request.form['last_hour']

	search, date= meshlium.read_msensors()
	json = {
			'datas': date,
			'TC': search[0],
			'PRES': search[1],
			'HUM': search[2],
			'SOIL_C': search[3],
			'SOIL_E': search[4]
		}

	return render_template('dash.html', header='Dashboard', title='PyGRDN2 - Dashboard', json=json)


@app.route('/rest/<change>')
def rest(change):

	if change == 'lamps':

		board.invert_lamps()
		return 'ok'

	if change == 'water_pump':

		board.irriga()
		return 'ok'

	if change == 'coolers':

		board.invert_coolers()
		return 'ok'


	if change =='picture':

		board.pictures()
		return 'ok'

	return 'nothing'


	
	
if __name__ == '__main__':

	board = rasp.Rasp(10)
	meshlium = meshliumDB('172.16.232.105', 'root', 'libelium2007','MeshliumDB')
	app.run(port=80, debug=True, host='0.0.0.0')