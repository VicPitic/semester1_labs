from domain.student import Student
from repository.student_repo import StudentRepo

class StudentFileRepo(StudentRepo):
    def __init__(self, filename):
        """
        Initializes the student file repository.
        :param filename: The name of the file to store data in.
        """
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads students from the file.
        """
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line == "":
                        continue
                    parts = line.split(",")
                    student = Student(int(parts[0]), parts[1])
                    super().store(student)
        except FileNotFoundError:
            pass

    def __write_to_file(self):
        """
        Writes all students to the file.
        """
        with open(self.__filename, "w") as f:
            for student in self.get_all():
                f.write(f"{student.get_student_id()},{student.get_name()}\n")

    def store(self, student):
        """
        Stores a student in the repository and saves to file.
        :param student: The student to store.
        """
        super().store(student)
        self.__write_to_file()

    def update(self, student):
        """
        Updates a student in the repository and saves to file.
        :param student: The student to update.
        """
        super().update(student)
        self.__write_to_file()

    def delete(self, student_id):
        """
        Deletes a student from the repository and saves to file.
        :param student_id: The ID of the student to delete.
        """
        super().delete(student_id)
        self.__write_to_file()
