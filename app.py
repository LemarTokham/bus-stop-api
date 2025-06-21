import json, requests as request
import xml.etree.ElementTree as ET
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from flask import Flask, jsonify

from bus_stops import get_bus_stops
from bus_num import get_bus_numbers


def main():
    # Get bus stops
    bus_stops_file = 'timetables.json'
    bus_stops = get_bus_stops(bus_stops_file)
    
    # Print each stop one by one for route 7
    for stop_ref, details in bus_stops.items():
        print(f"Stop Ref: {stop_ref}, Name: {details['name']}, Coordinates: {details['coordinates']}")
    
    # Get bus numbers
    bus_numbers = get_bus_numbers()
    print("Bus Numbers:", bus_numbers)


if __name__ == "__main__":
    main()