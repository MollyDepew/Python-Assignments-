#Molly Depew
#CS21
#ex 7 pg 335 (driver exam)
#Assignment 8
#Store answers in a list and compare to the students answers
#display whether they passed or failed, number correct, number incorrect
# and the numbers of the questions that were incorrect

def main():
    try:
        infile_key = open("correct.txt", 'r')
    except IOError:
        print("Solution file invalid")
    try:
        infile_response = open("student_solution.txt", 'r')
    except IOError:
        print("Student answer file invalid")
    key = []
    responses = []
#save answer key and student responses into lists
    try:
        for n in infile_key:
            correct = str(n)
            key.append(correct)
        for n in infile_response:
            answer = str(n)
            responses.append(answer)
    except ValueError:
        print("Invalid value")
    i = 0
    total = 0
    incorrect = []
#compare the two lists by index
#if they match add one to the score if they don't save the index in the incorrect list
    while i < len(key):
        if key[i] == responses[i]:
            total +=1
        else:
            incorrect.append(i)
        i += 1
    print(total,'correct')
    print(20-total,'incorrect')
    print('questions answers incorrectly: ',incorrect)
#if the total score is under 15 the student failed
    if total < 15:
        print("failed")
    else:
        print("passed!")
    
main()
            
        
            
