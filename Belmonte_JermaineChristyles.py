"""
Midterm Practical Exam — Movie Collection Manager
Student: Jermaine Christyles A. Belmonte
"""

movies = []

def display_menu(self):
    # print the menu
    print(" === Movie Collection Manager === ")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs. unwatched")
    print("4. Find a movie")
    print("5. Exit")

    # return the user's choice
    self.user_option = input("Choose an option: ")
    return self.user_option


def add_movie(movie_list):
    # ask for title, director, and status
    Movie = input("Enter movie title: ")
    Director = input("Enter director: ")
    Status = input("Enter status (Watched/Unwatched): ")
    # build the movie string
    movielist = (Movie, Director, Status)
    movies.append(movielist)
    # add it to the list
    print("Movie Added Successfully")


def view_movies(movie_list):
    # loop through and print every movie
    for x in movies: 
        print(x)
    # handle empty list
    

def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()

display_menu(display_menu)
if display_menu.user_option == "1":
    add_movie(add_movie)
        
elif display_menu.user_option == "2":
    view_movies(view_movies)
