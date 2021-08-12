 #!/usr/bin/env python3
# # - * - coding: utf-8 - * -
""" Midwest Map A* Search """
__author__="Michael Cicero"

import sys
import re
import math
from queue import PriorityQueue

def AStar(inpStr):
    temp = inpStr.split(" ")
    start = temp[0]
    finish = temp[1]
    h = cost(start,finish)
    frontier = PriorityQueue()
    frontier.put((h,start))
    explored = set()
    cities = set(d.keys())
    path = []
    routes = set(d2.keys())

    while not frontier.empty():
        curr = frontier.get()
        if not curr[1] in explored:
            explored.add(curr[1])
            for city in cities.difference(explored):
                if curr[1] + city in routes and city + " " + finish in routes:
                    pathcost = cost(curr[1], city) + cost(city, finish)
                    frontier.put((pathcost, city))
            path.append(curr[1])
            if curr[1] == finish:
                return path

    return(False)

def cost(start, finish):
    a = list(d[start])
    b = list(d[finish])
    c = start + " " + finish
    distance = int(d2[c])
    euclidean_distance = math.sqrt( (int(a[0])-int(b[0]))**2 + (int(a[1])-int(b[1]))**2)
    cost = euclidean_distance + distance
    return(cost)

d = {}
d2 = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
            s = line.strip().split(", ")
            d[s[0]] = (s[1],s[2])
            

with open(sys.argv[2], 'r') as f:
    for line in f:
            s = line.strip().split(", ")
            d2[s[0]] = (s[1])
            
# print(d)
# print(d2)

while True:
    print("Please choose two cities listed below. One city will be the starting point and one city will be the destination. Be sure to enter as listed below:")
    print("kansascity")
    print("minneapolis")
    print("stlouis")
    print("milwaukee")
    print("chicago")
    print("indianapolis")
    print("cincinnati")
    print("detroit")
    print("cleveland")
    start = input("Which midwestern city would you like to start in?")
    finish = input("Which city would you like to travel to?:")

    inpStr = start + " " + finish
    print(AStar(inpStr))
    # print(d2[inpStr])
    break
