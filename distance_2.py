#Molly Depew
#CS 21
#Chapter 4 ex 4 (functions)
#create a function show_travel
#accepts the time and speed and prints the chart of distance traveled by hour.
def main():

#get time
    time = int(input("Enter time traveled in hours: "))
    while time <= 0:
            print("time must be greater than 0")
            time = int(input("Enter time traveled in hours: "))
#get Speed
    speed = int(input("Enter speed of the car in mph: "))
    while speed <= 0:
            print("Speed must be greater than 0")
            speed = int(input("Enter speed of the car in mph: "))
#Calculate distance
    distance = time*speed

#invoke show_travel
    show_travel(time,speed,distance)
        
#define show_travel function                   
def show_travel(time, speed, distance):
    if speed>0 :
        print('Hour\tDistance')
        print('-----------------------')
    for time in range(1,time+1):
        distance = time*speed
        print(time,'\t', distance)


    
