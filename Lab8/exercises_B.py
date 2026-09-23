movie_dictionary = {
    'title': 'A title',
    'director': 'A director',
    'rating': 3.2
}

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        return self.rating >= 8

movie = Movie('Movie name', 'NN', 8.7)
print(movie.is_highly_rated())  

# Directory is better whit simple logic, like small static data
# Class is better when when combining function with data or it will be used in larger programs. 