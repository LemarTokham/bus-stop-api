import json, requests as request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from flask import Flask, jsonify

global API_KEY, DATASET_ID
API_KEY = "b7085c08b7908af68ad10f79008c6c91b88ce318"
DATASET_ID = "15954"


# get list of all bus numbers
def get_bus_numbers():
    url = f"https://data.bus-data.dft.gov.uk/api/v1/dataset/{DATASET_ID}/?api_key={API_KEY}" 
    response = request.get(url)
    if response.status_code == 200:
        data = response.json()
        bus_numbers = [number for number in data['lines']]
        print(bus_numbers)
        return bus_numbers
    else:
        print(f"Error: {response.status_code}")
        return []

get_bus_numbers()




# import json
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hi mom"


# # Busstop data
# @app.route('/api/buses/<atco_code>')
# def get_buses(atco_code):
#     # atco codes representing bus stops, with their values being the buses that stop at them
#     obj = {'2800S42048C':[699],
#            '2800S42053B':[6, 7, 79]
#            }
#     return jsonify(obj[atco_code])

# if __name__ == "__main__":
#     app.run(debug=True)