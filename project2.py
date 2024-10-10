
Movies= [
    ["Title", "Rating", "Genre"],
    ['The Grand Budapest Hotel', 91, "Comedy/Drama"],
    ['Mad Max: Fury Road', 97, "Action/Adventure"],
    ["Inside Out", 99, "Animation/Family"],
    ["Get Out", 98, "Horror/Thriller"],
    ["The Social Network", 96, "Biography/Drama"],
    ["Parasite", 98, "Thriller/Drama"],
    ["Pulp Fiction", 92, "Crime/Drama"],

]
movies = Movies

Movies[1] = ["A Quiet Place", 95, 'Horror/Thriller']
Movies.append(["La La Land", 91, "Musical/Romance"])
#print(Movies)

for i in range(1,8):
    print(Movies[i][0])

print(" ")

ratings = [0, (Movies[1][1]), (Movies[2][1]), (Movies[3][1]), (Movies[4][1]), (Movies[5][1]), (Movies[6][1]), (Movies[7][1]), (Movies[8][1]), ]
genres = [0, (Movies[1][2]), (Movies[2][2]), (Movies[3][2]), (Movies[4][2]), (Movies[5][2]), (Movies[6][2]), (Movies[7][2]), (Movies[8][2]), ]

total_rating = 0

for rating in ratings:
    total_rating += rating
print("Total Rating:", total_rating)

print(" ")

for i in range(1,8):
    print(Movies[i][0],"has a rating of", ratings[i] )

print(' ')

highest_rating = max(ratings)
index = ratings.index(highest_rating)
print("The highest rated movie is:", Movies[index])

print(' ')

def calculate_average_rating(ratings):
    total = sum(ratings)
    return round(total / len(ratings))
average = calculate_average_rating(ratings)
print('Average Rating:', average)

print(' ')

def find_highest_rated(movies, ratings):
    highest_rating = max(ratings)
    index = ratings.index(highest_rating)
    return Movies[index]

top_movie = find_highest_rated(movies, ratings)
print('Top Rated Movie:', top_movie)

def filter_by_genre(genrename):
 filtered_movies = []
 for i in range(1,8):
    genre = genrename
    if genres[i] == genrename:
        filtered_movies.append(Movies[i])
 print('Movies filtered by genre', genre, ':', filtered_movies)

filter_by_genre('Crime/Drama')

import csv
def load_movies(filename):
    with open(filename, 'r') as file:
        movies = file.readlines()
    return [movie.strip() for movie in movies]

#EXTRA BONUS:
def save_analysis(results, filename):
    results = load_movies('action.csv')
    with open(filename, 'w') as file:
   	 file.write(results)


