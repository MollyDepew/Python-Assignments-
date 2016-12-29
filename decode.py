#Molly Depew
#CS21
#Assignment 10 ex 1
#write a program so that each character is assigned to a code using dictionaries
#create the keys with the first column
#value for second

def main():
    #welcome message
    print('welcome to my encryption program\n')
    print('You can choose to either encrypt a file or decode an encrypted file')
    print('1- Encrypt\n','2- Decrypt')

    #setting up the dictionary for encoding or decode
    #open the codes file and save the strings in the key and matching values in value
    try:
        codes_file = open('codes.txt', 'r')
        codes = codes_file.readlines()
    except IOError:
        print('file not found')

    dic = {}

    #user choice to encrypt or decode with input validation
    choice = int(input('Your choice: '))
    while choice is not 1 and choice is not 2:
        print('please enter either 1 or 2')
        choice = int(input('Your choice: '))

    # if choice is 1 we encrypt by looking for the string in the keys of the dictionary and replacing with the corresponding value
    if choice == 1:
        infile = input('Enter the name of the input file: ')
        output = input('Enter the name of the output file: ')
        print('writing encrypted data to ', output)
        output = open(output, 'w')

    # saving lines of code file by the key 
        try:
            for line in codes:
                (key,val) = line.split()
                dic[str(key)] = val
        except ValueError:
            print("invalid value")

    # reading the file the user wants to encrypt and writing the output file 
        try:
            user_file = open(infile,'r')
            user_file = user_file.read()
            for n in user_file:
                if n in dic:
                    n = n.replace(n,dic[str(n)])
                    output.write(str(n))
                if n.isspace():
                    n = n
                    output.write(n)
        except IOError:
            print('invalid file')
        
    
    # choice 2 take the contents of the encrypt file and relay it back to the key 
    if choice == 2:
        infile = input('Enter the name of the input file: ')
        output = open('choice2.txt', 'w')
    #saving codes in dictionary by value so we can search that way 
        try:
            for line in codes:
                (key,val) = line.split()
                dic[str(val)] = key
        except ValueError:
            print("invalid value")
        try:
            user_file = open(infile,'r')
            user_file = user_file.read()
        except IOError:
            print('invalid file')
        print('The decrypted contents of the file are: ')
    # decrypting the file by replace the value with the corresponding key 
            
        for n in user_file:
            if n.isspace():
                n = n
                print(n, end = '')
            
            else:
                n = dic[str(n)]
                print(n, end = '')
                
    codes_file.close()
      
                
        
    
        
        
main()
