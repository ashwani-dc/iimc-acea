from flask import Flask, render_template, request, flash
from flask_navigation import Navigation

app = Flask(__name__)
# nav = Navigation(app)
app.secret_key = "manbearpig_MUDMAN888"

# 	nav.Bar('top', [
#     nav.Item('Home', 'index'),
#     nav.Item('Gfg', 'gfg', {'page': 5}),
# ])

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


@app.route('/navpage')
def navpage():
    return render_template('navpage.html')
  
  
# @app.route('/gfg/<int:page>')
# def gfg(page):
#     return render_template('gfg.html', page=page)
  
  

# @app.route("/greet", methods=['POST', 'GET'])
# def greeter():
# 	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
# 	return render_template("index.html")

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
