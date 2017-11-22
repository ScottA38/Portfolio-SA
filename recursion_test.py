"""
An over-engineered peice of code to try and use recursion in order to determine an hcf
"""

def newInput(subject, binary):
    var = None
    while True:
        try:
            var = int(input("Please enter a desired integer value here for your {} ->".format(subject)))
            if binary == True:
                if (var > 1) | (var < 0):
                    print("The integer input was out of the range of binary digits (please enter either 1 or 0).")
                    var = None
            break
        except:
             ValueError('The data received was not consistently of the correct type, please try again.')
    return var

def commonFactor(hcf, num, denom):
    #if the hcf number has reached 1 or below then the process has failed and returning false
    #provides evidence of that instead of returning a number (this is a base case)
    if hcf <= 1:
        return False

    print(f"case {hcf} (descending)")
    #specify a base case where both numbers are directly divisible by the hcf variable
    #is this a second base case?
    if (denom % hcf == 0) & (num % hcf == 0) & (hcf >= num):
            print("hcf found!")
            return hcf

    #decrement 'i' variable
    hcf -= 1

    #call the same function as a subfunction
    return commonFactor(hcf, num, denom)

def startUp():

    print("This is a program to find the highest common factor of a given numerator and denominator.\nPlease follow the instructions below:")

    #intiate exit clause (boolean)
    exit_clause = False

    #to allow this segment of function to run on loop until the user specifies to stop
    while exit_clause == False:

        #take int input from the user using predefined functions for numerator and denominator
        num = newInput("numerator", False)
        denom = newInput("denom", False)

        #find the lower of the 2 values as a starting point for decrementing hcf search
        hcf = min(num, denom)

        #use predefined function to calculate the highest common factor (if any)
        out = commonFactor(, num, denom)

        if not out:
            print(f"There is no common factor for the numerator {num} and denominator {denom} (besides 1).")

        else:
            print(f"The highest common factor of {num} and {denom} is {out}.")
        #inform user of action to be taken and input expected
        print("Do you want to continue? type '1' for yes and '0' for no below:")

        if newInput("exit decision", True) == 0:
            break
        else:
            print("Continuing...")

startUp()
