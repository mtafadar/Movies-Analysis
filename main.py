#Name: Mosrour Tafadar 
#University of Illinois at Chicago
# Fall 2022 





import sqlite3
import objecttier

##################################################################  
# 
# retrieve_stations
#
def retrieve_movie(dbConn):
    movie_pattern = input("Enter movie name (wildcards _ and % supported): ")
  
    movie_name_values = objecttier.get_movies(dbConn, movie_pattern);
    num_movie_found = len(movie_name_values);
    print();
    print("# of movies found:", num_movie_found )
  
    if(movie_name_values == None or num_movie_found == 0):
      print();
      return;
    
    elif(num_movie_found > 100):
      print("There are too many movies to display, please narrow your search and try again...");
      print();
      return;

    else:  
      for  movie in movie_name_values:
        print(movie.Movie_ID, ": ", movie.Title, "(" + movie.Release_Year + ")" )
      print();   

  
    
def retrieve_movie_details(dbConn):
  
  movie_id = input("Enter  movie id: "); 
  print();
  movie_details_values = objecttier.get_movie_details(dbConn, movie_id );
  
  if(movie_details_values == None):
      print("No such movie...");
      

  #  print("  # of stops:", f"{fetchStops[0]:,}")
  else:  
    print(movie_details_values.Movie_ID, ":", movie_details_values.Title);
    print("   Release date:", movie_details_values.Release_Date);
    print("   Runtime:", movie_details_values.Runtime, "(mins)");
    print("   Orig language:", movie_details_values.Original_Language);
    #print("   Budget:", "$"+str(movie_details_values.Budget),"(USD)");
    print("   Budget:", "$"+  f"{movie_details_values.Budget:,}", "(USD)" )
    print("   Revenue:", "$"+  f"{movie_details_values.Revenue:,}", "(USD)" )
    #print("   Revenue:", "$"+str(movie_details_values.Revenue),"(USD)");
    print("   Num reviews:", movie_details_values.Num_Reviews);
    average_rating = "{:.2f}".format(movie_details_values.Avg_Rating)
    print("   Avg rating:",average_rating , "(0..10)");
    #print("   Genres:", movie_details_values.Genres);
    genres_value = movie_details_values.Genres
    print("   Genres: ", end ='')
    for val in genres_value:
      print(val + ", " , end ='' );
    print();
  
    print("   Production companies: ",end ='' )
    production_companies_value =movie_details_values.Production_Companies;
  
    for prod in production_companies_value:
      print(prod + ", " , end ='' )
  
    print();
  
    print("   Tagline:", movie_details_values.Tagline);
  
  print();
  



def retrieve_N_movie_with_reviews(dbConn):
  
  n = int(input("N? "))
  if(n <= 0):
    print("Please enter a positive value for N...");
    print();
    return;
 
  min_reviews = int(input("min number of reviews? "))
  if(min_reviews  <= 0):
    print("Please enter a positive value for min number of reviews...");
    print ();
    return;
  print();

  movies_with_min_reviews = objecttier.get_top_N_movies(dbConn, n, min_reviews  );

  if(movies_with_min_reviews == None or len(movies_with_min_reviews)== 0):
    print();
    return
 
  for movie in movies_with_min_reviews: 
    average_rating = "{:.2f}".format(movie.Avg_Rating)
    print(movie.Movie_ID, ":", movie.Title, "(" + movie.Release_Year + ")" + ",", "avg rating =", average_rating, "("+ str(movie.Num_Reviews), "reviews)");
  print();
    
  


def insert_rating(dbConn):
  rating = int(input("Enter rating (0..10): "))
  if(rating < 0 or rating > 10):
    print("Invalid rating...")
    print()
    return

  movie_id = int(input("Enter  movie id: "))

  

  
  inserting_rating = objecttier.add_review(dbConn, movie_id, rating);

  if(inserting_rating  == 1):
    print()
    print("Review successfully inserted")
    print();
    return

  if(inserting_rating == 0):
    print();
    print("No such movie...")
    print()
    return


def set_tagline(dbConn):
  tag =  input("tagline? ");
  movie_id = int(input("movie id? "))
  set_tagline = objecttier.set_tagline(dbConn, movie_id, tag);

  if(set_tagline ==  0):
    print()
    print("No such movie...")
    print()
    return

  if(set_tagline == 1):
    print()
    print("Tagline successfully set")
    print()
    return
  

  

  
  

  

  

  
  



  
##################################################################  
#
# main
#
print('** Welcome to the MovieLens app **')
dbConn = sqlite3.connect('MovieLens.db')
print();

print("General stats:")

num_movies = objecttier.num_movies(dbConn)
print("  # of movies:", f"{ num_movies:,}")

num_reviews = objecttier.num_reviews(dbConn)
print("  # of reviews:", f"{ num_reviews:,}")
print();

cmd = input("Please enter a command (1-5, x to exit): ")
while cmd != "x":
    if cmd == "1":
      print()
      retrieve_movie(dbConn)
    if(cmd == "2"):
      print();
      retrieve_movie_details(dbConn);

    if(cmd == "3"):
      print()
      retrieve_N_movie_with_reviews(dbConn)

    if(cmd == "4"):
      print();
      insert_rating(dbConn)

    if(cmd == "5"):
      print();
      set_tagline(dbConn)
      
    cmd = input("Please enter a command (1-5, x to exit): ")

