"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    martian = media.Movie("The Martian",
                          "A man is stuck on Mars",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/"
                          "The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=lQqhfq87FgY",
                          "October 2, 2015")

    contact = media.Movie("Contact",
                          "We make contact with aliens",
                          "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                          "https://www.youtube.com/watch?v=d9C2cF3KvP8",
                          "July 11, 1997")

    res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw",
                           "March 15, 2002")

    matrix = media.Movie("The Matrix",
                         "The world is a simulation",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "March 31, 1999")

    the_dish = media.Movie("The Dish",
                           "A film about a radio telescope",
                           "https://upload.wikimedia.org/wikipedia/en/4/4a/Thedish_poster.jpg",
                           "https://www.youtube.com/watch?v=2TAqXENo1rA",
                           "October 19, 2000")

    spectre = media.Movie("Spectre",
                          "The latest James Bond movie",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                          "https://www.youtube.com/watch?v=vBnGxAkdh_k",
                          "October 26, 2015")

    # Store the Movie objects in a list.
    movies = [martian, contact, res_evil, matrix, the_dish, spectre]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
