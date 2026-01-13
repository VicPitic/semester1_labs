from domain.student import Student
from domain.course import Course
from domain.grade import Grade

class ValidatorException(Exception):
    pass

class StudentValidator:
    def validate(self, student):
        """
        Validates a student object.
        :param student: The student object to validate.
        :raises ValidatorException: If the student ID is negative or the name is empty.
        """
        errors = ""
        if student.get_student_id() < 0:
            errors += "Invalid ID!\n"
        if student.get_name() == "":
            errors += "Name cannot be empty!\n"
        if len(errors) > 0:
            raise ValidatorException(errors)

class CourseValidator:
    def validate(self, course):
        """
        Validates a course object.
        :param course: The course object to validate.
        :raises ValidatorException: If the course ID is negative, the name is empty, or the professor is empty.
        """
        errors = ""
        if course.get_course_id() < 0:
            errors += "Invalid ID!\n"
        if course.get_name() == "":
            errors += "Name cannot be empty!\n"
        if course.get_professor() == "":
            errors += "Professor cannot be empty!\n"
        if len(errors) > 0:
            raise ValidatorException(errors)

class GradeValidator:
    def validate(self, grade):
        """
        Validates a grade object.
        :param grade: The grade object to validate.
        :raises ValidatorException: If the grade value is not between 1 and 10, or the date is empty.
        """
        errors = ""
        if grade.get_grade_value() < 1 or grade.get_grade_value() > 10:
            errors += "Grade must be between 1 and 10!\n"
        if grade.get_date() == "":
            errors += "Date cannot be empty!\n"
        if len(errors) > 0:
            raise ValidatorException(errors)
