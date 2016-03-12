import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

ramona_and_beezus = media.Movie("Ramona and Beezus",
                                 "A Story of two sisters",
                                 "http://a3.mzstatic.com/us/r30/Video3/v4/0e/7b/b3/0e7bb3a9-096b-b09c-4cf7-f1deb9eeb2f9/poster227x227.jpeg",
                                 "https://www.youtube.com/watch?v=6yG4oBdWONM")

eega = media.Movie("Eega",
                   "Rebirth of a person as a housefly to take revenge and help his lover survive",
                   "http://moviegalleri.net/wp-content/gallery/eega-movie-wallpapers/ss_rajamouli_eega_movie_wallpapers_posters_nani_samantha_sudeep_9246.jpg",
                   "https://www.youtube.com/watch?v=lbWURFD4vdE")

movies = [toy_story, ramona_and_beezus, eega]

fresh_tomatoes.open_movies_page(movies)
