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

with open("alucard.txt","a") as file:# does not require a .close function to close the file.
    file.write("\n Dont you Know, bitches love cannons!")# using with open you need to have indentation for the next line
