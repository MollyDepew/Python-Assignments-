#Molly Depew
#CS21
#Chapter 4 ex 4 (distance)
#User inputs hours and speed traveledd
#create a table of distance

# hours traveled
hours = int(input("Enter hours traveled: "))

#speed
speed = float(input("Enter speed in mph: "))
while speed < 0:
    print("Speed must be greater than 0")
    speed = float(input("Enter speed in mph: "))
    
if speed>0 :
    print('Hour   Distance')
    print('-----------------------')
    for hours in range(1,hours+1):
        distance = hours*speed
        print(hours,'\t', distance)
