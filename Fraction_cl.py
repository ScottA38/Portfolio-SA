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
        """
        num_1 = operand.denom * num
        num_2 = denom * operand.num
        denom_1 = operand.denom * denom
        return (num_1, num_2, denom_1)

    def simplifyFraction(self, hcf):
        """
        Use a recursion process to find the highest common factor between a numerator and denominator
        in order to factorise.

        When calling this function the 'hcf' argument should be the same as the numerator argument. This will mean that if the
        numerator is 1 the 1st base case 'hcf <= 1' is caught

        Issue: Python doesn't recognise these object attributes of self like 'num' and 'denom' unless they have self. before them, but has done previously?
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
            res = inversion(self)
            res.output()

        if operation == "decimalisation":
            #inform user of action being taken
            print(f"Here is the {operation} of {self}:")
            res = float(self)
            res.output()

    def output(self):
        """
        modular function to output fraction result of operation performed and then print simplified fraction
        """
        #initilaise simplified fraction variables to be printed
        res_num = 0
        res_denom = 0

        #show user unsimplified result of operation
        print(f"The unsimplified result is {res}")

        #simplify result of fraction (output will be new fraction object)
        res = res.simplifyFraction(res.num)
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
        #unpack the variables of commonDenom
        num, add_num, denom = commonDenom(operand.num, operand.denom)

        #perform addition operation on numerator
        num += add_num

        return Fraction(num, denom)

    def __sub__(self, operand):
        """
        base method for subtracting current fraction by a variable
        """
        #common denom & modify numerators acordingly
        num, sub_num, denom = commonDenom(operand.num, operand.denom)

        #perform operation
        num -= sub_num

        #divide numerator and denominator by hcf and give as int for new Fraction object
        return Fraction(num, denom)


    def __mul__(self, operand):
        """
        base method for multiplying current fracton by a variable
        """
        #multiply numerators and denominators together
        num *= operand.num
        denom *= operand.denom

        return Fraction(num, denom)

    def __div__(self, operand):
        """
        base method for dividing current fraction by a variable
        """
        #multiply each numerator with denominator of other fraction for division
        num *= operand.denom
        denom *= operand.num

        return Fraction(num, denom)

    def __float__(self):
        """
        base method for defining a floating point number from the current num and denom
        """
        return float(num / denom)

    def inversion(self):
        """
        method to inverse num and denom ints and return new fraction instance
        """
        #allowed because arguments only respect order or csvs, not identifiers
        return Fraction(denom, num)
