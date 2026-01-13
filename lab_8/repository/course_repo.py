class RepositoryException(Exception):
    pass

class CourseRepo:
    def __init__(self):
        """
        Initializes the course repository with an empty list of courses.
        """
        self._courses = []

    def store(self, course):
        """
        Stores a course in the repository.
        :param course: The course to store.
        :raises RepositoryException: If a course with the same ID already exists.
        """
        if self.find(course.get_course_id()) is not None:
            raise RepositoryException("Course already exists!")
        self._courses.append(course)

    def find(self, course_id):
        """
        Finds a course by its ID.
        :param course_id: The ID of the course to find.
        :return: The course object if found, None otherwise.
        """
        for course in self._courses:
            if course.get_course_id() == course_id:
                return course
        return None

    def update(self, course):
        """
        Updates an existing course in the repository.
        :param course: The course object with updated information.
        :raises RepositoryException: If the course does not exist.
        """
        existing_course = self.find(course.get_course_id())
        if existing_course is None:
            raise RepositoryException("Course does not exist!")
        existing_course.set_name(course.get_name())
        existing_course.set_professor(course.get_professor())

    def delete(self, course_id):
        """
        Deletes a course from the repository by its ID.
        :param course_id: The ID of the course to delete.
        :raises RepositoryException: If the course does not exist.
        """
        course = self.find(course_id)
        if course is None:
            raise RepositoryException("Course does not exist!")
        self._courses.remove(course)

    def get_all(self):
        """
        Returns all courses in the repository.
        :return: A list of all courses.
        """
        return self._courses
