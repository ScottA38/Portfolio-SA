class Fraction(object):
    i = 0

    #create an init file
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    #create output if class object is called to a 'print' function
    def __str__(self):
        print(denom + "/" + num)

    def commonDenom(self, num, denom, var_num, var_denom):
        #create equivalent numerator/denominator fraction values as if you had timesed the bottom denominators by each other
        num_1 = var_denom * num
        num_2 = denom * var_num
        denom_1 = var_denom * denom
        return (num_1, num_2, denom_1)

    def factors(self):
        if i > 
        if denom % num == 0 & num

    def simplifyFraction(self, num, denom):



    #class method for add operator (only works with other fractions)
    def __add__(self, var_num, var_denom):
        num, add_num, denom = commonDenom(addFrac)
        num += add_num

        return Fraction(num)

    #base method for subtracting current fraction by a variable
    def __sub__(self, var_num, var_denom):

        return Fraction(num, denom)

    #base method for multiplying current fracton by a variable
    def __mul__(self, var_num, var_denom):

        return Fraction(num, denom)

    #base method for dividing current fraction by a variable
    def __div__(self, var_num, var_denom):
        return(float(num / value) / denom)

    #base method for defining a floating point number from the current num and denom
    def __float__(self):
        return Fraction(num, denom)

#initialise a boolean operator which specifies exit condition for the loop
exit_cond = True
