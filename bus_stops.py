'''
This file will take in json file of timetables, extract & process it 
and sort it into different collections of bus stop locations, 
bus stop names, bus stop schedules.

brute force it for 1 bus route for now, expand it to all bus routes later,
rewriting code for reusability and modularity.
'''

import json


# Extracts bus stops from the json file. Returns a dictionary with stop references as keys
# and a dictionary of stop details (name and coordinates) as values.
def get_bus_stops(file):
    with open(file, 'r') as f:
        data = json.load(f)
    
    bus_stops = {}
    for stop in data["TransXChange"]['StopPoints']:
        no_of_stops = len(stop['AnnotatedStopPointRef'])
        for i in range(no_of_stops):
          stop_ref = stop['AnnotatedStopPointRef'][i]['StopPointRef'][0]
          common_name = stop['AnnotatedStopPointRef'][i]['CommonName'][0] 
          latitude = stop['AnnotatedStopPointRef'][i]['Location'][0]['Latitude'][0]
          longitude = stop['AnnotatedStopPointRef'][i]['Location'][0]['Longitude'][0]

          # print(f"Stop Ref: {stop_ref}, Name: {common_name}, Coordinates: ({latitude}, {longitude})")
          # bus_stops.append(stop)
          bus_stops[stop_ref] = {
              'name': common_name,
              'coordinates': (latitude, longitude)
          }
    
    return bus_stops


# This function will extract bus schedules from the timetables file.
# There are multiple schedules for the route, for no7 bus for example,
# it goes 3001, 3003, 3007, 3005 ... 3067 (note odd for outbound, even for inbound).
# The trouble is figuring out which time is for which bus stop, as some schedules only
# stop at about half the stops or less or skip stops.
def get_bus_schedules(file):
    ...


# main
def main():
    file = 'timetables.json'
    _ = get_bus_stops(file)
    # print each stop one by one
    for stop_ref, details in _.items():
        print(f"Stop Ref: {stop_ref}, Name: {details['name']}, Coordinates: {details['coordinates']}")

if __name__ == "__main__":
    main()
