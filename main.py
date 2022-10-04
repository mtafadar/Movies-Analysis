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
    name = input("Enter movie id:  ")

    stations = objecttier.get_movie_details(dbConn, name)
  
    if stations is None:  # error
        print("**Internal error: retrieve_stations")
    else:
        print("  Avg rating:", f"{stations.Avg_Rating:.2f}", "(0..10)")
        print("  Budget:", f"${stations.Budget:,}", "(USD)")
        print(stations.Tagline)
        

    




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
