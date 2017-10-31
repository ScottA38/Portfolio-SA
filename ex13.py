"""
this function does not work in the current state as when you are altering the length of a list in a 'for' loop it resets the
internally held index number of the for loop.
"""


def remove_dups(L1, L2):
    """
    Define a function which iterates through L1.
    The element in the list which is currently being looped over is compared with all the variables in L2,

    If a match is found the current loop element of L1 - 'e' is removed from the L1 list.
    """
    #initialise index for for loop
    index = 0

    #start iterator over L1 with temporary element variable e
    for e in L1:
        print(index)
        #for each element in L1 check if element 'e' is in L2 in any position
        if e in L2:
            #if conditional returns true remove the element from L1
            L1.remove(e)
        index += 1
        print(L1, "\n")
        print(L2, "\n")


#list L1
L1 = [1, 2, 3, 4]
#list L2
L2 = [1, 2, 5, 6]

#Call function with L1 and L2 as arguments
remove_dups(L1, L2)
