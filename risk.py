import os
import logging
from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def calculateRiskScore(score):
    assessment = ""

    if score < 600:
        assessment = "low"
    elif score < 900:
        assessment = "medium"
    else:
        assessment = "high"

    return assessment

