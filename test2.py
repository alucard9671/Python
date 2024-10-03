#print('this is test 2 ')
#print( 100)

#for u in range (1, 11):
 # if u % 2 == 0:
  #  print(u)


#for v in range (1, 50):
  #if v % 10 == 0:
   # print(v)


#k = 20

#while k >= 0:
  #print(k)
 # k -= 10


#for step in range (5):
 # print('take a step')

#T_step = 0

#while T_step < 5:
  #print ('step off')
  #T_step += 1

#for pep in range(10):
 # if pep % 2 == 0:
  #  print('take a step')
#else:
#  print('step off')


shoe = 10

#while shoe >= 0:
 # print('take a step')
 # shoe -= 2


#if shoe == pep:
 # print ('its a step')
#else:
#  print('your drunk')

#for i in range (1,4):
 #   print(i)

#colours = ['red', 'green', 'blue']

#for color in colours:
 #   print(color)

#while colors == colors:
 #   print(color)
  #  color += 1


x = 3

#while x >= 0:
 #   print(x)
  #  x -= 1

#anima = ['dog', 'cat', 'fish']

#for anim in anima:
 #   print('I love my', anim)


#for bear in ['black', 'polar', 'grizzly']:
 #   print(bear)


#for char in 'world Domination':
 #   print(char)



L = 100

#while L >= 0:
 #   print("I Love you")
  #  L -= 1

#file handling

file = open('alucard.txt', 'w')
file.write('The air was thick, the moon was full and I was dying to sink my teeth into something. Get it because Im a vampire')
file.close

file = open('alucard.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('alucard.txt', 'a')
file.write('\nthe new line of succession')#\n starts a new line underneth
file.close()
#after every action the file must be closed and opened to perform another function
file = open('alucard.txt', 'r')
updated_content = file.read()
print(updated_content)
file.close()


