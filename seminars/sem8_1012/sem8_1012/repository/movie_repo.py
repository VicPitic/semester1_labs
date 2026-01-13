# repo should contain all CRUD methods
# CRUD = CREATE (add), READ, UPDATE, DELETE
from domain.movie import Movie


class MovieRepo:
    def __init__(self):
        self.__movies = []

    def add_movie(self, movie: Movie):
        """
        Adds a movie object to the movies list
        :param movie: movie to add
        :return: -
        """
        self.__movies.append(movie)

    def get_all_movies(self):
        """
        Gets the list with all movies
        :return: list with all movies
        """
        return self.__movies

    def get_movie_by_id(self, id):
        """
        Get a movie by given id
        :param id: the id of the movie to find
        :return: the found movie, None otherwise
        """
        for movie in self.__movies:
            if movie.get_id() == id:
                return movie
        return None

    def delete_movie(self, id):
        """
        Deletes a movie by a given id
        :param id: the id of the movie to delete
        :return: -
        """

        movie_to_delete = self.get_movie_by_id(id)
        # del movie_to_delete
        if movie_to_delete:
            self.__movies.remove(movie_to_delete)

    def update_movie_by_id(self, id, new_name, new_genre):
        """
        Update a movie with given id
        :param new_name: new name
        :param new_genre: new genre
        :return: -
        """
        movie_to_update = self.get_movie_by_id(id)
        if movie_to_update:
            movie_to_update.set_name(new_name)
            movie_to_update.set_genre(new_genre)





