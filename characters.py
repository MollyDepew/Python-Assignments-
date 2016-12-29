#Molly Depew
#CS21
#Assignment 9 ex 2
#create a program that find the number of
# lowercase letters, uppercase, spaces, and digits in the file

def main():
    infile = str(input('Enter the file name: '))
    try:
        doc = open(infile,'r')
        file = doc.readlines()
    except IOError:
        print('invalid file')
    upper = 0
    lower = 0
    space = 0
    digit = 0
#if the character returns true for the string fuctions the count will increment
    for ch in file:
        if ch.isupper():
            upper +=1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            space += 1
    print('Uppercase letters: ', upper)
    print('Lowercase letters: ', lower)
    print('Digits: ', digit)
    print('Spaces: ', space)
main()
