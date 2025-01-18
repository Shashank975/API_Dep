from flask import Flask, jsonify,request
# import db_cnxn
from db import db
import json
app = Flask(__name__)


@app.route('/')
def home():
    return "Comeback Home"


@app.route('/api/dep_data')
def Department_dataAPI():
    # data = db_cnxn.department_data()
    data = db
    return jsonify(data)