from domain.student import Student

class StudentService:
    def __init__(self, student_repo, validator):
        """
        Initializes the student service.
        :param student_repo: The student repository.
        :param validator: The student validator.
        """
        self.__student_repo = student_repo
        self.__validator = validator

    def add_student(self, student_id, name):
        """
        Adds a new student.
        :param student_id: The ID of the student.
        :param name: The name of the student.
        :raises ValidatorException: If the student data is invalid.
        :raises RepositoryException: If the student already exists.
        """
        student = Student(student_id, name)
        self.__validator.validate(student)
        self.__student_repo.store(student)

    def delete_student(self, student_id):
        """
        Deletes a student by ID.
        :param student_id: The ID of the student to delete.
        :raises RepositoryException: If the student does not exist.
        """
        self.__student_repo.delete(student_id)

    def update_student(self, student_id, name):
        """
        Updates a student's name.
        :param student_id: The ID of the student to update.
        :param name: The new name of the student.
        :raises ValidatorException: If the student data is invalid.
        :raises RepositoryException: If the student does not exist.
        """
        student = Student(student_id, name)
        self.__validator.validate(student)
        self.__student_repo.update(student)

    def find_student(self, student_id):
        """
        Finds a student by ID.
        :param student_id: The ID of the student to find.
        :return: The student object if found, None otherwise.
        """
        return self.__student_repo.find(student_id)

    def get_all_students(self):
        """
        Returns all students.
        :return: A list of all students.
        """
        return self.__student_repo.get_all()

    def search_students(self, name_part):
        """
        Searches for students whose name contains the given string (case-insensitive).
        :param name_part: The string to search for in student names.
        :return: A list of matching students.
        """
        all_students = self.get_all_students()
        filtered_students = [s for s in all_students if name_part.lower() in s.get_name().lower()]
        return filtered_students
