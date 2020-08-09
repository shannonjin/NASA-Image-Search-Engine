from flask import Flask, render_template, request
import requests
import sys
import random

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	if request.method == 'GET':
		PARAMS= {'q': request.args.getlist('q')[0]}
		
		if PARAMS['q']=='':
			n = random.randrange(1, 100, 1)
			PARAMS['q']= str(n)
			s = "No search term provided, random page returned"
		else:
			s = PARAMS['q']

		URL="https://images-api.nasa.gov/search"
		r=requests.get(url=URL, params=PARAMS)
	
		data=r.json()

	return render_template('search.html', data=data, search_term = s)
	






