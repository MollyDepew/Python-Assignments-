#Molly Depew
#CS 21
# Chapter 4 ex 5 (rainfall)
#Asks user for rainfall  over each month for predetermined months

years = int(input("years: "))
months = years*12
total = 0
for years in range(1,years+1):
    print("Year ", years)
    for months in range(1,13):
        rainfall = float(input("Enter rainfall in inches for the month: "))
        total += rainfall
    print("Year total is ", total)
    average= total/12
    print("Average rain per month is ", average)
        
