#!/usr/bin/env python3

import requests
import time
import turtle


__author__ = 'Patrick Buzzo'


def get_astronaut_info():
    """ Write a python program to obtain a list of the
    astronauts who are currently in space.
    Print their full names, the spacecraft,
    and the total number of astronauts in space."""
    response = requests.get("http://api.open-notify.org/astros.json").json()
    people_list = response['people']
    print("Number of astronauts in space: {}\n".format(response['number']))
    print("List of Astronauts and Their Crafts:\n{}\n".format(people_list))
    return response


def get_iss_info():
    """ Write a python program to obtain the longitude,
    latitude, and timestamp of ISS"""
    response = requests.get("http://api.open-notify.org/iss-now.json").json()
    lon = response['iss_position']["longitude"]
    lat = response['iss_position']["latitude"]
    timed = response["timestamp"]
    return lon, lat, timed


def find_next_pass():
    """ Find out the next time that the ISS
    will be overhead of Indianapolis IN."""
    lat = 39.7
    lon = -86.1
    response = requests.get(
        f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}&n=1')
    fixed_time = time.ctime(response.json()['response'][0]['risetime'])
    response = turtle.Turtle()
    response.shape('circle')
    response.color('yellow')
    response.penup()
    response.goto(lon, lat)
    response.write(fixed_time, font=15)


def model_iss_path(coords):
    """ With the turtle graphics library (part of standard Python),
    create a graphics screen with the world map background image"""
    map_image = turtle.Screen()
    map_image.setup(width=0.7, height=0.5)
    map_image.bgpic('map.gif')
    map_image.setworldcoordinates(-180, -120, 180, 120)

    find_next_pass()

    map_image.addshape('iss.gif')
    iss_station = turtle.Turtle()
    iss_station.shape('iss.gif')
    iss_station.goto(float(coords[0]), float(coords[1]))

    map_image.exitonclick()

    return map_image


def main():
    lon, lat, time = get_iss_info()
    model_iss_path([lon, lat])
    get_astronaut_info()


if __name__ == '__main__':
    main()
