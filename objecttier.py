#
# File: objecttier.py
#
# Builds Movie-related objects from data retrieved through 
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:
  def __init__(self, id, title, r_year):
    self._Movie_ID = id;
    self._Title = title;
    self._Release_Year = r_year

  @property 
  def Movie_ID(self):
    return self._Movie_ID; 

  @property
  def Title(self):
    return self._Title;

  @property
  def Release_Year(self):
    return self._Release_Year;

    
##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:
  def __init__(self, id, title, r_year, n_reviews, avg_rating):
    self._Movie_ID = id
    self._Title = title
    self._Release_Year = r_year
    self._Num_Reviews = n_reviews
    self._Avg_Rating =avg_rating

  @property 
  def Movie_ID(self):
    return self._Movie_ID;

  @property 
  def Title(self):
    return self._Title;

  @property
  def Release_Year(self):
    return self._Release_Year;

  @property
  def Num_Reviews(self):
    return self._Num_Reviews; 
     
    


    
    
    


##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:
  def __init__(self,  id, title, r_date,  runtime, o_language, budget, revenue,  num_reviews, avg_rating, tagline, genres, production_companies):
    self._Movie_ID = id;
    self._Title = title
    self._Release_Date = r_date;
    self._Runtime = runtime
    self._Original_Language = o_language;
    self._Budget = budget;
    self._Revenue = revenue;
    self._Num_Reviews = num_reviews;
    self._Avg_Rating = avg_rating;
    self._Tagline = tagline;
    self._Genres = genres;
    self._Production_Companies = production_companies;

  @property
  def Movie_ID(self):
    return self._Movie_ID;

  @property
  def Title(self):
    return self._Title;

  @property
  def Release_Date(self):
    return self._Release_Date;

  @property 
  def Runtime(self):
    return self._Runtime;

  @property
  def Original_Language(self):
    return self._Original_Language;

  @property
  def Budget(self):
    return self._Budget;

  @property
  def Revenue(self):
    return self._Revenue;

  @property 
  def Num_Reviews(self):
    return self._Num_Reviews;

  @property 
  def Avg_Rating(self):
    return self._Avg_Rating;

  @property 
  def Tagline(self):
    return self._Tagline;

  @property
  def Genres(self):
    return  self._Genres;
  @property
  def Production_Companies(self):
    return self._Production_Companies; 
  
    

    

    

##################################################################
# 
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  try:
    sql = """select count(Movie_ID) from  Movies;"""
    row = datatier.select_one_row(dbConn, sql);
    if row is None:
      return [];
    return row[0];
  except Exception as err:
    print("Error in num_movies", err)
    return -1;
    
    

  
  
   


##################################################################
# 
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
   try: 
     sql = """select count(Rating) from  Ratings;"""
     row = datatier.select_one_row(dbConn, sql);
     if row is None:
      return []
     return  row[0];
   except Exception as err:
     print("Error in num_reviews:", err)
     return -1;
   
    
  
   

  


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
   sql = """Select Movie_ID, Title, strftime('%Y',Release_Date)  from Movies
Where Title like ?
Order by Title ASC"""

   rows = datatier.select_n_rows(dbConn, sql, [pattern])
   movie_names = [];
   for row in rows:
     movie = Movie(row[0], row[1], row[2])
     movie_names.append(movie);
   return movie_names;
     
  

  

  
  


##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  sql = """
   Select M.Movie_ID, Title, Date(Release_Date), Runtime, 
original_Language, Budget, Revenue,  count(Rating), Avg(Rating), Tagline
From  Movies M
left join Ratings  on  M.Movie_ID = Ratings.Movie_ID
left join Movie_Taglines on M.Movie_ID = Movie_Taglines.Movie_ID
Where M.Movie_ID = ?;
  """

  sql2 = """
    Select   group_concat(distinct (Genre_Name)),  group_concat(distinct(Company_Name)) From Movies M 
left join  Movie_Genres  on M.Movie_ID = Movie_Genres.Movie_ID
left Join Genres on Movie_Genres.Genre_ID = Genres.Genre_ID
left join  Movie_Production_Companies on  M.Movie_ID = Movie_Production_Companies.Movie_ID
left join Companies on  Movie_Production_Companies.Company_ID = Companies.Company_ID
Where M.Movie_ID = ?;
  """

  rows1 = datatier.select_one_row(dbConn, sql, [movie_id]);
  rows2 = datatier.select_n_rows(dbConn, sql2, [movie_id]); 


  if(rows1[0] == None):
    return None;
  
  if(len(rows1) == 0):
    return None;

  if(len(rows2) == 0):
    return None;

  mylist =  (0, 0.0);

  if rows1[8] is None:
    mylist=0.0;
  else:
    mylist = rows1[8];
  
  if(rows1[9] == None):
    tagline = ""
    
  else:
    tagline = rows1[9];

  mylist2 = [];

  if(rows2[0][0] == None):
      mylist2 = [];

  else:
    for r in rows2:
      val = r[0].split(",");
      for j in val:
       mylist2.append(j);
      
  mylist2.sort();
  mylist3 = [];

  if(rows2[0][1] == None):
    mylist3 = [];
  else:
    for r2 in rows2:
      val = r[1].split(",");
      for j in val:
       mylist3.append(j);
      
    mylist3.sort();

  movie_d = MovieDetails(rows1[0], rows1[1], rows1[2], rows1[3], rows1[4], rows1[5], rows1[6], rows1[7], mylist, tagline,mylist2, mylist3)
  
  return movie_d; 

       

##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average 
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error 
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
   
    


##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
   pass


##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively 
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
   pass
