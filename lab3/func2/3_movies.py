# list of Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def highrating(movies):
    return [movie['name'] for movie in movies if movie['imdb'] > 5.5]
    #print movie-name for every 'movie' in list(movies) if...


def high(movies, movie_name):
    for movie in movies:                        #search for exact movie
        if movie['name'] == movie_name:         #find that movie
            return movie['imdb'] > 5.5          #return True if >5.5
    return False                                #return False if no such movie


def category(movies, movie_cat):
    movie_names = []                            #create list with category movies
    for movie in movies:
        if movie['category'] == movie_cat:
            movie_names.append(movie['name'])
    return movie_names if movie_names else False #checks if non-empty


def average(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)


def avg_of_cat(movies, movie_cat):
    movie_names = []
    for movie in movies:
        if movie['category'] == movie_cat:
            movie_names.append(movie['name'])
    if not movie_names:
        return False  # Return False if no movies in the specified category
    return average([movie for movie in movies if movie['name'] in movie_names])

print(avg_of_cat(movies, "Romance"))