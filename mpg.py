#Molly Depew
#CS21
#Assignment 11 ex 1
#pg 562 #3
#write a GUI program that allows the user to input miles and gallons
#when calculate mpg button pressed should display mpg

import tkinter  
class MPGGUI:
    def __init__(self):  
        # Create the main window.
        self.main_window = tkinter.Tk()  
        # Frames
        self.gas_held = tkinter.Frame(self.main_window)
        self.mile_tank = tkinter.Frame(self.main_window)
        self.mpg = tkinter.Frame(self.main_window)
        self.bottom = tkinter.Frame(self.main_window)
        # widget for gas held
        
        self.label_gas = tkinter.Label(self.gas_held, \
                                       text='Enter the number of gallons:')
        self.gas_entry = tkinter.Entry(self.gas_held, width=10)  
        # Pack the gas held 
        self.label_gas.pack(side='left')
        self.gas_entry.pack(side='left')
        
        # Create the widgets for miles traveled.
        
        self.label_miles = tkinter.Label(self.mile_tank, \
                                       text='Enter the number of miles:')
        self.miles_entry = tkinter.Entry(self.mile_tank, width=10) 
       #pack
        self.label_miles.pack(side='left')
        self.miles_entry.pack(side='left')

        #create label for answer
        self.label = tkinter.Label(self.mpg,\
                             text='mpg:')
        self.value = tkinter.StringVar()
        #string variable
        self.mpg_label = tkinter.Label(self.mpg,\
                                       textvariable=self.value)
        self.label.pack(side='left')
        self.mpg_label.pack(side='left')
    
        # Create the buttons
        self.calc_button = tkinter.Button(self.bottom, \
                                          text='Convert', \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom, \
                                          text='Quit', \
                                          command=self.main_window.destroy)  
            
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')  
        # Pack the frames.
        self.gas_held.pack()
        self.mile_tank.pack()
        self.mpg.pack()
        self.bottom.pack()  
        # Enter the tkinter main loop.
        tkinter.mainloop()  
    # The convert method is a callback function for
    # the Calculate button.
    def convert(self):
        # Get the value entered by the user into the
        # gas held widget
        gas = float(self.gas_entry.get())
        miles = float(self.miles_entry.get()) 
        # Convert to mpg
        mpg = miles/gas 
        # store it in our string variable
        self.value.set(mpg)  
# Create an instance of this class
mpg_found = MPGGUI() 
    
