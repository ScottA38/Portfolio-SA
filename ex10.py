#define a function which checks to see if the current iteration number is
#is a multiple of 3 - takes current iteration no as arg
def fizz(no):
    #initialise return variable and set to none
    fmsg = None
    #moduko used to check if multiple of 3
    if no % 3 == 0:
        #if the number is a multiple of 3 the return variable is set to "Fizz"
        fmsg = "Fizz"
    return fmsg

#function to check if iteration number is a variable of 5 - if so change return string to "Buzz"
def buzz(no):
    #initialise return variable and set to 'None' for return value validation later on
    bmsg = None
    #modulo used to check if multiple of 5
    if no % 5 == 0:
        #if the number is a multiple of 3 the return variable is set to "Fizz"
        bmsg = "Buzz"
    return bmsg

#iterate through number 1-100 using 'for'
for no in range(100):
    #if both functions return non-null data
    if buzz(no) != None and fizz(no) != None:
        #print both func return statements on one line
        print(fizz(no), buzz(no))
    #if only fizz() returned a string
    elif fizz(no) != None:
        print(fizz(no))
    #if only buzz() returned a string
    elif buzz(no) != None:
        print(buzz(no))
    #if nothing returned a string
    else:
        print(no)
