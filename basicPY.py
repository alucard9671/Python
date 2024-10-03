import datetime

def main():

    current_year = datetime.datetime.now().year

    while True:
        try:
            name = input('enter your name: ')
            if name.isalpha():
                break
            else:
                print('Invalid Input! Please enter letters only!')
        except(ValueError):
            print('Invalid Input! Please enter letters only!')

    

    def AgeCheck(age, name):
        if age >= 18:
            print(f'welcome to the next step {name}!')
        else:
            print('your not ready for the next step')

        
    while True:
        try:
            age = int(input('enter your age: '))
            break
        except ValueError:
            print('Invalid Input! please enter a valid number!')


    while True:
        try:
            year = int(input('please enter your birth year: '))
            if 1800 <= year <= current_year:
                break
            else:
                print(f'invalid Input! please enter a valid year between 1800 and {current_year}!')
        except(ValueError):
            print('invalid Input! please enter a valid year!')

    AgeCheck(age, name)

    ghost = {'name': name,
             'age': age,
             'birth year': year}


    for key, value in ghost.items():
        print(f'{key}: {value}')

main()