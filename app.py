import threading
from flask import Flask, jsonify, render_template, request
import json
import datetime as dt
from meshlium import meshliumDB
from routine import Routine
import utility

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
	meshlium = meshliumDB('172.16.54.69', 'root', 'libelium2007','MeshliumDB')
	data = meshlium.read_moment()
	meshlium.close()
	return render_template('home.html', header="PyGRDN2 - Acompanhe em tempo real",
							title='PyGRDN2' , data=data)



@app.route('/dash', methods=['POST','GET']) 
def dash():
	meshlium = meshliumDB('172.16.54.69', 'root', 'libelium2007','MeshliumDB')

	if request.form:
		print(request.form)
		
		meshlium.inf_limit = request.form['first_hour']
		meshlium.sup_limit = request.form['last_hour']

	search, date= meshlium.read_msensors()
	meshlium.close()
	json = {
			'datas': date,
			'TC': search[0],
			'PRES': search[1],
			'HUM': search[2],
		}
	return render_template('dash.html', header='Dashboard', title='PyGRDN2 - Dashboard', json=json)


@app.route('/REST')
def REST():
#	meshlium = meshliumDB('172.16.54.69', 'root', 'libelium2007', 'MeshliumDB')
#	meshlium.sup_limit = dt.datetime.now()
#	search, date= meshlium.read_msensors()
#	print(date)

	json = jsonify({
			'datas':[0,1,2],
			'TC':[0,1,2],
			'PRES':[0,1,2],
			'HUM':[0,1,2],
		})
	return retorno



	
	
if __name__ == '__main__':

	app.run(port=80, debug=True, host='0.0.0.0')