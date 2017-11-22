class Fraction(object):

    #create an init file
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        """
        create output if class object is called to a 'print' function
        """
        print(denom + "/" + num)

    def newInput(subject, binary):
        """
        modular function to take int input from the user
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

    def simplifyFraction(hcf, num, denom):
        """
        Use a recursion process to find the highest common factor between a numerator and denominator
        in order to factorise
        """
        #if the hcf number has reached 1 or below then the process has failed and returning false
        #provides evidence of that instead of returning a number (this is a base case)
        if hcf <= 1:
            return False

        print(f"case {hcf} (descending)")
        #specify a base case where both numbers are directly divisible by the hcf variable
        #second base case (?)
        if (denom % hcf == 0) & (num % hcf == 0):
            print("hcf found!")
            return hcf

        #decrement 'i' variable
        hcf -= 1

        #call the same function as a subfunction
        return commonFactor(hcf, num, denom)

    def __add__(self, var_num, var_denom):
        """
        class method for add operator (only works with other fractions)
        """
        #unpack the variables of commonDenom
        num, add_num, denom = commonDenom(num, denom, var_num, var_denom)

        #perform addition operation on numerator
        num += add_num

        #assign the highest common factor of fractions to 'div'
        div = simplifyFraction(num, num, denom)
        if not div:
            return Fraction(num, denom)
        else:
            #division on found hcf for fraction (num and denom) and return into new fraction instance
            return Fraction(int(num / div), int(denom / div))

    def __sub__(self, var_num, var_denom):
        """
        base method for subtracting current fraction by a variable
        """
        #common denom & modify numerators acordingly
        num, sub_num, denom = commonDenom(num, denom, var_num, var_denom)

        #perform operation
        num -= sub_num

        #call simplifyFraction to find hcf of num and denom
        div = simplifyFraction(num, num, denom)
        if not div:
            #return new fraction object
            return Fraction(num, denom)
        else:
            #divide numerator and denominator by hcf and give as int for new Fraction object
            return Fraction(int(num / div), int(denom / div))


    def __mul__(self, var_num, var_denom):
        """
        base method for multiplying current fracton by a variable
        """
        #multiply numerators and denominators together
        num *= var_num
        denom *= var_denom

        #call simplifyFraction
        div = simplifyFraction(num, num, denom)
        #catch if simplifyFraction returns False
        if not div:
            return Fraction(num, denom)
        else:
            return Fraction(int(num / div), int(num / div))

    def __div__(self, var_num, var_denom):
        """
        base method for dividing current fraction by a variable
        """
        #multiply numerator with denominator of other fraction
        num *= var_denom
        denom *= var_num

        #call simplifyFraction
        div = simplifyFraction(num, num, denom)
        #conditonals to catch if simplifyFraction returns false
        if not div:
            return Fraction(num, denom)
        else:
            return Fraction(int(num / div), int(num / div))


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
