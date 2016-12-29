#Molly Depew
#CS21
#21 game
#create a program that asked the user if they'd like to roll
#'y' to roll again 'n' to stop
#selct random integers from 1 to 6 and add them together then to the running total


def main():
    max_points = 21
    user_total = 0
    comp_total = 0
    while user_total <= max_points and get_response() == 'y':
        user_roll, comp_roll = rollDice()
        user_total += user_roll
        comp_total += comp_roll
        print("points: ", user_total)
    print("User's points: ", user_total)
    print("Computer's points: ", comp_total)
    if user_total > comp_total and user_total <= max_points and comp_total <= max_points:
        print("User Wins!")
    elif comp_total == user_total or comp_total > max_points and user_total > max_points:
        print("Tie game!")
    else:
        print("Computer Wins!")
        
        
        
def rollDice():
    import random
    userDice1 = random.randint(1,6)
    userDice2 = random.randint(1,6)
    user_roll = userDice1+userDice2
    compDice1 = random.randint(1,6)
    compDice2 = random.randint(1,6)
    comp_roll = compDice1+compDice2
    return user_roll, comp_roll

def get_response():
    response = str(input("do you want to roll?"))
    return response

main()




    
