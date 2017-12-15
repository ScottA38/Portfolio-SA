"""
Seperate script for ex19.py to  reference test functions which don't require 'self'
"""
def checkFaceVals(lst):
    """
    test function to check for inconsistencies in data values for variables holding card face value names"""
    #debug
    print(f"Input list displays as {lst}")
    #check each value of the input list iteratively
    assert lst == ("1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"), "Values for base data list not displaying as expected"
    return True

def cardIter(deck_inst, debug_prints, suit_name, face_val):
    """
    Test function defined to iterate through all card object names in either the Deck's class attribute (card_names) or a specific Deck instance's 'deck' attribute.
    Within the for loop check each peice of data stored is concurrent with input data values and then go on to ensure no duplication of cards anywhere
    """
    #list which is populated via for loop with each card object's suit and value pairs in a tuple
    attrs = []
    if debug_prints:
        print(len(deck_inst))
    #iterate through all cards in the provided object list and save each suit and value pair to a dict. Detect for a duplicate with the dict for the current iterated instance of card.
    for card in deck_inst:
        #test if flag for printing back-end data to screen is True
        if debug_prints:
            print(f"{card} currently being iterated.")

        assert card.suit in suit_name, "    Card object's 'suit' name: {}, not found within recognised values".format(card.suit)
        assert card.value in face_val, "    Card object's 'value' name: {}, not found within recognised values.".format(card.value)
        #assert that an exact match of the current object's attributes as a tuple pair does not already exist
        assert (card.value, card.suit) not in attrs, "    Card duplication detected for: {}, {}".format(card.value, card.suit)

        #create tuple pair value to add to existing list
        new = (card.value, card.suit)

        #append to list
        attrs.append(new)
    if debug_prints:
        print("\n\n\n")
    return True

def confInstance(obj, class_name):
    """
    Take arguments for an object instanc and a class constrcutor id and return true if the given 'obj' argument is an instance of the constructor, False if not
    """
    #raise exception of obj is not an object
    assert isinstance(obj, class_name), "Given object {} is not an object instance of {}".format(obj, class_name)
