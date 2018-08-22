import os
import logging
import risk
import json
from datetime import datetime, timedelta
from flask_cors import CORS

from flask import Flask, request, render_template

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['POST'])
def getMany():
	data = request.get_json(force=True)
	returnData = []
	
	for x in data:
		returnData.append(risk.calculateRiskScore(x))
	
	response = app.response_class(
		response=json.dumps(returnData),
	    status=200,
	    mimetype='application/json'
	)
	return response
