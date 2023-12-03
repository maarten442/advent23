import re

"""
The exampel input of a game look like:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

We start with the known configuration of cubes in the bag, and we want to find
out which games are possible, and which ones are not. 


"""

config_start = {"red": 12, "green": 13, "blue": 14}

test = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
testing = test.split(":")[1].split(";")


print(testing)