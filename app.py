from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	print("ha")
	if request.method == 'GET':
		PARAMS= request.form['search']
		print('hi')
		print(PARAMS)






#def search():
    #render_template(index.html)-
	#url="https://images-api.nasa.gov/search"

