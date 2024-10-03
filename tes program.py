def detail():
    name = str(input('please enter your name:'))
    age = int(input())

    print (name)
    print(age)


#name_list = [name]

def meet():
    print ("what up World!")

def Equation():
    var = 50
    if var == 0:
        print('Zero')
    elif var <= 0:
        print('negative')
    else:
        print('Positive')

#detail()
#meet()
#Equation()
#detail()

def greet(name):
    print("Hello " + name + "!")


#greet('Alice')

def square(number):
    return number * number

#result = square(4)
#print(result)

def is_even(number):
    return number % 2 == 0

if is_even (5):
    print('even')
else :
    print('odds')

#is_even(3)
#square(2)

def greet_user(name, age):
    print(f'Hello, {name} you are {age} years old')

#greet_user('Kg', 23)

#Y_name = input("please enter your naame:")
#print(f'hello {Y_name}!')

#fav_number = input("please enter a number netween 1 and 100:")
#if fav_number.isdigit():
 #   print(f'your favorite number is {fav_number}.')
#else:
 #   print('this is not a valid number')


#birth_year = int(input('please enter your birth year: '))#input gets data from the user as a string/ int is used to get/convert intergers
#current_year = 2024
#print(f'you are {current_year - birth_year} years old')

#error handling

try:
    number = int(input('please enter a number: '))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print('you cant divide this number by zero')
except ValueError:
    print('please enter a valid number!')


try:
    file = open('readme.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('this file does not exist!')


class car:
    def __init__(self, model, brand, year) -> None:
        self.model = model
        self.brand = brand
        self.year = year

    def Your_car(self):
        print(f'you have the {self.brand} {self.model} of {self.year}')

Dream = car('Swift', 'Suzuki', 2017)

Dream.Your_car()