import random
def movies():
    movies=['The call of the wild',       "The Dark Knight",
            "The Dark Knight Rises",      "The Godfather",
            "Toy Story four",             " Avengers Endgame",
            "kahaani",                    "Titanic",
            "three idiots",               "Once Upon a Time in Mumbai",
            "Chennai Express",            "Delhi Belly",
            "Chandani Chowk to China",    "munna bhai mbbs"]

    a=random.choice(movies)
    return a.lower()
