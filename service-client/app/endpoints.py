from app import app
from flask import jsonify


@app.route("/")
def index():
    res = {'data':[],'message':'Hello from Service 2'}
    return jsonify(res)
