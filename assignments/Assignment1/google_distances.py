"""CSC148 Lab 1

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a function that uses Google Maps to find
the distance between two cities.

You are *not* responsible for understanding how the json and
urllib.request libraries work; focus only on extracting data from
the dictionary (see TODO below).
"""
import json
from urllib.request import urlopen

API_KEY = 'AIzaSyCBTNTwx_joRD5zVE5di4W89pQmiRzHcWk'

GOOGLE_MAPS_API_URL = (
    'https://maps.googleapis.com/maps/api/distancematrix/json?' +
    'units=metric&origins={}&destinations={}&key=' +
    API_KEY)


def get_city_data(city1, city2):
    """Return the distance between two cities using the Google Maps API.

    The distance returned is measured in metres.

    @type city1: str
    @type city2: str
    @rtype: int
    """
    formatted_city1 = city1.replace(' ', '+')
    formatted_city2 = city2.replace(' ', '+')
    request_url = GOOGLE_MAPS_API_URL.format(formatted_city1, formatted_city2)

    response_text = urlopen(request_url).read().decode(encoding='UTF-8')
    response_json = json.loads(response_text)

    return response_json['rows'][0]['elements'][0]['distance']['text']
