from domain.course import Course
from repository.course_repo import CourseRepo

class CourseFileRepo(CourseRepo):
    def __init__(self, filename):
        """
        Initializes the course file repository.
        :param filename: The name of the file to store data in.
        """
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads courses from the file.
        """
        try:
            with open(self.__filename, "r") as f:
                content = f.read().strip()
               
                if content == "":
                    return
                courses_data = content.split("\n\n")
                for course_data in courses_data:
                    lines = course_data.strip().split("\n")
                    if len(lines) >= 3:
                        course = Course(int(lines[0]), lines[1], lines[2])
                        super().store(course)

        except FileNotFoundError:
            pass

    def __write_to_file(self):
        """
        Writes all courses to the file.
        """
        with open(self.__filename, "w") as f:
            courses = self.get_all()
            for i, course in enumerate(courses):
                f.write(f"{course.get_course_id()}\n{course.get_name()}\n{course.get_professor()}")
                if i < len(courses) - 1:
                    f.write("\n\n")

    def store(self, course):
        """
        Stores a course in the repository and saves to file.
        :param course: The course to store.
        """
        super().store(course)
        self.__write_to_file()

    def update(self, course):
        """
        Updates a course in the repository and saves to file.
        :param course: The course to update.
        """
        super().update(course)
        self.__write_to_file()

    def delete(self, course_id):
        """
        Deletes a course from the repository and saves to file.
        :param course_id: The ID of the course to delete.
        """
        super().delete(course_id)
        self.__write_to_file()
