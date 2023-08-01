movies = [
    {"name": "sdfgh", "director": "asdf"},
    {"name": "yh", "director": "oijh"},
    {"name": "rtg", "director": "vfr"},
    {"name": "phj", "director": "sdf"},
    {"name": "tgh", "director": "kj"},
    {"name": "nhg", "director": "oiuy"},
]


def finder(helper, user_input):
    for movie in movies:
        if helper(movie) == user_input:
            print(movie)


user_choice = input("What do you want to search for ? ")
user_input = input("Please enter the term you want to search for - ")

finder(lambda movie: movie[user_choice], user_input)
