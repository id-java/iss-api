#!/bin/python3

from tkinter import *
import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print (result)

print('People in space: ', result['number'])

people = result['people']

for p in people:
    print (p['name'] + ' in ' + p['craft'])

url_pos = 'http://api.open-notify.org/iss-now.json'
response_pos = urllib.request.urlopen(url_pos)
result_pos = json.loads(response_pos.read())
location = result_pos['iss_position']
print('\nISS Position: ')
print('Longitude: ', location['longitude'])
print('Latitude: ', location['latitude'])

# Point on Map
screen = turtle.Screen()
screen.setup(720.360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.png')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(location['longitude'],location['latitude'])