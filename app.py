import os
import logging
import risk
from datetime import datetime, timedelta


from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    r = int(request.args.get("risk"))
    health = risk.calculateRiskScore(r)
    return jsonify(health)

