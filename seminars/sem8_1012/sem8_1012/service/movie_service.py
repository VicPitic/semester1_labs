from domain.movie import Movie
from domain.validation import MovieValidator
from repository.movie_repo import MovieRepo


class MovieService:
    def __init__(self, movie_repo: MovieRepo, movie_validator: MovieValidator):
        self.__movie_repo = movie_repo
        self.__movie_validator = movie_validator

    def add_movie(self, id, name, genre):
        """
        Adds a movie with given parameters
        :param id: movie id
        :param name: movie name
        :param genre: movie genre
        :return: -
        """
        movie = Movie(id, name, genre)
        self.__movie_validator.validate_movie(movie)
        self.__movie_repo.add_movie(movie)

    def delete_movie(self, id):
        """
        Deletes a movie by id
        :param id: the id of the movie to be deleteed
        :return: -
        """
        self.__movie_repo.delete_movie(id)

    def get_movie_by_id(self, id):
        """
        Get a movie by given id
        :param id: given id
        :return: found movie
        """

        return self.__movie_repo.get_movie_by_id(id)

    def get_all_movies(self):
        """
        Get the list with all movies
        :return: a list with all movies
        """
        return self.__movie_repo.get_all_movies()





