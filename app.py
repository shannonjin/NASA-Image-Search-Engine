from flask import Flask, render_template, request


app = Flask(__name__)
z
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
	if request.method == 'GET':
		#print("hi")
		PARAMS= request.args.getlist('q')
		print(PARAMS)


	return render_template('search.html')






#def search():
    #render_template(index.html)-
	#url="https://images-api.nasa.gov/search"

