from domain.movie import Movie
from repository.movie_repo import MovieRepo


def test_add_movie():
    test_repo = MovieRepo()
    assert len(test_repo.get_all_movies()) == 0
    movie = Movie("1", "Dune", "action")
    test_repo.add_movie(movie)
    assert len(test_repo.get_all_movies()) == 1
    movie2 = Movie("2", "Dune 2", "action")
    test_repo.add_movie(movie2)
    assert len(test_repo.get_all_movies()) == 2


def test_delete_movie():
    test_repo = MovieRepo()
    movie = Movie("1", "Dune", "action")
    test_repo.add_movie(movie)
    movie2 = Movie("2", "Dune 2", "action")
    test_repo.add_movie(movie2)
    assert len(test_repo.get_all_movies()) == 2

    test_repo.delete_movie("2")
    assert len(test_repo.get_all_movies()) == 1
    assert test_repo.get_all_movies()[0].get_id() == "1"

    test_repo.delete_movie("1")
    assert len(test_repo.get_all_movies()) == 0


def test_update_movie():
    pass


