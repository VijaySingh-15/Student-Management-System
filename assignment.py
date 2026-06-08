class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
 
    def update(self, name=None, age=None, course=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if course:
            self.course = course
 
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}"
 
 
class StudentManager:
    def __init__(self):
        self.students = [] 
 
    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully.")
 
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
 
    def update_student(self, student_id, name=None, age=None, course=None):
        student = self.find_student(student_id)
        if student:
            student.update(name, age, course)
            print("Student updated successfully.")
        else:
            print("Student not found.")
 
    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")
 
    def search_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            print("Student found:")
            print(student)
        else:
            print("Student not found.")
 
    def display_all(self):
        if not self.students:
            print("No records available.")
        else:
            print("\nAll Student Records:")
            for student in self.students:
                print(student)

 
def main():
    manager = StudentManager()
 
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")
 
        choice = input("Enter choice: ")
 
        if choice == '1':
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            manager.add_student(Student(sid, name, age, course))
 
        elif choice == '2':
            sid = input("Enter ID to update: ")
            name = input("Enter new name : ")
            age = input("Enter new age : ")
            course = input("Enter new course : ")
 
            age = int(age) if age else None
            manager.update_student(sid, name or None, age, course or None)
 
        elif choice == '3':
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)
 
        elif choice == '4':
            sid = input("Enter ID to search: ")
            manager.search_student(sid)
 
        elif choice == '5':
            manager.display_all()
 
        elif choice == '6':
            print("Exiting...")
            break
 
        else:
            print("Invalid choice. Try again.")
 
 
if __name__ == "__main__":
    main()