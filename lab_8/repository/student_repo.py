class RepositoryException(Exception):
    pass

class StudentRepo:
    def __init__(self):
        """
        Initializes the student repository with an empty list of students.
        """
        self._students = []

    def store(self, student):
        """
        Stores a student in the repository.
        :param student: The student to store.
        :raises RepositoryException: If a student with the same ID already exists.
        """
        if self.find(student.get_student_id()) is not None:
            raise RepositoryException("Student already exists!")
        self._students.append(student)

    def find(self, student_id):
        """
        Finds a student by their ID.
        :param student_id: The ID of the student to find.
        :return: The student object if found, None otherwise.
        """
        for student in self._students:
            if student.get_student_id() == student_id:
                return student
        return None

    def update(self, student):
        """
        Updates an existing student in the repository.
        :param student: The student object with updated information.
        :raises RepositoryException: If the student does not exist.
        """
        existing_student = self.find(student.get_student_id())
        if existing_student is None:
            raise RepositoryException("Student does not exist!")
        existing_student.set_name(student.get_name())

    def delete(self, student_id):
        """
        Deletes a student from the repository by their ID.
        :param student_id: The ID of the student to delete.
        :raises RepositoryException: If the student does not exist.
        """
        student = self.find(student_id)
        if student is None:
            raise RepositoryException("Student does not exist!")
        self._students.remove(student)

    def get_all(self):
        """
        Returns all students in the repository.
        :return: A list of all students.
        """
        return self._students
