import urllib.requests 
import json

def get_API():
    with open('apikey.txt') as f:
        api_key = f.readline()
        f.close
#retrieve start destination from database
def get_Start_location():
    # implement retreving from database here when database is up and running 
    start_dest = "retrieved destination here"
    return start_dest

def get_End_destination():
    # implement retreving from database here when database is up and running 
    end_dest = "retrieved destination here"
    return end_dest
    # returns json file of all possible directions 
def get_directions(response):
    directions = json.loads(response)
    return directions
    # getting directions for travel method user specified 
def get_travel_method(directions, method):
    method.lower()
    keys = directions.keys()
    routes = routes[0].keys()
    
    if method == "vehicle":
        driving_route = routes[0]['DRIVING']
        return driving_route
    if method == "walk":
        walking_route = routes[0]['WALKING']
        return walking_route
    if method == "bike":
        bike_route = routes[0]['BICYCLING']
        return bike_route


#def get_traffic:
    #get traffic data from google maps directions api
    

if __name__ == "__main__":

    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    #format request and send it 
    nav_request = 'start={} &end={} &key={}'.format(get_Start_location, get_End_destination, get_API)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    
    travelMethod = input('How do you plan on travelling? (Vehicle, Walk, Bike): ')
    get_travel_method(travelMethod)