class StudentGrade:
    def __init__(self, student_name, grade_value):
        self.__student_name = student_name
        self.__grade_value = grade_value

    def get_student_name(self):
        return self.__student_name

    def get_grade_value(self):
        return self.__grade_value

    def __str__(self):
        return f"Student: {self.__student_name}, Grade: {self.__grade_value}"


class StudentAverage:
    def __init__(self, student_name, average_grade):
        self.__student_name = student_name
        self.__average_grade = average_grade

    def get_student_name(self):
        return self.__student_name

    def get_average_grade(self):
        return self.__average_grade

    def __str__(self):
        return f"Student: {self.__student_name}, Average: {self.__average_grade}"


class CourseStudentCount:
    def __init__(self, course_name, student_count):
        self.__course_name = course_name
        self.__student_count = student_count

    def get_course_name(self):
        return self.__course_name

    def get_student_count(self):
        return self.__student_count

    def __str__(self):
        return f"Course: {self.__course_name}, Students: {self.__student_count}"
