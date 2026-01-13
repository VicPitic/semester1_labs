from domain.student import Student
from domain.course import Course
from domain.grade import Grade
from domain.validation import StudentValidator, CourseValidator, GradeValidator, ValidatorException

def test_student_creation():
    s = Student(1, "John")
    assert s.get_student_id() == 1
    assert s.get_name() == "John"

def test_student_validation():
    validator = StudentValidator()
    s = Student(-1, "")
    try:
        validator.validate(s)
        assert False
    except ValidatorException:
        pass

def test_course_creation():
    c = Course(1, "Math", "Prof. X")
    assert c.get_course_id() == 1
    assert c.get_name() == "Math"
    assert c.get_professor() == "Prof. X"

def test_course_validation():
    validator = CourseValidator()
    c = Course(-1, "", "")
    try:
        validator.validate(c)
        assert False
    except ValidatorException:
        pass

def test_grade_creation():
    g = Grade(1, 1, 9.5, "2023-10-10")
    assert g.get_grade_value() == 9.5

def test_grade_validation():
    validator = GradeValidator()
    g = Grade(1, 1, 11, "")
    try:
        validator.validate(g)
        assert False
    except ValidatorException:
        pass

def run_domain_tests():
    test_student_creation()
    test_student_validation()
    test_course_creation()
    test_course_validation()
    test_grade_creation()
    test_grade_validation()
