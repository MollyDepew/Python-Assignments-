#Molly Depew
#CS21
#Assignment 7 ex 1
# Write a program that asks the user for the name of the file.
#The program should write the contents of this input file to an output file.
#In the output file, each line should be preceded with a line number

def main():
    sampleprogram = input("Enter the name of the file: ")
    try:
        infile = open("sampleprogram.py", "r")
        outfile = open("ln_sampleprogram.py", "w")
        count = 0
        print(infile)

        for line in infile:
         line = line.rstrip()
         count = count + 1
         outfile.write(str(count) + ":" + line + "\n")

        infile.close()
        outfile.close()
    except IOError:
         print("invalid file")
     
main()
        
