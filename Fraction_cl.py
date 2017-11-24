"""
Current changes to issue:

    -Take all self instances out of simplifyFraction by calling it after each fraction has been called in startUp X(cannot do)
"""
class Fraction(object):
    #list of possible actions to perform on an initially created list
    ops = ['addition', 'subtraction', 'multiplication', 'division', 'inversion', 'decimalisation']

    #create an init file
    def __init__(self, num, denom):
        #debug
        # print("!init function!")

        #assign instance variables to ordinary identifiers for easy reference
        self.num = num
        self.denom = denom

    def commonDenom(self, operand):
        """
        find commmon denominator by multiplying denominators of fractions together and adjusting numerator values accordinglys

        Even 'self' attributes have to be assigned called via the 'self' instance: self.num | self.denom because the variables of just 'num' | 'denom' are
        only available in the __init__() scope where they are defined. They could be defined again (if desired) for each method for easy referencing
        """
        #debug
        # print("!commonDenom function!")

        num_1 = operand.denom * self.num
        num_2 = self.denom * operand.num
        denom_1 = operand.denom * self.denom
        return (num_1, num_2, denom_1)

    def simplifyFraction(self, hcf, cases):
        """
        Use a recursion process to find the highest common factor between a numerator and denominator
        in order to factorise.

        When calling this function the 'hcf' argument should be the same as the numerator argument, making sure that it does not recurse over values which are
        higher than the numerator (will never be hcf: do not accept top-heavy fractions). Also if the
        numerator entered for hcf is 1 the 1st base case 'hcf <= 1' is caught
        """
        #debug
        # print("!simplifyFraction function!")

        #if the hcf number has reached 1 or below then the process has failed and returning false
        #provides evidence of that instead of returning a number (this is a base case)
        if hcf <= 1:
            #user information about simplifyFraction process
            print(f"No HCF found, a total of {cases} numbers considered\n")
            #return original object (no common factors)
            return self

        #debug
        #print(f"case {hcf} (descending)")

        #specify a base case where both numbers are directly divisible by the hcf variable
        #second base case (?)
        if (self.num % hcf == 0) & (self.denom % hcf == 0):
            print(f"HCF of {hcf} found! a total of {cases} cases considered\n")
            return Fraction(int(self.num/hcf), int(self.denom/hcf))

        #decrement 'i' variable
        hcf -= 1

        #increment a re
        cases += 1

        #call the same function as a subfunction
        return self.simplifyFraction(hcf, cases)

    def oper(self, operation, operand):
        """
        take input of created initial fraction and argument for type of operation to perform (arithmetic)

        Currently I cannot think of another method to use to physically feed Pyhton the arithmetic function except for a big hairty if, elif.. statement
        """
        #debug
        # print("!oper function!")

        if operation == "addition":
            #inform user of the arithmetic operation to be performed by what operands
            print(f"Here is the {operation} of {self} & {operand}:\n")
            res = self + operand
            res.result(operation)

        if operation == "subtraction":
            #inform user of the arithmetic operation to be performed by what operands
            print(f"Here is the {operation} of {self} & {operand}:\n")
            res = self - operand
            res.result(operation)

        if operation == "multiplication":
            print(f"Here is the {operation} of {self} & {operand}:\n")
            res = self * operand
            res.result(operation)

        if operation == "division":
            print(f"Here is the {operation} of {self} & {operand}:\n")
            res = self / operand
            res.result(operation)

        if operation == "inversion":
            #inform user of action to be taken
            print(f"Here is the {operation} of {self}:\n")
            res = self.inversion()
            res.result(operation)

        if operation == "decimalisation":
            #inform user of action being taken
            print(f"Here is the {operation} of {self}:")
            flot = float(self)
            print(flot)

    def result(self, operation):
        """
        Give final output of user requests in simplified form
        """
        print(f"The unsimplified result is {self}")
        #call simplifyFraction to simplify result
        new = self.simplifyFraction(self.num, 0)
        print(f"The final result of the {operation} is {new}\n")

    def __str__(self):
        """
        create output if class object is called to a 'print' function
        """
        #debug
        # print("!__str__ function!")

        return(f"{self.num} / {self.denom}")

    def __add__(self, operand):
        """
        class method for add operator (only works with other fractions)
        """
        #debug
        # print("!__add__ function!")

        #unpack the variables of commonDenom. commonDenom will not be redognised unless attached to an instance of class such as 'self' or 'Fraction'
        num, add_num, denom = self.commonDenom(operand)

        #perform addition operation on numerator
        num += add_num

        return Fraction(num, denom)

    def __sub__(self, operand):
        """
        base method for subtracting current fraction by a variable
        """
        #debug
        # print("!__sub__ function!")

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
        #debug
        # print("!__mul__ function!")

        #multiply numerators and denominators together
        self.num *= operand.num
        self.denom *= operand.denom

        return Fraction(self.num, self.denom)

    def __truediv__(self, operand):
        """
        base method for dividing current fraction by a variable
        """
        #debug
        # print("!__div__ function!")

        #multiply each numerator with denominator of other fraction for division
        self.num *= operand.denom
        self.denom *= operand.num

        return Fraction(self.num, self.denom)

    def __float__(self):
        """
        base method for defining a floating point number from the current num and denom
        """
        #debug
        # print("!__float__ function!")

        return float(self.num / self.denom)

    def inversion(self):
        """
        method to inverse num and denom ints and return new fraction instance
        """
        #debug
        # print("!inversion function!")

        #allowed because arguments only respect order or csvs, not identifiers
        return Fraction(self.denom, self.num)
