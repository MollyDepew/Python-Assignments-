#Molly Depew
#CS21
#Chapter 5 ex 19
#calculate the amount you will have in your account after a specific time
# with compound interest

def main():
    account_present = float(input("Enter the current value in the account: $"))
    interest = float(input("Enter the interest rate as a percent: %"))
    while interest < 0.0 or interest > 100.0:
        print("Invalid value")
        interest = float(input("Enter the interest rate as a percent: %"))
    months = int(input("Enter the number of months: "))
    while months < 0:
        print("Invalid values")
        months = int(input("Enter the number of months: "))
    account_future = future_values(account_present, interest, months)
    print("The value in the account after", months, "months is ", format(account_future,'.2f'))

def future_values(account_present, interest, months):
    interest_decimal = interest/100
    value = account_present*(1+interest_decimal)**months
    return value
    

main()
