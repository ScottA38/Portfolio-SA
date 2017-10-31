"""
Fix to function.

Using a while loop and starting with an index value as large as:
len(L1) -1.  Set this as a manual index number and decrement each time only if remove has not been called.
- not affected by the .remove() resetting python's internal for index.
"""


def remove_dups(L1, L2):
    """
    Define a function which iterates through L1.
    The element in the list which is currently being looped over is compared with all the variables in L2,

    If a match is found the current loop element of L1 - 'e' is removed from the L1 list.
    """
    #initialise index for 'for' loop (debug)
    index = 0

    #intialise an empty array for for loop
    L3 = []

    #start iterator over L1 with temporary element variable e
    for e in L1:
        print(index)
        #for each element in L1 check if element 'e' is not in L2 in any position
        if e not in L2:
            L3.append(e)
        #index number for tracking for loop in execution (debug)
        index += 1
        #output L1 and L2 to screen for
        print(L1, "\n")
        print(L2, "\n")
    return L3

def remove_dups2(L1, L2):
    """
    Alternative process for incrementing through data in loop L1 without editing data directly.
    Because L3 is the data subject being iterated through here you do not need to worry about
    """
    L3 = L1[:]
    for e in L3:
        if e in L2:
            L1.remove(e)

def remove_dups3(L1, L2):
    """
    Alternative process for remove_dups. Set a while loop with a manual index
    """
    #initialise index variable
    index = 0
    #create a while loop with a continuous condition
    while 1:
        print(index)
        if index > (len(L1) - 1):
            break
        #Reference the index number of the loop as an index
        if L1[index] in L2:
            L1.remove(L1[index])
        #if the if condition is not triggered then increment value
        else:
            index += 1
        print(L1)

def remove_dups4(L1, L2):
    """
    An example with assignment where this function will be assigned to variable L1 in global scope and the values
    temp in local scope will overwrite it's existing values
    """
    #convert args to tuple in local scope??
    temp = []
    for e in L1:
        if e not in L2:
            temp.append[e]
    return temp


#list L1
L1 = [1, 2, 3, 4]
#list L2
L2 = [1, 2, 5, 6]

#Call function with L1 and L2 as arguments - don't need to assign as .remove() is data mutation
remove_dups3(L1, L2)

#print the mutated data
print("\n\nL1 is now: ", L1)
print("L2 is now: ", L2)
