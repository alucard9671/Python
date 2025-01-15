#Student and Teacher management system
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people = {}

    def display_info(self):
        print(f"\n name: {self.name}")
        print(f"age: {self.age}")

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = []
        self.students = {}

    def add_grade(self, grade):
        name = input("enter students' name: ")
        if name in self.students:
            try:
                grade = int(input("enter grade: "))
                if 0 <= grade <= 100:
                    self.students[name].grade.append(grade)
                    print(f"{grade} added for {name}")
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
                
                self.students[name] = Student (name, age, self.grade)
                print(f"{name} has been added to the database.")
                break
            except ValueError as e:
                print(e)

    def graduate_student(self, name):#graduated students file
        if name in self.students:
            student = self.students[name]

            with open("graduated.txt", "a") as file:
                grades_str = ",".join(map(str,student.grade)) or "no greades yet."
                file.write(f"name: {student.name} age: {student.age} grade: {grades_str}\n")
    #remove from current student
            del self.students[name]
            print(f"{name} has been moved to graduated students")
        else:
            print(f"{name} not found in current roster")

    def display_all_students(self):
        if not self.students:
            print("not in the database.")
        else:
            for student in self.students.values():
                student.display_info()

    def save_to_file(self):
        with open("students.txt","w") as file: #use a to append the file, with open doesn't require to function close the file
            for student in self.students.values():
                grades_str = ",".join(map(str, student.grade)) or "no grades yet."
                file.write(f"Name: {student.name}, Age: {student.age}, Grade: {grades_str}\n")
        print("All active students' data has been saved to students.txt.") 

    def display_S_instance_info(self):
        print(f"\n name: {self.name}")
        print(f"Age: {self.age}")
        print(f"grade: {self.grade}")
        
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
            except ValueError as o:
                print(o)

    def add_subject(self):
        name = input("enter teacher's name: ")
        if name in self.teachers:
            subject = input("Enter the subject to assign: ")
            self.teachers[name].subject = subject
            print(f"Subject: {subject} assigned to {name}.")
        else:
            print(f"No teacher found with the name {name}")
            
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
        print(f"{teacher.name}'s data has been saved to teachers.txt.")


    def display_T_instance_info(self):
        print(f"\n name: {self.name}")
        print(f"Age: {self.age}")
        print(f"subject: {self.subject}")



#main loop program
def main():
    student_manager = Student("Temp", 0, [])
    teacher_manager = Teacher("Temp", 0, "Temp")

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
            print('9. Exit')

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
            elif choice == '9':
                print('exiting... Goodbye!')
                break
            else:
                print('invalid choice. Please try again')

if __name__ == '__main__':
    main()
