from domain.grade import Grade
from domain.report_models import StudentGrade, StudentAverage, CourseStudentCount

class GradeService:
    def __init__(self, grade_repo, student_repo, course_repo, validator):
        """
        Initializes the grade service.
        :param grade_repo: The grade repository.
        :param student_repo: The student repository.
        :param course_repo: The course repository.
        :param validator: The grade validator.
        """
        self.__grade_repo = grade_repo
        self.__student_repo = student_repo
        self.__course_repo = course_repo
        self.__validator = validator

    def assign_grade(self, student_id, course_id, grade_value, date):
        """
        Assigns a grade to a student for a course.
        :param student_id: The ID of the student.
        :param course_id: The ID of the course.
        :param grade_value: The value of the grade.
        :param date: The date the grade was assigned.
        :raises ValueError: If the student or course does not exist.
        :raises ValidatorException: If the grade data is invalid.
        :raises RepositoryException: If the grade already exists.
        """
        if self.__student_repo.find(student_id) is None:
            raise ValueError("Student does not exist!")
        if self.__course_repo.find(course_id) is None:
            raise ValueError("Course does not exist!")

        grade = Grade(student_id, course_id, grade_value, date)
        self.__validator.validate(grade)
        self.__grade_repo.store(grade)

    def get_all_grades(self):
        """
        Returns all grades.
        :return: A list of all grades.
        """
        return self.__grade_repo.get_all()

    def get_students_for_course_report(self, course_id):
        """
        Returns a list of students and their grades for a given course.
        """
        if self.__course_repo.find(course_id) is None:
            raise ValueError("Course does not exist!")
        
        grades = self.__grade_repo.get_all()
        report = []
        for grade in grades:
            if grade.get_course_id() == course_id:
                student = self.__student_repo.find(grade.get_student_id())
                if student is not None:
                    report.append(StudentGrade(student.get_name(), grade.get_grade_value()))
        return report

    def get_most_popular_courses_report(self):
        """
        Returns the top 3 most popular courses.
        """
        grades = self.__grade_repo.get_all()
        course_counts = {}
        for grade in grades:
            c_id = grade.get_course_id()
            if c_id not in course_counts:
                course_counts[c_id] = 0
            course_counts[c_id] += 1
        
        result = []
        for c_id, count in course_counts.items():
            course = self.__course_repo.find(c_id)
            if course is not None:
                result.append(CourseStudentCount(course.get_name(), count))
            
        # Sort by count descending
        result.sort(key=lambda x: x.get_student_count(), reverse=True)
        return result[:3]

    def get_top_students_report(self):
        """
        Returns the top 20% students by average grade.
        """
        grades = self.__grade_repo.get_all()
        student_grades = {}
        for grade in grades:
            s_id = grade.get_student_id()
            if s_id not in student_grades:
                student_grades[s_id] = []
            student_grades[s_id].append(grade.get_grade_value())
            
        result = []
        for s_id, g_list in student_grades.items():
            avg = sum(g_list) / len(g_list)
            student = self.__student_repo.find(s_id)
            if student is not None:
                result.append(StudentAverage(student.get_name(), avg))
            
        # Sort by average descending
        result.sort(key=lambda x: x.get_average_grade(), reverse=True)
        
        count = int(len(result) * 0.2)
        if count == 0 and len(result) > 0:
            count = 1
            
        return result[:count]
