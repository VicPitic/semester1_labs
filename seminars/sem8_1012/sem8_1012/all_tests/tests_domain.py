from domain.movie import Movie
from domain.validation import MovieValidator


def test_create_movie():
    movie = Movie("1", "Dune", "action")
    assert movie.get_id() == "1"
    assert movie.get_name() == "Dune"
    assert movie.get_genre() == "action"


def test_domain_setters():
    movie = Movie("1", "Dune", "action")
    assert movie.get_name() == "Dune"
    movie.set_name("Dune 2")
    assert movie.get_name() == "Dune 2"
    movie.set_genre("drama")
    assert movie.get_genre() == "drama"


def test_validate_movie():
    movie = Movie("1", "Dune", "action")
    validator = MovieValidator()
    try:
        validator.validate_movie(movie)
        assert True
    except ValueError:
        assert False

    movie2 = Movie("1", "Dune", "SF")
    validator = MovieValidator()
    try:
        validator.validate_movie(movie2)
        assert False
    except ValueError:
        assert True


