class Person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f'Hello Im {self.name} and Im {self.age} years old')


new_Person = Person('Angi', 28, 'Female')

new_Person.display()


class Anime:
    def __init__(self, title, genres, rating ) -> None:
        self.title = title
        self.genres = genres
        self.rating = rating

    def What_Your_Watching(self):
        print(f'your watching {self.title} rated {self.rating} stars')

Watching = Anime('demon slayer', 'adventure', 5)

Watching.What_Your_Watching()


