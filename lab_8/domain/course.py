class Course:
    def __init__(self, course_id, name, professor):
        """
        Initializes a course with an ID, name, and professor.
        :param course_id: The unique identifier of the course.
        :param name: The name of the course.
        :param professor: The name of the professor teaching the course.
        """
        self.__course_id = course_id
        self.__name = name
        self.__professor = professor

    def get_course_id(self):
        """
        Returns the course's ID.
        :return: The course's ID.
        """
        return self.__course_id

    def get_name(self):
        """
        Returns the course's name.
        :return: The course's name.
        """
        return self.__name

    def get_professor(self):
        """
        Returns the professor's name.
        :return: The professor's name.
        """
        return self.__professor

    def set_name(self, name):
        """
        Sets the course's name.
        :param name: The new name of the course.
        """
        self.__name = name

    def set_professor(self, professor):
        """
        Sets the professor's name.
        :param professor: The new name of the professor.
        """
        self.__professor = professor

    def __eq__(self, other):
        """
        Checks if two courses are equal based on their ID.
        :param other: The other course to compare with.
        :return: True if the courses have the same ID, False otherwise.
        """
        return self.__course_id == other.__course_id

    def __str__(self):
        """
        Returns a string representation of the course.
        :return: A string containing the course's ID, name, and professor.
        """
        return f"ID: {self.__course_id}, Name: {self.__name}, Professor: {self.__professor}"
