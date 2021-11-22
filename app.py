from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN889"

river_data=[
	{'River':"EXZ",
	'Data':"dss fsfdfsf fffdf"},
	{'River':"ABC",
	'Data':"FSGGG yjhnn fffdf"},
]

aquifer_data=[{
	'Stationarity':'Yes',
	'Trend':'No',
	'Cyclic':'Yes'
}]

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")



@app.route("/river", methods=['POST', 'GET'])
def river():
	return render_template("river.html",river_data=river_data)

@app.route("/spring", methods=['POST', 'GET'])
def spring():
	return render_template("spring.html",river_data=river_data)

@app.route("/lake", methods=['POST', 'GET'])
def lake():
	return render_template("lake.html",river_data=river_data)

@app.route("/aquifer", methods=['POST', 'GET'])
def aquifer():
	return render_template("aquifer.html",aquifer_data=aquifer_data)
