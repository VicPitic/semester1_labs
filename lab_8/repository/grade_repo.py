class RepositoryException(Exception):
    pass

class GradeRepo:
    def __init__(self):
        """
        Initializes the grade repository with an empty list of grades.
        """
        self._grades = []

    def store(self, grade):
        """
        Stores a grade in the repository.
        :param grade: The grade to store.
        :raises RepositoryException: If a grade for the same student and course already exists.
        """
        if self.find(grade.get_student_id(), grade.get_course_id()) is not None:
            raise RepositoryException("Grade already assigned for this student and course!")
        self._grades.append(grade)

    def find(self, student_id, course_id):
        """
        Finds a grade by student ID and course ID.
        :param student_id: The ID of the student.
        :param course_id: The ID of the course.
        :return: The grade object if found, None otherwise.
        """
        for grade in self._grades:
            if grade.get_student_id() == student_id and grade.get_course_id() == course_id:
                return grade
        return None

    def get_all(self):
        """
        Returns all grades in the repository.
        :return: A list of all grades.
        """
        return self._grades
