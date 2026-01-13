class Grade:
    def __init__(self, student_id, course_id, grade_value, date):
        """
        Initializes a grade with a student ID, course ID, grade value, and date.
        :param student_id: The ID of the student.
        :param course_id: The ID of the course.
        :param grade_value: The value of the grade.
        :param date: The date the grade was assigned.
        """
        self.__student_id = student_id
        self.__course_id = course_id
        self.__grade_value = grade_value
        self.__date = date

    def get_student_id(self):
        """
        Returns the student's ID.
        :return: The student's ID.
        """
        return self.__student_id

    def get_course_id(self):
        """
        Returns the course's ID.
        :return: The course's ID.
        """
        return self.__course_id

    def get_grade_value(self):
        """
        Returns the grade value.
        :return: The grade value.
        """
        return self.__grade_value

    def get_date(self):
        """
        Returns the date the grade was assigned.
        :return: The date.
        """
        return self.__date

    def set_grade_value(self, grade_value):
        """
        Sets the grade value.
        :param grade_value: The new grade value.
        """
        self.__grade_value = grade_value

    def set_date(self, date):
        """
        Sets the date the grade was assigned.
        :param date: The new date.
        """
        self.__date = date

    def __eq__(self, other):
        """
        Checks if two grades are equal based on student ID and course ID.
        :param other: The other grade to compare with.
        :return: True if the grades have the same student ID and course ID, False otherwise.
        """
        return self.__student_id == other.__student_id and self.__course_id == other.__course_id

    def __str__(self):
        """
        Returns a string representation of the grade.
        :return: A string containing the student ID, course ID, grade value, and date.
        """
        return f"Student ID: {self.__student_id}, Course ID: {self.__course_id}, Grade: {self.__grade_value}, Date: {self.__date}"
