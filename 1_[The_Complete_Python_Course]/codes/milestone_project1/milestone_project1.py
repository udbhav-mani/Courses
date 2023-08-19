USER_PROMPT = """
Enter 'a' to add a movie, 'l' to list all your movies, 'f' to find a movie by title and 'q' to quit. 
"""
movies = []


def add_movie():
    user_movie_name = input("Enter the name of the movie. ")
    user_movie_director = input("Enter the director of the movie. ")
    user_movie_rd = input("Enter the release date of the movie. ")
    movies.append(
        {
            "name": user_movie_name,
            "director": user_movie_director,
            "release_date": user_movie_rd,
        }
    )
    print("Movie added succesfully!! ")


def view_movies():
    print("List of all movies - ")
    for movie in movies:
        movie_name = movie["name"]
        movie_director = movie["director"]
        movie_rd = movie["release_date"]

        print(
            f"{movie_name}, Directed by - {movie_director} and released in {movie_rd}"
        )


def search_movie():
    movie_name = input("Enter the name of the movie. ")

    for movie in movies:
        if movie_name == movie["name"]:
            print(f"You have {movie_name} in your collection!!")
            break
    else:
        print(f"You do not have {movie_name} in your collection!!")


user_validations = {"a": add_movie, "l": view_movies, "f": search_movie}


def menu():
    user_input = input(USER_PROMPT)
    while user_input != "q":
        if user_input in user_validations:
            user_validations[user_input]()
        else:
            print("UNKNOWN COMMAND !!! ")
        user_input = input(USER_PROMPT)


menu()
