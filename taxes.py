#Molly Depew
#CS21
#Create a function show_property_tax to print out the calculated taxes
def main():

#define actual value
    value = int(input("Enter the actual value of the property in dollars: "))
    while value <= 0:
            print("The actual value must be greater than 0")
            value = int(input("Enter the actual value of the property in dollars: "))
           

#calculate assessment value
    assessment_value = value*.6

#calculate property tax
    property_tax = assessment_value*.72

#invoke show_property_tax
    show_property_tax(assessment_value, property_tax)

#define our function 

def show_property_tax(assessment_value, property_tax):
    print("The assessment value is $", format(assessment_value, '.2f'))
    print("The property tax is $" , format(property_tax, '.2f'))
    

    
