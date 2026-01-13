from repository.student_repo import StudentRepo, RepositoryException
from domain.student import Student

def test_student_repo():
    repo = StudentRepo()
    s = Student(1, "John")
    repo.store(s)
    assert len(repo.get_all()) == 1
    assert repo.find(1) == s

    try:
        repo.store(s)
        assert False
    except RepositoryException:
        pass

    s2 = Student(1, "Jane")
    repo.update(s2)
    assert repo.find(1).get_name() == "Jane"

    repo.delete(1)
    assert len(repo.get_all()) == 0

def run_repo_tests():
    test_student_repo()
