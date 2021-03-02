# by Kami Bigdely
# Extract class
class User:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first = first_name
        self.last = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email


    def send_hiring_email(self, email):
        print("email sent to: ", email)

    def print_movies(self):
        for movie in self.movies:
            print(movie, end=', ')

    def custom_method(self, email):
        """Custom method that can be customized for anything."""
        print(self.first, " ", self.last)
        self.print_movies()
        print()

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

users = []    

for i, value in enumerate(emails):
    if birth_year[i] > 1985:
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
