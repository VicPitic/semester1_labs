# Student & Course Management System - Documentation

## Problem Statement
The faculty needs an application to store and manage information about Students and Courses. The application should allow managing lists of students and courses (Add, Update, Delete, Find, Show All), assigning grades to students for specific courses, and generating reports.

## Iteration Plan

### Iteration 1: Core Domain & Basic Management (Week 8)
**Goal:** Implement the foundational architecture and CRUD operations for Students and Courses using in-memory storage.

**Features:**
1.  **Student Management**: Add, Remove, Update, Find, List all students.
2.  **Course Management**: Add, Remove, Update, Find, List all courses.
3.  **Validations**: Ensure data integrity (e.g., non-empty names, valid IDs).

**Technical Tasks:**
*   Define `Student` and `Course` entities.
*   Implement `StudentValidator` and `CourseValidator`.
*   Implement `StudentRepo` and `CourseRepo` (In-Memory).
*   Implement `StudentService` and `CourseService`.
*   Create Console UI with menus for Student and Course management.
*   Setup `main.py` and Test infrastructure.

### Iteration 2: Grade Assignment, Search & Persistence (Week 9)
**Goal:** Introduce the relational entity (Grade), add search functionality, and implement file-based persistence.

**Features:**
1.  **Persistence**: Save and load data (Students, Courses, Grades) from text files.
2.  **Grade Assignment**: Assign a grade to a student for a specific course.
3.  **Search**: Search for students and courses (e.g., by name).

**Technical Tasks:**
*   Define `Grade` entity (Student ID, Course ID, Grade Value, Date).
*   Implement `GradeValidator`.
*   Implement `StudentFileRepo`, `CourseFileRepo`, and `GradeFileRepo` inheriting from base repos.
*   Implement `GradeService` with business logic (check if Student/Course exists).
*   Add `search` methods to Services.
*   Update UI to support Grade assignment and Search.

---

## Specifications (Iteration 1 & 2)

### Domain
*   **Student**: `student_id` (int), `name` (string).
*   **Course**: `course_id` (int), `name` (string), `professor` (string).
*   **Grade**: `student_id` (int), `course_id` (int), `grade_value` (float), `date` (string/date).

### Services
*   **StudentService**:
    *   `add_student(id, name)`
    *   `delete_student(id)`
    *   `update_student(id, name)`
    *   `find_student(id)`
    *   `get_all_students()`
    *   `search_students(name_part)`
*   **CourseService**:
    *   `add_course(id, name, professor)`
    *   `delete_course(id)`
    *   `update_course(id, name, professor)`
    *   `find_course(id)`
    *   `get_all_courses()`
    *   `search_courses(name_part)`
*   **GradeService**:
    *   `assign_grade(student_id, course_id, grade_value, date)`: Throws exception if Student or Course does not exist.

### Repositories
*   **Base Repositories**: `store`, `delete`, `update`, `find`, `get_all`.
*   **File Repositories**: Load data on initialization, save data on modification.

### Iteration 3: Reports & Advanced Features (Week 10)
**Goal:** Implement complex reporting functionality and advanced sorting.

**Features:**
1.  **Course Report**: List all students and their grades for a specific course.
    *   Order alphabetically by student name.
    *   Order by grade value.
2.  **Popular Courses Report**: Display the top 3 courses with the most students enrolled (most grades assigned).
3.  **Top Students Report**: Display the top 20% of students based on their average grade across all courses.

**Technical Tasks:**
*   **Report Models**: Create `StudentGrade`, `StudentAverage`, and `CourseStudentCount` classes in `domain/report_models.py` to structure report data.
*   **Service Logic**: Implement report generation in `GradeService`.
    *   Calculate averages.
    *   Sort data using lambdas.
    *   Filter top results.
*   **UI Updates**: Add a "Reports" submenu in the Console.
*   **Testing**: Comprehensive tests for report logic (sorting, calculations, edge cases like empty lists).
