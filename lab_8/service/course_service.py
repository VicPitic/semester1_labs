from domain.course import Course

class CourseService:
    def __init__(self, course_repo, validator):
        """
        Initializes the course service.
        :param course_repo: The course repository.
        :param validator: The course validator.
        """
        self.__course_repo = course_repo
        self.__validator = validator

    def add_course(self, course_id, name, professor):
        """
        Adds a new course.
        :param course_id: The ID of the course.
        :param name: The name of the course.
        :param professor: The professor of the course.
        :raises ValidatorException: If the course data is invalid.
        :raises RepositoryException: If the course already exists.
        """
        course = Course(course_id, name, professor)
        self.__validator.validate(course)
        self.__course_repo.store(course)

    def delete_course(self, course_id):
        """
        Deletes a course by ID.
        :param course_id: The ID of the course to delete.
        :raises RepositoryException: If the course does not exist.
        """
        self.__course_repo.delete(course_id)

    def update_course(self, course_id, name, professor):
        """
        Updates a course's name and professor.
        :param course_id: The ID of the course to update.
        :param name: The new name of the course.
        :param professor: The new professor of the course.
        :raises ValidatorException: If the course data is invalid.
        :raises RepositoryException: If the course does not exist.
        """
        course = Course(course_id, name, professor)
        self.__validator.validate(course)
        self.__course_repo.update(course)

    def find_course(self, course_id):
        """
        Finds a course by ID.
        :param course_id: The ID of the course to find.
        :return: The course object if found, None otherwise.
        """
        return self.__course_repo.find(course_id)

    def get_all_courses(self):
        """
        Returns all courses.
        :return: A list of all courses.
        """
        return self.__course_repo.get_all()

    def search_courses(self, name_part):
        """
        Searches for courses whose name contains the given string (case-insensitive).
        :param name_part: The string to search for in course names.
        :return: A list of matching courses.
        """
        all_courses = self.get_all_courses()
        filtered_courses = [c for c in all_courses if name_part.lower() in c.get_name().lower()]
        return filtered_courses
