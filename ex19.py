from random import shuffle

suit_name = ("Hearts", "Diamonds", "Spades", "Clubs")
royalty = ("Jack", "Queen", "King", "Ace")
face_val = ()

# iterate over 10 values with a counter starting from 1
for i in range(0, 9):
    #add current index no to tuple
    face_val += ((i + 1),)

#add the names of the monarchy titles to face_val title
face_val += royalty

#run test
if checkFaceVals == False
    raise Excpetion('Base data for card face values is not as expected')

def checkFaceVals(lst):
    """
    test function to check for inconsistencies in data values for variables holding card face value names"""
    #debug
    print(f"Face_vals displays as {lst}")]
    #check each value of the input list iteratively
    for i in lst:
        if i not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        #if a match for the characters is not found at any point return false
        return (False, "Face_val not displaying correct values")
    return True

class Deck(object):
    orig_deck = ()
    def __init__(self):
        #intialise an empty list to store all card names in - note: needs to be populated in order to be able to use - *test this*
        self.deck = ()

    def deckOCards(Deck.orig_deck):
        """iterate through card attribute base data and create unique names by concatenating iterated values and add as records to self.deck and create unique classes
        of card by referencing the last entry from Deck.orig_deck for the class name and using the iterator variables for attributes"""
        for_var = 0
        while for_var < 4:
            for suit in suit_name:
                for value in face_val:
                    print(f"face_val = {value}, suit_name = {suit})
                    #save to deck list for referencing the card object's names
                    Deck.orig_deck += (str(value),str(suit))
                    #create the card object for this specific case, with the name being referenced from the list (this is one of the only ways to generate a class name dynamically)
                    Deck.orig_deck[-1] = Card(value, suit)

    def deckCheck(self, obj):
        #check to see via boolean 'obj' variable whether the user wants to check the instance's deck or the class' deck
        if obj == True:
            deck = self.orig_deck
        else:
            deck = Deck.orig_deck

        if len(deck) != 52:
            return (False, "Amount of cards within given deck is incorrect.")
        for


class Card(object):
    def __init__(self, value, suit)
    #assign variables passed into init to the object
    self.value = value
    self.suit = suit
