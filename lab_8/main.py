from domain.validation import StudentValidator, CourseValidator, GradeValidator
from repository.student_repo_file import StudentFileRepo
from repository.course_repo_file import CourseFileRepo
from repository.grade_repo_file import GradeFileRepo
from service.student_service import StudentService
from service.course_service import CourseService
from service.grade_service import GradeService
from ui.console import Console

def main():
    student_validator = StudentValidator()
    course_validator = CourseValidator()
    grade_validator = GradeValidator()

    student_repo = StudentFileRepo("students.txt")
    course_repo = CourseFileRepo("courses.txt")
    grade_repo = GradeFileRepo("grades.txt")

    student_service = StudentService(student_repo, student_validator)
    course_service = CourseService(course_repo, course_validator)
    grade_service = GradeService(grade_repo, student_repo, course_repo, grade_validator)

    console = Console(student_service, course_service, grade_service)
    console.run()

if __name__ == "__main__":
    main()
