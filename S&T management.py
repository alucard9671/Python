#Student and Teacher management system
import logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)#debug and monitoring
class Person:#parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):#child class inbeded in parent class

    def __init__(self, name, age):
        super().__init__(name, age)#brings info from parent class without duplicating code
        self.grades = []
        self.students = {}

    def add_grade(self):
        name = input("enter students' name: ")
        if name in self.students:
            try:
                grades = int(input("enter grade: "))
                if 0 <= grades <= 100:
                    self.students[name].grades.append(grades)
                    print(f"{grades} added for {name}")
                else:
                    print("Grade must be between 0 & 100.")
            except ValueError:
                print("Invalid input. please enter a number")
        else:
            print(f"no student found with the name {name}.")

    def add_students(self):
        while True:
            try:
                name = input("Enter students name: ")
                if not name.isalpha():
                    raise ValueError ("name must only contain letters.")
                if name in self.students:
                    raise ValueError ("student already exists")
                
                age = int(input("Enter students age: "))
                if age <=0 :
                    raise ValueError ("Age must be greater than 0.")
                
                self.students[name] = Student (name, age)
                print(f"{name} has been added to the database.")
                break
            except ValueError as e:
                logging.error(f"failed to add student:{e}")
                print(e)

    def graduate_student(self, name):#graduated students file
        if name in self.students:
            student = self.students[name]

            with open("graduated.txt", "a") as file:
                grades_str = ",".join(map(str,student.grades)) or "no greades yet."
                file.write(f"name: {student.name} age: {student.age} grade: {grades_str}\n")
    #remove from current student list
            del self.students[name]
            print(f"{name} has been moved to graduated students")
        else:
            print(f"{name} not found in current roster")


    def search_student(self, name):# search feature to find a specific student
        if name in self.students:
            student = self.students[name]
            print("\n--- student found ---")
            student.display_info()
        else:
            print(f"student {name} not in the database")

    def display_all_students(self):
        if not self.students:
            print("Student not in the database.")
        else:
            for student in self.students.values():
                student.display_info()

    def save_to_file(self):
        with open("students.txt","w") as file: #use a to append the file, with open doesn't require to function close the file
            for student in self.students.values():
                grades_str = ",".join(map(str, student.grades)) or "no grades yet."
                file.write(f"Name: {student.name}, Age: {student.age}, Grade: {grades_str}\n")
        print("All active students' data has been saved to students.txt.") 

    def load_from_file(self):
        try: 
            with open("students.txt","r") as file:
                for line in file:
                    #parse each line and extract student data
                    parts = line.strip().split(",")
                    name = parts[0].split(": ")[1]
                    age = int(parts[1].split(": ")[1])
                    grades = list(map(int, parts[2].split(": ")[1].split(", "))) if "no grades yet" not in parts[2] else[]
                    #recreate the student and add to dictionary 
                    self.students[name] = Student(name, age)
                    self.students[name].grades =grades
            print("student loaded from file.")
        except FileNotFoundError:
            print("no student data file found. Starting fresh")
        except Exception as e:
            print(f"Error loading students: {e}")

    def display_S_instance_info(self):
        print(f"\n name: {self.name}")
        print(f"Age: {self.age}")
        print(f"grade: {self.grades}")
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.teachers = {}

    def add_teacher(self):
        while True:
            try:
                name = input("Enter teacher's name: ")
                if not name.isalpha():
                    raise ValueError("name must only contain letters")

                if name in self.teachers:
                    raise ValueError ("Teacher already exists")
                    
                age = int(input("Enter teachers age: "))
                if age <=0 :
                    raise ValueError("age must be greater than 0")
                
                
                subject = input("Enter the subject of the teacher: ")
                if not subject.isalpha():
                    raise ValueError("Sbject must only contain letters.")
                
                
                self.teachers [name] = Teacher (name, age, subject)
                print(f"{name} has been added to the database.")
                break
            except ValueError as e:
                logging.error(f"failed to add teacher:{e}")
                print(e)

    def add_subject(self):
        name = input("enter teacher's name: ")
        if name in self.teachers:
            subject = input("Enter the subject to assign: ")
            self.teachers[name].subject = subject
            print(f"Subject: {subject} assigned to {name}.")
        else:
            print(f"No teacher found with the name {name}")

    def search_teacher(self, name):# search feature to find a specific Teacher
        if name in self.teachers:
            teacher = self.teachers[name]
            print("\n--- teacher found ---")
            teacher.display_info()
        else:
            print(f"teacher {name} not in the database")
            
    def display_all_teachers(self):
        if not self.teachers:
            print("no teachers in the database.")
        else:
            for teacher in self.teachers.values():
                teacher.display_info()

    def save_to_file(self):
        with open("teachers.txt", "w") as file:
            for teacher in self.teachers.values():
                file.write(f"Name: {teacher.name}, Age: {teacher.age}, Subject: {teacher.subject}\n")
        print("All teacher's data has been saved to teachers.txt.")

    def load_from_file(self):
        try: 
            with open("teachers.txt","r") as file:
                for line in file:
                    #parse each line and extract student data
                    parts = line.strip().split(",")
                    name = parts[0].split(": ")[1]
                    age = int(parts[1].split(": ")[1])
                    subject = parts[2].split(": ")[1]
                    #recreate teacher and add to dictionary 
                    self.teachers[name] = Teacher(name, age, subject)
            print("teachers loaded from file.")
        except FileNotFoundError:
            print("no teacher data file found. Starting fresh")
        except Exception as e:
            print(f"Error loading teacher: {e}")

    def display_T_instance_info(self):
        print(f"\n name: {self.name}")
        print(f"Age: {self.age}")
        print(f"subject: {self.subject}")



#main loop program
def main():
    student_manager = Student("Temp", 0)
    teacher_manager = Teacher("Temp", 0, "Temp")

    #load data from file
    student_manager.load_from_file()
    teacher_manager.load_from_file()

    while True:
            print('\n--- main menu ---')
            print('1. add student')
            print('2. add grade')
            print("3. add Teacher")
            print("4. add subject")
            print('5. display all students')
            print("6. display all Teachers")
            print("7. Graduate student")
            print("8. Save data to files")
            print("9. search student")
            print("10. search teacher")
            print('11. Exit')

            choice = input('enter your choice: ')

            if choice == '1':
                student_manager.add_students()
            elif choice == '2':
                student_manager.add_grade(None)#pass none if needed, since its unused
            elif choice == '3': 
                teacher_manager.add_teacher()
            elif choice == '4':
                teacher_manager.add_subject()
            elif choice == '5':
                student_manager.display_all_students()
            elif choice == '6':
                teacher_manager.display_all_teachers()
            elif choice == '7':
                name = input("enter the name of the student to graduate: ")
                student_manager.graduate_student(name)
            elif choice == '8':
                student_manager.save_to_file()
                teacher_manager.save_to_file()
            elif choice == "9":
                name = input("Enter students name to search: ")
                student_manager.search_student(name)
            elif choice == "10":
                name = input("Enter teachers name to search: ")
                teacher_manager.search_teacher(name)
            elif choice == '11':
                print('exiting... Goodbye!')
                break
            else:
                print('invalid choice. Please try again')

if __name__ == '__main__':
    main()
