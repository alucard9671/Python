#student management system

class Students: #stores student info (name, age, grade)
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade): #inputs grade
        if 0 <= grade <= 100: 
            self.grades.append(grade)
            print(f'Grade {grade} added for {self.name}.')
        else:
            print('invalid grade please enter a valid number between 0 and 100')

    def calculate_average(self):#calculates the average grade for the students
        if self.grades:
            return sum (self.grades) / len (self.grades)
        else:
            print(f'no grades available for {self.name}.')
            return 0
    
    def display_info(self): #displays the list of students name, age, grade and average
        print(f'\nName: {self.name}')
        print(f'Age: {self.age}')
        print(f'grades: {self.grades}')
        print(f'Average: {self.calculate_average():.2f}')


class School:
    def __init__(self) -> None:
        self.students = {}

    def add_student(self): #adds the students to the database
        while True:
            try:
                name = input ('enter students name: ')
                if not name.isalpha():
                    raise ValueError('name should only contain letters')

                age = int(input('Enter students age: '))
                if age <= 0:
                    raise ValueError ('age must be greater than 0')

                self.students[name] = Students (name, age)
                print(f'student {name} added successfully!\n')
                break
            except ValueError as e:
                print(e)

    def add_grade_to_student(self): #adds grades to the database
        name = input('enter the students name: ')
        if name in self.students:
            while True:
                try:
                    grade = int(input (f'enter grade for {name}: '))
                    self.students[name].add_grade(grade)
                    break
                except ValueError:
                    print('invalid input. Please enter a number.')

        else:
            print('student not found.')
            return

    def display_all_students(self):
        if not self.students:
            print('not in the system yet')
        else:
            for student in self.students.values():
                student.display_info()

#main program loop    
def main(): #function to update or view student information
    school = School()

    while True:
        print('\n--- Student management system ---')
        print('1. add student')
        print('2. add grade')
        print('3. display all students')
        print('4. Exit')

        choice = input('enter your choice: ')

        if choice == '1':
            school.add_student()
        elif choice == '2':
            school.add_grade_to_student()
        elif choice == '3': 
            school.display_all_students()
        elif choice == '4':
            print('exiting... Goodbye!')
            break
        else:
            print('invalid choice. Please try again')

if __name__ == '__main__':
    main()