import grade
import datetime
import threading
import time


# Q1. Student class with constructor
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 0

        # Q7. Admission date
        self.admission_date = datetime.date.today()

    # Q3. Getter method
    def get_marks(self):
        return self.__marks

    # Q3. Setter method
    def set_marks(self, marks):

        # Q6. Exception handling
        if marks < 0 or marks > 100:
            raise ValueError("Invalid Marks")
        else:
            self.__marks = marks

    # Q4. Calculate grade
    def calculate_grade(self):
        return grade.calculate_grade(self.__marks)

    # Q2. Display student details
    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.get_marks())
        print("Grade:", self.calculate_grade())
        print("Admission Date:", self.admission_date)


# Q5. Department container class
class Department:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            student.display()
            print()


# Q9. Inheritance and method overriding
class MeritStudent(Student):

    def calculate_grade(self):
        if self.get_marks() >= 90:
            return "A+"
        else:
            return super().calculate_grade()


# Q10. Report generation using thread
def generate_report():
    print("Generating Report...")
    time.sleep(2)
    department.display_students()
    print("Report Generated Successfully")


# Q2. Creating student objects
s1 = Student(1, "Rahul")
s2 = MeritStudent(2, "Amit")


# Q6. Handling exceptions
try:
    s1.set_marks(80)
    s2.set_marks(95)

except ValueError as e:
    print(e)


# Creating department object
department = Department()

# Adding students to department
department.add_student(s1)
department.add_student(s2)


# Q10. Creating and starting thread
t1 = threading.Thread(target=generate_report)
t1.start()
t1.join()

print("Program Completed")