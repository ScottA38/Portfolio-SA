"""
This script takes a the defined 'Fraction' class in 'Fraction_cl.py' and creates objects/ calls methods such that it performs arithmetic or other miscellaneous operations on Fractions using user inputs
"""

from Fraction_cl import Fraction

def newInput(subject, binary):
    """
    modular function to take int input from the user & validate it before returning the value
    """
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
             ValueError('The data received was not of the correct type, please try again.')
    return var

def create():
    """
    Creates a new instance of fraction for given parameters
    """
    #take int input from the user using predefined functions for numerator and denominator
    num = newInput("numerator", False)
    denom = newInput("denom", False)

    #return simplified num and denom class instance
    return Fraction(num, denom)

def startUp():
    """
    Class which encompasses entire program cycle
    """
    print("Welcome - this is a program to create and manipulate fractions in Python.\nPlease follow the instructions below:")

    #intiate exit clause (boolean)
    exit_clause = False

    #to allow this segment of function to run on loop until the user specifies to stop
    while exit_clause == False:

        #create() to create first fraction object, save to operand_1
        operand_1 = create()

        print("Your fraction is: ", operand_1)

        print("What would you like to do with the fraction? Options are provided in the list below: ")

        #iterate over enumerated list of strings to display options
        for i, value in enumerate(Fraction.ops):
            print(f"[{i}]: {value} your fraction.")

        while True:
            print("Please select from the list by giving a corrseponding integer number.\n")
            #take int input for operation required
            entry = newInput("choice", False)
            if entry not in range(0, len(Fraction.ops)):
                #error message to user
                print("Input out of range of options list, please try again.")
            #and index into list using this value to assign a string such as 'add' to 'entry'
            operation = Fraction.ops[entry]
            break

        if entry <= 3:
            print("Please follow the instructions to give a 2nd fraction with which to perform the operation.\n")
            #gather int inputs for numerator and denominator of arithmetic operation using newInput()
            oper_num = newInput("operand numerator", False)
            oper_denom = newInput("operand denominator", False)
            #create a new fraction object with identifier 'operand'
            operand_2 = Fraction(oper_num, oper_denom)
            #call function oper() to perform arithmetic operation
            operand_1.oper(operation, operand_2)

        if entry > 3:
            #call oper function to execute operation, but set 2nd argument to None because it is not required and should not be called in the logic flow for 'ntry > 3'
            operand_1.oper(operation, None)

        #inform user of action to be taken and input expected
        print("Do you want to continue? type '1' for yes and '0' for no below:")

        if newInput("exit decision", True) == 0:
            break
        else:
            print("Continuing...")


startUp()
