class Student:
    def __init__(self, student_id, name):
        """
        Initializes a student with an ID and a name.
        :param student_id: The unique identifier of the student.
        :param name: The name of the student.
        """
        self.__student_id = student_id
        self.__name = name

    def get_student_id(self):
        """
        Returns the student's ID.
        :return: The student's ID.
        """
        return self.__student_id

    def get_name(self):
        """
        Returns the student's name.
        :return: The student's name.
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the student's name.
        :param name: The new name of the student.
        """
        self.__name = name

    def __eq__(self, other):
        """
        Checks if two students are equal based on their ID.
        :param other: The other student to compare with.
        :return: True if the students have the same ID, False otherwise.
        """
        return self.__student_id == other.__student_id

    def __str__(self):
        """
        Returns a string representation of the student.
        :return: A string containing the student's ID and name.
        """
        return f"ID: {self.__student_id}, Name: {self.__name}"
