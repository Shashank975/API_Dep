from flask import Flask, jsonify,request
import db_cnxn
import json
app = Flask(__name__)


@app.route('/')
def home():
    return "Comeback Home"


@app.route('/api/dep_data')
def Department_dataAPI():
    data = db_cnxn.department_data()
    return jsonify(data)