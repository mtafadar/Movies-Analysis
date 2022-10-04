#
# Program to analyze data from CTA L daily ridership database.
# This is a simplified version of the program for Project 01,
# and works mainly with stations and stops; console-based only,
# all plotting has been removed.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#
# References: 
#  learning python: https://www.w3schools.com/python/
#  sqlite programming: https://docs.python.org/3/library/sqlite3.html
#
import sqlite3
import objecttier


##################################################################  
# 
# retrieve_stations
#
def retrieve_movie(dbConn):
    print()
    limit = input("Enter movie id:  ")
    Tagline= input("Enter movie Tag:  ")

    stations = objecttier.set_tagline(dbConn, limit, Tagline)
    print(stations);
  
    
        
        

    




##################################################################  
#
# main
#
print('** Welcome to the Movie App **')

dbConn = sqlite3.connect('MovieLens.db')

print()
cmd = input("Please enter a command (1-9, x to exit): ")

while cmd != "x":
    if cmd == "1":
        retrieve_movie(dbConn)
      
    cmd = input("Please enter a command (1-9, x to exit): ")

#
# done
#
