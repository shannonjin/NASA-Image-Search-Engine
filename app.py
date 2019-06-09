from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
	PARAMS= request.form
	print(PARAMS)
	return render_template('index.html')



#def search():
    #render_template(index.html)-
	#url="https://images-api.nasa.gov/search"

