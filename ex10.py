#a functon call that takes any string argument and strips any whitespace characters
#including newline to allow fizz and buzz to print in one line when called together
def strip_whtspace(msg):
    #call lstrip() function on string arg
    result = msg.lstrip()
    #return
    return result

#iterate through 10 iterations using 'for' loop and range function
for no in range(100):
    #reset string variable to hold 'Fizz' to empty for each loop
    fmsg = ""
    #reset string variable to hold 'Buzz' to empty for each loop
    bmsg = ""
    #if iteration number is a multiple of 3
    if no % 3 == 0 :
        #set fmsg variable to "Fizz"
        fmsg = "Fizz"
    #if iteration number is a multiple of 5
    if no % 5 == 0:
        #set bmsg variable to "Buzz"
        bmsg = "Buzz"
    #if both fmsg/bmsg variable strings are empty 
    if fmsg == "" and bmsg == "":
        #set fmsg (1st in print statement) to iterator number converted to string
        fmsg = str(no)
    fmsg = strip_whtspace(fmsg)
    bmsg = strip_whtspace(bmsg)
    print(f"{fmsg}{bmsg}")
