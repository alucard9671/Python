#var = 50

#if var == 0:
    #print('Zero')
#elif var <= 0:
  #  print('negative')
#else:
   # print('Positive')



#for i in range(2, 11, 2):
 # print (i)


x = 10

#while x > 0:
 #print(x)
  #x -= 1


#y = 10
#y += 2
#y -= 3
#y *= 5
#y /= 7
#y %= 4 
#print(y)

#person = int(input())

#if person < 13:
   # print('child')
#elif person <= 18:
  #print('teenager')
#else:
   #print('adult')


#movie = ['spider-man', 'the amazing spider-man', 'deadpool']#list where data is stored

#print (movie[0])
#print(movie[-1])

#ovie.append('Kong & Godzilla')#thid adds an item to the list
#movie.remove('spider-man')#removes an item from a list
#movie[1]= 'hulk'#replaces an item in the list

#print(movie)


#person = {
   # "name": "Alice",
  #  "age": 30,
  #  "city": "New York"
#}

#perp = {'name': 'Mr sins', 'age': 34, 'residence': 'New York' }

#print(perp['name'])
#when  working with lists and dictionaries [lists use sq to create] while {dictinary uses curly to create}in print they bot use sq[]
#perp['job'] = 'welder'


books = {
    "title":"1984",
    "auther": "joe camble",
    "year": 2024
}

print(books['auther'])
print (books['title'])

books ['genre'] = "horror"

print(books)

animals = ['dog', 'cat', 'horse', 'fish', 'tiger','elephant', 'sparrow']

for anim in animals:#for loops with lists goes through each item
    print (anim)


ja_man = {
    'name': 'fin',
    'age': '24',
    'job': 'plumber'
}

for key, value in ja_man.items():#for loops with dictionaries use .items(), for both use .keys() .values() for either one
    print(f'{key}: {value}')

numbers = [1,2,3,4,5,6,7,8,9,10]
for numb in numbers:
    if numb % 2 == 0:
        print (numb)


