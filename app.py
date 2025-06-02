import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi mom"


# Busstop data
@app.route('/api/buses/<atco_code>')
def get_buses(atco_code):
    # atco codes representing bus stops, with their values being the buses that stop at them
    obj = {'2800S42048C':[699],
           '2800S42053B':[6, 7, 79]
           }
    return jsonify(obj[atco_code])

if __name__ == "__main__":
    app.run(debug=True)