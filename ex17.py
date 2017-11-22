class Fraction(object):
    #list of possible actions to perform on an initially created list
    ops = {'add': "+", 'subtract': "-", 'multiply': "*", 'divide': "/", 'invert':"", 'decimalise':""}

    #create an init file
    def __init__(self, num, denom):
        #assign instance variables to ordinary identifiers for easy reference
        self.num = num
        self.denom = denom

        #collect a simplified version of the fraction entered by calling simplifyFraction()
        out_num, out_denom = self.simplifyFraction(num)

        #*debug* test that the simplifyFraction() function is returning a reasonable result
        print(f"The best simplification of {num}/{denom} is {out_num}/{out_denom}.")

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

    def commonDenom(self, num, denom, var_num, var_denom):
        """
        find commmon denominator by multiplying denominators of fractions together and adjusting numerator values accordinglys
        """
        num_1 = var_denom * num
        num_2 = denom * var_num
        denom_1 = var_denom * denom
        return (num_1, num_2, denom_1)

    def simplifyFraction(self, hcf):
        """
        Use a recursion process to find the highest common factor between a numerator and denominator
        in order to factorise.

        When calling this function the 'hcf' argument should be the same as the numerator argument. This will mean that if the
        numerator is 1 the 1st base case 'hcf <= 1' is caught
        """
        #if the hcf number has reached 1 or below then the process has failed and returning false
        #provides evidence of that instead of returning a number (this is a base case)
        if hcf <= 1:
            #return standard numerator (no common factors)
            return self.num, self.denom

        print(f"case {hcf} (descending)")
        #specify a base case where both numbers are directly divisible by the hcf variable
        #second base case (?)
        if (self.num % hcf == 0) & (self.denom % hcf == 0):
            print("hcf found!")
            return (int(self.num/hcf), int(self.denom/hcf))

        #decrement 'i' variable
        hcf -= 1

        #call the same function as a subfunction
        return self.simplifyFraction(hcf)

    def __str__(self):
        """
        create output if class object is called to a 'print' function
        """
        return(f"{self.num} / {self.denom}")

    def __add__(self, var_num, var_denom):
        """
        class method for add operator (only works with other fractions)
        """
        #unpack the variables of commonDenom
        num, add_num, denom = commonDenom(num, denom, var_num, var_denom)

        #perform addition operation on numerator
        num += add_num

        return Fraction(num, denom)

    def __sub__(self, var_num, var_denom):
        """
        base method for subtracting current fraction by a variable
        """
        #common denom & modify numerators acordingly
        num, sub_num, denom = commonDenom(num, denom, var_num, var_denom)

        #perform operation
        num -= sub_num

        #divide numerator and denominator by hcf and give as int for new Fraction object
        return Fraction(num, denom)


    def __mul__(self, var_num, var_denom):
        """
        base method for multiplying current fracton by a variable
        """
        #multiply numerators and denominators together
        num *= var_num
        denom *= var_denom

        return Fraction(num, denom)

    def __div__(self, var_num, var_denom):
        """
        base method for dividing current fraction by a variable
        """
        #multiply numerator with denominator of other fraction
        num *= var_denom
        denom *= var_num

        return Fraction(num, denom)


    def __float__(self):
        """
        base method for defining a floating point number from the current num and denom
        """
        return float(num / denom)

    def inverse(self):
        """
        method to inverse num and denom ints and return new fraction instance
        """
        #allowed because arguments only respect order or csvs, not identifiers
        return Fraction(denom, num)


def create():
    #take int input from the user using predefined functions for numerator and denominator
    num = Fraction.newInput("numerator", False)
    denom = Fraction.newInput("denom", False)

    #return simplified num and denom class instance
    return Fraction(num, denom)

def startUp():

    print("Welcome - this is a program to create and manipulate fractions in Python.\nPlease follow the instructions below:")

    #intiate exit clause (boolean)
    exit_clause = False

    #to allow this segment of function to run on loop until the user specifies to stop
    while exit_clause == False:

        #create() to create first fraction object
        one = create()

        print("Your fraction is: ", one)

        print("What would you like to do with the fraction? Options are provided in the list below: ")

        #iterate over enumerated list of strings to display options
        for i, value in enumerate(Fraction.ops.keys()):
            print(f"[{i}]: {value} your fraction.")

        while True:
            print("Please select from the list by giving a corrseponding decimal number.")
            #take input via function
            entry = Fraction.newInput("choice", False)
            if entry not in range(0, len(Fraction.ops)):
                #error message to user
                print("Input out of range of options list, please try again.")
            break


        #inform user of action to be taken and input expected
        print("Do you want to continue? type '1' for yes and '0' for no below:")

        if Fraction.newInput("exit decision", True) == 0:
            break
        else:
            print("Continuing...")

startUp()
