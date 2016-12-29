# Molly Depew
#CS21
#Assignment 8
#ex 5 pg 335
# program reads the contents of the file into a list.
#ask user for an input and search list to see if it is in there

def main():
    try:
        infile = open("charge_accounts.txt",'r')
    except IOError:
        print("error opening file")
    #load data into a list
    accountList = []
    try:
        for n in infile:
            num = int(n)
            accountList.append(num)
    except ValueError:
            print('Value error, not added to list')
    #search for value
    search = int(input("Enter a charger account number: "))
    if search in accountList:
        print("Valid Number")
    else:
        print(search,"was not found in the list")
main()
                          
