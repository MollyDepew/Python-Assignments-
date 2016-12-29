#Molly Depew
#CS21
#Assignment 9 ex 1
#ask user for 10 digit phone number
#display the number with alphabetical characters translated to numbers

def main():
    num = str(input("Enter the telephone number in XXX-XXX-XXXX format: "))
    num = num.replace(num, num.upper())
    print('The phone number is ', letter_convert(num))

#using the replace function in strings we can write it so that letters are replaced by the respective number
def letter_convert(num):
    num = num.replace('A','2')
    num = num.replace('B','2')
    num = num.replace('C','2')
    num = num.replace('D','3')
    num = num.replace('E','3')
    num = num.replace('F','3')
    num = num.replace('G','4')
    num = num.replace('H','4')
    num = num.replace('I','4')
    num = num.replace('J','5')
    num = num.replace('K','5')
    num = num.replace('L','5')
    num = num.replace('M','6')
    num = num.replace('N','6')
    num = num.replace('O','6')
    num = num.replace('P','7')
    num = num.replace('Q','7')
    num = num.replace('R','7')
    num = num.replace('S','7')
    num = num.replace('T','8')
    num = num.replace('U','8')
    num = num.replace('V','8')
    num = num.replace('W','9')
    num = num.replace('X','9')
    num = num.replace('Y','9')
    num = num.replace('Z','9')
    return num
    
  
main()
