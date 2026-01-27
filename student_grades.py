"""
Student Grade Tracker
Demonstrates Git workflows with data structures
"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Must be between 0 and 100.")
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"\nStudent: {self.name} (ID: {self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")

if __name__ == "__main__":
    student1 = Student("Alice Johnson", "GT1")
    student1.add_grade(85)
    student1.add_grade(92)
    student1.add_grade(88)
    
    print("=== BDBI Student Grade Tracker ===")
    student1.display_info()

