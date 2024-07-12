# 151115_q2.py

# Import necessary libraries
import json

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                print(f"Average grade for {student.name}: {student.get_average()}")
                return
        print("Student not found.")

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades for subject: {subject}")
        else:
            print(f"Class average for {subject}: {total / count}")

# Function to load students from a JSON file
def load_students(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            classroom = Classroom()
            for student_data in data:
                student = Student(student_data['name'])
                student.grades = student_data['grades']
                classroom.add_student(student)
            return classroom
    except FileNotFoundError:
        return Classroom()

# Function to save students to a JSON file
def save_students(filename, classroom):
    with open(filename, 'w') as file:
        data = [{'name': student.name, 'grades': student.grades} for student in classroom.students]
        json.dump(data, file)

def main():
    filename = 'students.json'
    classroom = load_students(filename)
    
    while True:
        print("\nSchool Class Management System")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Get average grade of a student")
        print("4. Get class average for a subject")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            student = Student(name)
            while True:
                subject = input("Enter subject (or type 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                student.add_grade(subject, grade)
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            name = input("Enter student's name to get average: ")
            classroom.get_student_average(name)
        elif choice == '4':
            subject = input("Enter subject to get class average: ")
            classroom.get_class_average(subject)
        elif choice == '5':
            save_students(filename, classroom)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
