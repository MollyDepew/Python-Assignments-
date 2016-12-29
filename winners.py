#Molly Depew
#CS21
#ex 10 pg 336
#assignment 8
#let user enter team name and display the number times that team won the
#world series
def main():
    #open file and store into list "winners"
    try:
        infile = open('WorldSeriesWinners.txt','r')
    except IOError:
        print("File invalid")
    winners = []
    try:
        for n in infile:
            team = str(n)
            winners.append(n)
    except ValueError:
        print("Team invalid")
     #User input to search for a specific name
    team_search = str(input("Enter a team name: "))
    i = 0
    count = 0
    #iterate through list if the name is in the list add one else go on to the next entry
    while i < len(winners):
        if team_search in winners[i]:
            count += 1
        i +=1
    print(count)
main()
    
