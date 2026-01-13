from service.grade_service import GradeService
from repository.student_repo import StudentRepo
from repository.course_repo import CourseRepo
from repository.grade_repo import GradeRepo
from domain.validation import GradeValidator
from domain.student import Student
from domain.course import Course
from domain.grade import Grade

def test_reports():
    student_repo = StudentRepo()
    course_repo = CourseRepo()
    grade_repo = GradeRepo()
    validator = GradeValidator()
    service = GradeService(grade_repo, student_repo, course_repo, validator)

    # Setup data
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    s3 = Student(3, "Charlie")
    s4 = Student(4, "David")
    s5 = Student(5, "Eve")
    
    student_repo.store(s1)
    student_repo.store(s2)
    student_repo.store(s3)
    student_repo.store(s4)
    student_repo.store(s5)

    c1 = Course(101, "Math", "Prof. X")
    c2 = Course(102, "Physics", "Prof. Y")
    c3 = Course(103, "Chemistry", "Prof. Z")
    c4 = Course(104, "Biology", "Prof. W")

    course_repo.store(c1)
    course_repo.store(c2)
    course_repo.store(c3)
    course_repo.store(c4)

    # Assign grades
    # Course 1: Alice (10), Bob (9)
    service.assign_grade(1, 101, 10, "2023-01-01")
    service.assign_grade(2, 101, 9, "2023-01-01")

    # Course 2: Alice (8), Charlie (7), David (6)
    service.assign_grade(1, 102, 8, "2023-01-02")
    service.assign_grade(3, 102, 7, "2023-01-02")
    service.assign_grade(4, 102, 6, "2023-01-02")

    # Course 3: Bob (10)
    service.assign_grade(2, 103, 10, "2023-01-03")

    # Test 1: Students for Course 101
    report_c1 = service.get_students_for_course_report(101)
    assert len(report_c1) == 2
    # Check content (Alice, 10), (Bob, 9)
    names = [item.get_student_name() for item in report_c1]
    assert "Alice" in names
    assert "Bob" in names

    # Test 2: Popular Courses
    # C102: 3 students, C101: 2 students, C103: 1 student, C104: 0
    popular = service.get_most_popular_courses_report()
    assert len(popular) == 3
    assert popular[0].get_course_name() == "Physics" # 3 students
    assert popular[0].get_student_count() == 3
    assert popular[1].get_course_name() == "Math" # 2 students
    assert popular[2].get_course_name() == "Chemistry" # 1 student

    # Test 3: Top 20% Students
    # Averages:
    # Alice: (10+8)/2 = 9
    # Bob: (9+10)/2 = 9.5
    # Charlie: 7
    # David: 6
    # Eve: 0 (no grades) - usually not in report if no grades? My implementation iterates over grades, so Eve won't be there.
    # Students with grades: 4. Top 20% of 4 is 0.8 -> 1 student.
    # Top student should be Bob (9.5).
    
    top_students = service.get_top_students_report()
    assert len(top_students) == 1
    assert top_students[0].get_student_name() == "Bob"
    assert top_students[0].get_average_grade() == 9.5

def run_reports_tests():
    test_reports()
