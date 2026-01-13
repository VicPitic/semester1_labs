from domain.movie import Movie


class MovieValidator:
    # genre to be in action, drama, historic, romance, comedy
    def validate_movie(self, movie: Movie):
        """
        Validate a movie
        :param movie: movie to validate
        :return: -
        :raises ValueError if movie is not valid
        """
        if movie.get_genre() not in ["action", "drama", "historic", "romance", "comedy"]:
            raise ValueError("Genre should be one of: action, drama, historic, romance, comedy")


class ClientValidator:
    def validate_client(self, client):
        """
        Validate a client object. CNP must be 13 digit sequence
        Name must be at least one character
        :param client: client to validate
        :return: -
        :raises ValueError if client is not valid
        """
        if len(client.get_cnp()) != 13:
            raise ValueError("CNP must be 13 digit long")
        if not client.get_cnp().isdigit():
            raise ValueError("CNP must be a digit sequence")
        if len(client.get_name()) == 0:
            raise ValueError("Name must be one character long at least")