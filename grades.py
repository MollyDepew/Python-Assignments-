#Molly Depew
#CS21
#grades

def main():
    A = 90
    B = 80
    C = 70
    D = 60
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    try:
        infile = open("grades.txt", "r")
        outfile = open("grade_out.py", "w")

        for line in infile:
            grade = float(line)
            if grade >= A:
               outfile.write("A\n")
               a = a+1
      
            elif grade >= 80:
                outfile.write("B\n")
                b = b+1
            elif grade >= 70:
                outfile.write("C\n")
                c = c+1
            elif grade >= 60:
                outfile.write("D\n")
                d = d+1
            else:
                outfile.write("F\n")
                f = f+1
        outfile.write("A:")
        outfile.write("*"*a)
        outfile.write("\n")
        outfile.write("B:")
        outfile.write("*"*b)
        outfile.write("\n")
        outfile.write("C:")
        outfile.write("*"*c)
        outfile.write("\n")
        outfile.write("D:")
        outfile.write("*"*d)
        outfile.write("\n")
        outfile.write("F:")
        outfile.write("*"*f)
    except IOError:
        print("There was an error trying to read the file")
    except ValueError:
        print("There were invalid values in the file that were not floats")
        
main()
