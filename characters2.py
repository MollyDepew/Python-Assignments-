#Molly Depew
#CS21
#Assignment 9 ex 3
#Create a program that takes in a string and finds the most frequently occuring
#letter of letters


#change the string that's inputed so that all te characters are uppercase
#this way we only have to check one character not two
def main():
    string = str(input('Enter a string: '))
    string = string.replace(string, string.upper())
    frequency = []
    ch_list = []
    answer = []
#using a character in the string look for any characters that match
#if they do add one to our running total
# if the character we just counted is not already in the list add it to the list
#as well as the total times it appears
    for ch in string:
        temp = ch
        count = 0
        for char in string:
            if temp == char:
                count += 1
        if ch not in ch_list:
            ch_list.append(ch)
            frequency.append(count)
#find the max number we saved in the list of counts and the index it is in the list
#check to see if there are other values in the list that are the same aka we have multiple maxs

    mx = max(frequency)
    max_index = frequency.index(mx)
    i = 0
    while i < len(frequency):
        if mx == frequency[i] and i != max_index:
            val = i
            answer.append(ch_list[val])
        i+= 1
#find the character in the ch_list that corresponds with the max count 
    answer.append(ch_list[max_index])
    print('The most frequently occurring letter(s): ', answer)

    
       

    

    
    
            

main()
    
