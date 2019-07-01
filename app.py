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
		#print(type(r))
		#print(r)
		data=r.json()
		#print(type(data))
		print(data)
		print(type(data['collection']['items']))
		#results=data['collection']
		#print("Results\n")
		#print(results)
		#metadata=results['metadata']
		#print(metadata)

		for result in data['collection']['items']:
			print(result)
			print(result['links'][0]['href'])


	return render_template('search.html', data=data)






#def search():
    #render_template(index.html)-
	#url="https://images-api.nasa.gov/search"

