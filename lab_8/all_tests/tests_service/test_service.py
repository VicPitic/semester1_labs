from service.student_service import StudentService
from repository.student_repo import StudentRepo
from domain.validation import StudentValidator

def test_student_service():
    repo = StudentRepo()
    validator = StudentValidator()
    service = StudentService(repo, validator)

    service.add_student(1, "John")
    assert len(service.get_all_students()) == 1

    service.update_student(1, "Jane")
    assert service.find_student(1).get_name() == "Jane"

    service.delete_student(1)
    assert len(service.get_all_students()) == 0

def run_service_tests():
    test_student_service()
