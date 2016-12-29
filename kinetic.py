#Molly Depew
#CS21
#Chapter 5 ex 14 (exception handling)

def main():
    try:
        mass = int(input("Enter mass in kilograms: "))
        velocity = int(input("Enter velocity in meters per second:"))
        KE = kinetic_energy(mass,velocity)
        print("Kinetic energy is ", KE)
    except ValueError:
        print("Error: mass and velocity must be valid numbers")
def kinetic_energy(mass,velocity):
    return mass/2*velocity**2
main()
    
