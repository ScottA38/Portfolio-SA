"""
Current changes to issue:

    -Take all self instances out of simplifyFraction by calling it after each fraction has been called in startUp X(cannot do)
"""
class Fraction(object):
    #list of possible actions to perform on an initially created list
    ops = ['addition', 'subtraction', 'multiplication', 'dividision', 'inversion', 'decimalisation']

    #create an init file
    def __init__(self, num, denom):
        #assign instance variables to ordinary identifiers for easy reference
        self.num = num
        self.denom = denom

        #collect a simplified version of the fraction entered by calling simplifyFraction()
        out_num, out_denom = self.simplifyFraction(num)

        #*debug* test that the simplifyFraction() function is returning a reasonable result
        print(f"The best simplification of {num}/{denom} is {out_num}/{out_denom}.")

    def commonDenom(self, operand):
        """
        find commmon denominator by multiplying denominators of fractions together and adjusting numerator values accordinglys

        Even 'self' attributes have to be assigned called via the 'self' instance: self.num | self.denom because the variables of just 'num' | 'denom' are
        only available in the __init__() scope where they are defined. They could be defined again (if desired) for each method for easy referencing
        """
        num_1 = operand.denom * self.num
        num_2 = self.denom * operand.num
        denom_1 = operand.denom * self.denom
        return (num_1, num_2, denom_1)

    def simplifyFraction(self, hcf):
        """
        Use a recursion process to find the highest common factor between a numerator and denominator
        in order to factorise.

        When calling this function the 'hcf' argument should be the same as the numerator argument, making sure that it does not recurse over values which are
        higher than the numerator (will never be hcf: do not accept top-heavy fractions). Also if the
        numerator entered for hcf is 1 the 1st base case 'hcf <= 1' is caught
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
            return Fraction(int(self.num/hcf), int(self.denom/hcf))

        #decrement 'i' variable
        hcf -= 1

        #call the same function as a subfunction
        return self.simplifyFraction(hcf)

    def oper(self, operation, operand):
        """
        take input of created initial fraction and argument for type of operation to perform (arithmetic)

        Currently I cannot think of another method to use to physically feed Pyhton the arithmetic function except for a big hairty if, elif.. statement
        """
        #not worth decalring empty object instance

        if operation == "addition":
            #inform user of the arithmetic operation to be performed by what operands
            print(f"Here is the {operation} of {self} & {operand}:")
            res = self + operand
            res.output()

        if operation == "subtraction":
            #inform user of the arithmetic operation to be performed by what operands
            print(f"Here is the {operation} of {self} & {operand}:")
            res = self - operand
            res.output()

        if operation == "multiplication":
            print(f"Here is the {operation} of {self} & {operand}:")
            res = self * operand
            res.output()

        if operation == "division":
            print(f"Here is the {operation} of {self} & {operand}:")
            res = self / operand
            res.output()

        if operation == "inversion":
            #inform user of action to be taken
            print(f"Here is the {operation} of {self}:")
            res = self.inversion()
            res.output()

        if operation == "decimalisation":
            #inform user of action being taken
            print(f"Here is the {operation} of {self}:")
            res = float(self)
            print(f"The decimalised value is: {res}")

    def output(self):
        """
        modular function to output fraction result of operation performed and then print simplified fraction
        """

        #show user unsimplified result of operation by calling base 'print' method of Fraction class
        print(f"The unsimplified result is {self}")

        #simplify result of fraction (output will be new fraction object), has to reference self to get num and denom attributes
        res = self.simplifyFraction(self.num)
        #print simplified result
        print(f"The simplified result is {res}")

    def __str__(self):
        """
        create output if class object is called to a 'print' function
        """
        return(f"{self.num} / {self.denom}")

    def __add__(self, operand):
        """
        class method for add operator (only works with other fractions)
        """
        #unpack the variables of commonDenom. commonDenom will not be redognised unless attached to an instance of class such as 'self' or 'Fraction'
        num, add_num, denom = self.commonDenom(operand)

        #perform addition operation on numerator
        num += add_num

        return Fraction(num, denom)

    def __sub__(self, operand):
        """
        base method for subtracting current fraction by a variable
        """
        #common denom & modify numerators acordingly
        num, sub_num, denom = self.commonDenom(operand)

        #perform operation - no instances of calling self.num required here (i think)
        num -= sub_num

        #divide numerator and denominator by hcf and give as int for new Fraction object
        return Fraction(num, denom)


    def __mul__(self, operand):
        """
        base method for multiplying current fracton by a variable
        """
        #multiply numerators and denominators together
        self.num *= operand.num
        self.denom *= operand.denom

        return Fraction(self.num, self.denom)

    def __div__(self, operand):
        """
        base method for dividing current fraction by a variable
        """
        #multiply each numerator with denominator of other fraction for division
        self.num *= operand.denom
        self.denom *= operand.num

        return Fraction(self.num, self.denom)

    def __float__(self):
        """
        base method for defining a floating point number from the current num and denom
        """
        return float(self.num / self.denom)

    def inversion(self):
        """
        method to inverse num and denom ints and return new fraction instance
        """
        #allowed because arguments only respect order or csvs, not identifiers
        return Fraction(self.denom, self.num)
