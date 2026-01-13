from domain.validation import ValidatorException
from repository.student_repo import RepositoryException

class Console:
    def __init__(self, student_service, course_service, grade_service):
        """
        Initializes the console UI.
        :param student_service: The student service.
        :param course_service: The course service.
        :param grade_service: The grade service.
        """
        self.__student_service = student_service
        self.__course_service = course_service
        self.__grade_service = grade_service

    def __print_menu(self):
        """
        Prints the main menu.
        """
        print("\n--- Student & Course Management ---")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Assign Grade")
        print("4. Search")
        print("5. Reports")
        print("0. Exit")

    def __print_student_menu(self):
        """
        Prints the student management menu.
        """
        print("\n--- Manage Students ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Show All Students")
        print("0. Back")

    def __print_course_menu(self):
        """
        Prints the course management menu.
        """
        print("\n--- Manage Courses ---")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Update Course")
        print("4. Show All Courses")
        print("0. Back")

    def __print_search_menu(self):
        """
        Prints the search menu.
        """
        print("\n--- Search ---")
        print("1. Search Students")
        print("2. Search Courses")
        print("0. Back")

    def __add_student(self):
        """
        Handles adding a student.
        """
        try:
            student_id = int(input("ID: "))
            name = input("Name: ")
            self.__student_service.add_student(student_id, name)
            print("Student added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ValidatorException as ve:
            print(f"Validation Error:\n{ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __delete_student(self):
        """
        Handles deleting a student.
        """
        try:
            student_id = int(input("ID: "))
            self.__student_service.delete_student(student_id)
            print("Student deleted successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __update_student(self):
        """
        Handles updating a student.
        """
        try:
            student_id = int(input("ID: "))
            name = input("New Name: ")
            self.__student_service.update_student(student_id, name)
            print("Student updated successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ValidatorException as ve:
            print(f"Validation Error:\n{ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __show_all_students(self):
        """
        Shows all students.
        """
        students = self.__student_service.get_all_students()
        if not students:
            print("No students found.")
        else:
            for s in students:
                print(s)

    def __add_course(self):
        """
        Handles adding a course.
        """
        try:
            course_id = int(input("ID: "))
            name = input("Name: ")
            professor = input("Professor: ")
            self.__course_service.add_course(course_id, name, professor)
            print("Course added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ValidatorException as ve:
            print(f"Validation Error:\n{ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __delete_course(self):
        """
        Handles deleting a course.
        """
        try:
            course_id = int(input("ID: "))
            self.__course_service.delete_course(course_id)
            print("Course deleted successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __update_course(self):
        """
        Handles updating a course.
        """
        try:
            course_id = int(input("ID: "))
            name = input("New Name: ")
            professor = input("New Professor: ")
            self.__course_service.update_course(course_id, name, professor)
            print("Course updated successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ValidatorException as ve:
            print(f"Validation Error:\n{ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __show_all_courses(self):
        """
        Shows all courses.
        """
        courses = self.__course_service.get_all_courses()
        if not courses:
            print("No courses found.")
        else:
            for c in courses:
                print(c)

    def __assign_grade(self):
        """
        Handles assigning a grade.
        """
        try:
            student_id = int(input("Student ID: "))
            course_id = int(input("Course ID: "))
            grade_value = float(input("Grade: "))
            date = input("Date (YYYY-MM-DD): ")
            self.__grade_service.assign_grade(student_id, course_id, grade_value, date)
            print("Grade assigned successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ValidatorException as ve:
            print(f"Validation Error:\n{ve}")
        except RepositoryException as re:
            print(f"Repository Error: {re}")

    def __search_students(self):
        """
        Handles searching for students.
        """
        name_part = input("Name to search: ")
        results = self.__student_service.search_students(name_part)
        if not results:
            print("No students found.")
        else:
            for s in results:
                print(s)

    def __search_courses(self):
        """
        Handles searching for courses.
        """
        name_part = input("Name to search: ")
        results = self.__course_service.search_courses(name_part)
        if not results:
            print("No courses found.")
        else:
            for c in results:
                print(c)

    def __print_reports_menu(self):
        """
        Prints the reports menu.
        """
        print("\n--- Reports ---")
        print("1. Students for a Course")
        print("2. Top 3 Popular Courses")
        print("3. Top 20% Students")
        print("0. Back")

    def __show_course_report(self):
        try:
            course_id = int(input("Course ID: "))
            report = self.__grade_service.get_students_for_course_report(course_id)
            
            print("Sort by: 1. Name, 2. Grade")
            sort_opt = input(">>> ")
            
            if sort_opt == "1":
                report.sort(key=lambda x: x.get_student_name())
            elif sort_opt == "2":
                report.sort(key=lambda x: x.get_grade_value(), reverse=True)
            
            if not report:
                print("No students found for this course.")
            else:
                for item in report:
                    print(item)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

    def __show_popular_courses_report(self):
        report = self.__grade_service.get_most_popular_courses_report()
        if not report:
            print("No data available.")
        else:
            for item in report:
                print(item)

    def __show_top_students_report(self):
        report = self.__grade_service.get_top_students_report()
        if not report:
            print("No data available.")
        else:
            for item in report:
                print(item)

    def run(self):
        """
        Runs the main application loop.
        """
        while True:
            self.__print_menu()
            cmd = input(">>> ")
            if cmd == "1":
                while True:
                    self.__print_student_menu()
                    sub_cmd = input(">>> ")
                    if sub_cmd == "1":
                        self.__add_student()
                    elif sub_cmd == "2":
                        self.__delete_student()
                    elif sub_cmd == "3":
                        self.__update_student()
                    elif sub_cmd == "4":
                        self.__show_all_students()
                    elif sub_cmd == "0":
                        break
                    else:
                        print("Invalid command.")
            elif cmd == "2":
                while True:
                    self.__print_course_menu()
                    sub_cmd = input(">>> ")
                    if sub_cmd == "1":
                        self.__add_course()
                    elif sub_cmd == "2":
                        self.__delete_course()
                    elif sub_cmd == "3":
                        self.__update_course()
                    elif sub_cmd == "4":
                        self.__show_all_courses()
                    elif sub_cmd == "0":
                        break
                    else:
                        print("Invalid command.")
            elif cmd == "3":
                self.__assign_grade()
            elif cmd == "4":
                while True:
                    self.__print_search_menu()
                    sub_cmd = input(">>> ")
                    if sub_cmd == "1":
                        self.__search_students()
                    elif sub_cmd == "2":
                        self.__search_courses()
                    elif sub_cmd == "0":
                        break
                    else:
                        print("Invalid command.")
            elif cmd == "5":
                while True:
                    self.__print_reports_menu()
                    sub_cmd = input(">>> ")
                    if sub_cmd == "1":
                        self.__show_course_report()
                    elif sub_cmd == "2":
                        self.__show_popular_courses_report()
                    elif sub_cmd == "3":
                        self.__show_top_students_report()
                    elif sub_cmd == "0":
                        break
                    else:
                        print("Invalid command.")
            elif cmd == "0":
                break
            else:
                print("Invalid command.")
