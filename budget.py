#Molly Depew
#CS21
#Chapter 4 ex 3 (budget)
#user inputs monthly budget and amount spent
#total is summed until user inputs 0

budget = float(input("Enter amount budgeted for the month: "))
#amount spent is initialized

amount = float(input("Enter an amount spent: "))
spent = amount

#keep asking for inout until user inputs 0
while amount !=  0:
    amount = float(input("Enter an amount spent(0 to quit): "))
    spent += amount

# If the program is quit then total up spent amounts
if amount == 0:
    print("Budgeted: ", budget)
    print("spent: ", spent)
if spent < budget :
    under = budget-spent
    print("You are ", under, "under budget. WELL DONE!")
if spent > budget :
    over = spent-budget
    print("You are ", over, "over budget. PLAN BETTER NEXT TIME!")
    
