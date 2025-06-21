'''
Right now, this script finds and returns all the bus numbers 
that are currently in service in the Merseyside area.
'''

import json, requests as request
import xml.etree.ElementTree as ET
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from flask import Flask, jsonify

global API_KEY, DATASET_ID
API_KEY = "b7085c08b7908af68ad10f79008c6c91b88ce318"
DATASET_ID = "15954"


# get list of all bus numbers serving in Merseyside
def get_bus_numbers():
    url = f"https://data.bus-data.dft.gov.uk/api/v1/dataset/{DATASET_ID}/?api_key={API_KEY}" 
    response = request.get(url)
    if response.status_code == 200:
        data = response.json()
        bus_numbers = [number for number in data['lines']]
        # bus_numbers.sort()
        return bus_numbers
    else:
        print(f"Error: {response.status_code}")
        return []
    

def main():
    print(get_bus_numbers())


if __name__ == "__main__":
    main()