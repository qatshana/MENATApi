from flask import Flask,request
from flask_restful import  Resource, Api
#import pandas as pd
import json

app=Flask(__name__)
api=Api(app)

tickers=['RJHI','SAMBA','ARNB','BSFR','ALINMA','SABB','NCB','RIBL']

class TodoSimple(Resource):

	def get(self,todo_id):
		if (todo_id in tickers):
			f=open(todo_id+'.json','r')
			data=f.read()
			f.close()
			txt=json.loads(data)
		else:
			txt = 'not supported'
		return txt
	def put(self,todo_id):
		todos[todo_id]=request.form['data']
		return {todo_id:todos[todo_id]}

api.add_resource(TodoSimple,'/<string:todo_id>')

if __name__=='__main__':
	app.run(debug=True)