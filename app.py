import os
import logging
import risk
import json
from datetime import datetime, timedelta

from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['POST'])
def home():
	data = request.get_json(force=True)
	returnData = []
	
	for x in data:
		returnData.append(risk.calculateRiskScore(x))
	
	return json.dumps(returnData)

