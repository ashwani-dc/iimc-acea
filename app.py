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

petrignano_summary=[{
	'Rows':'5223',
	'Columns':'7',
	'SDate':'14-03-2006',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'0.315',
	'Conclusion':'The metrics are low, which mean that the model is good for future predictions'
}]
auser_summary=[{
	'Rows':'8154',
	'Columns':'26',
	'SDate':'05-03-1998',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'',
	'Conclusion':'The metrics are low, which mean that the model is good for future predictions'
}]

doganella_summary=[{
	'Rows':'6026',
	'Columns':'21',
	'SDate':'01-01-2004',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'2303394.249',
	'Conclusion':'The model is not fitting well with the groundtruth. I think there are too much variables to make him fit. But we can see that the set of these 9 models to predict the depth to groundwater is using always the same variables : the temperature and the volume have a huge impact on it.'
}]
luco_summary=[{
	'Rows':'7487',
	'Columns':'21',
	'SDate':'01-01-2000',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'104.257',
	'Conclusion':'The prediction fits with the trend of the ground truth but again, many peaks come to rise the error metrics.'
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
	return render_template("aquifer.html",aquifer_data=aquifer_data,petrignano_summary=petrignano_summary,auser_summary=auser_summary,doganella_summary=doganella_summary,luco_summary=luco_summary)
