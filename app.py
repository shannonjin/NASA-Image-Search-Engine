from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	if request.method == 'GET':
		PARAMS= {'q': request.args.getlist('q')[0]}
		#print(type(PARAMS))
		#print(len(PARAMS))
		URL="https://images-api.nasa.gov/search"
		r=requests.get(url=URL, params=PARAMS)
		print(type(r))
		print(r)
		data=r.json()
		print(type(data))
		print(data)

	return render_template('search.html')






#def search():
    #render_template(index.html)-
	#url="https://images-api.nasa.gov/search"

