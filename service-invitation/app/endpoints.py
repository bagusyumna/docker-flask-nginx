from app import app
from flask import jsonify


@app.route("/")
def index():
    res = {'data':[],'message':'Hello from Service 1'}
    return jsonify(res)
