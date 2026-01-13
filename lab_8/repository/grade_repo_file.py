from domain.grade import Grade
from repository.grade_repo import GradeRepo

class GradeFileRepo(GradeRepo):
    def __init__(self, filename):
        """
        Initializes the grade file repository.
        :param filename: The name of the file to store data in.
        """
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads grades from the file.
        """
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line == "":
                        continue
                    parts = line.split(",")
                    grade = Grade(int(parts[0]), int(parts[1]), float(parts[2]), parts[3])
                    super().store(grade)
        except FileNotFoundError:
            pass

    def __write_to_file(self):
        """
        Writes all grades to the file.
        """
        with open(self.__filename, "w") as f:
            for grade in self.get_all():
                f.write(f"{grade.get_student_id()},{grade.get_course_id()},{grade.get_grade_value()},{grade.get_date()}\n")

    def store(self, grade):
        """
        Stores a grade in the repository and saves to file.
        :param grade: The grade to store.
        """
        super().store(grade)
        self.__write_to_file()
