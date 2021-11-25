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
	'Conclusion':'The metrics are low, which mean that the model is good for future predictions',
	'Target':'Depth to Groundwater',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]
auser_summary=[{
	'Rows':'8154',
	'Columns':'26',
	'SDate':'05-03-1998',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'9.660',
	'Conclusion':'Model fits for prediction',
	'Target':'Depth to Groundwater',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]

doganella_summary=[{
	'Rows':'6026',
	'Columns':'21',
	'SDate':'01-01-2004',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'2303394.249',
	'Conclusion':'The model is not fitting well with the groundtruth. I think there are too much variables to make him fit. But we can see that the set of these 9 models to predict the depth to groundwater is using always the same variables : the temperature and the volume have a huge impact on it.',
	'Target':'Depth to Groundwater',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]
luco_summary=[{
	'Rows':'7487',
	'Columns':'21',
	'SDate':'01-01-2000',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'104.257',
	'Conclusion':'The prediction fits with the trend of the ground truth but again, many peaks come to rise the error metrics.',
	'Target':'Depth to Groundwater',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]

spring_amiata_summary=[{
	'Rows':'7487',
	'Columns':'15',
	'SDate':'01-01-2000',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'12092.499',
	'Conclusion':'The model is not fitting well with the ground truth. According to this model, the other flow rates depend of the galleria alta flow rate. The temperature is also a variable that make us the predict the flow rate',
	'Target':'Flow Rate',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]
spring_madonna_summary=[{
	'Rows':'3113',
	'Columns':'3',
	'SDate':'01-01-2012',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'1440699.158',
	'Conclusion':'The Main reason for higher RMSE is there are  always some peaks that make higher the error metrics.',
	'Target':'Flow Rate',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]
spring_lupa_summary=[{
	'Rows':'7487',
	'Columns':'21',
	'SDate':'01-01-2009',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'833.960',
	'Conclusion':'The model is not fitting well with the ground truth.',
	'Target':'Flow Rate',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]

river_summary=[{
	'Rows':'8217',
	'Columns':'16',
	'SDate':'01-01-1998',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'0.034',
	'Conclusion':'The model is fitting well with the ground truth.',
	'Target':'Hydrometry',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]

lake_summary=[{
	'Rows':'6603',
	'Columns':'8',
	'SDate':'03-06-2002',
	'EDate':'30-06-2020',
	'Model':'LSTM',
	'RMSE':'0.114',
	'Conclusion':'The metrics are low, which mean that the model is good for future predictions.',
	'Target':'Lake Level, Flow Rate',
	'Features':'Date, Rainfall, Drainage_volume, River_hydrometry'
}]

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")



@app.route("/river", methods=['POST', 'GET'])
def river():
	return render_template("river.html",river_data=river_data,river_summary=river_summary)

@app.route("/spring", methods=['POST', 'GET'])
def spring():
	return render_template("spring.html",spring_amiata_summary=spring_amiata_summary,spring_madonna_summary=spring_madonna_summary,spring_lupa_summary=spring_lupa_summary)

@app.route("/lake", methods=['POST', 'GET'])
def lake():
	return render_template("lake.html",lake_summary=lake_summary)

@app.route("/aquifer", methods=['POST', 'GET'])
def aquifer():
	return render_template("aquifer.html",aquifer_data=aquifer_data,petrignano_summary=petrignano_summary,auser_summary=auser_summary,doganella_summary=doganella_summary,luco_summary=luco_summary)
