from random import shuffle
from ex19_tests import *
import string

class Deck(object):
    #create a dict to store an 'object name': 'attribute value tuple' pair
    def __init__(self, suit_name, face_val, debug_prints):
        """
        create list to store all card names in for current version of a deck instance - note: needs to be populated in order to be able to use.
        Python console tests show that there is no need to clone the Deck.card_names data here in order to have data as independent of each other
        """
        #intialise an empty tuple to hold each object instance for cards
        self.cards = ()

        Deck.deckOCards(self, suit_name, face_val, debug_prints)

        #convert tuple to list such that it is mutable when using methods
        self.deck = list(self.cards[:])

        #randomise the order of the given deck
        self.shuffleThePack()

        #convert back to tuple so that the data is not mutable unless specified
        self.deck = tuple(self.deck)

    def __str__(self):
        out_tup = ()
        for card in self.deck:
            out_tup += (card,)
        return out_tup

    def shuffleThePack(self):
        shuffle(self.deck)

    def deckOCards(self, suit_name, face_val, debug_prints):
        """
        nested iteration through suit_name and face_val card attribute base data:

        create object of Card for each iteration, include iterated data as attributes in created object.

        Create an item in card_names of each object name created
        """
        #initialise while loop manual indexes
        for_var = 0
        nested_var = 0

        #nested iteration
        while for_var < 4:
            for suit in suit_name:
                for value in face_val:
                    #attribute output for each card (debug)
                    print(f"face_val = {value}, suit_name = {suit}")
                    #add tuple to cards
                    self.cards += (Card(value, suit),)
                    nested_var += 1
                for_var += 1


    def deckCheck(self, debug, debug_prints):
        """
        Test function to try and verify the consistency of object data within the deck.
        boolean argument 'flag' to denote whether to check instance.deck or Deck.cards
        """
        #by using 'types' module assert that 'flag' input is boolean ------ cannot get to work!! (Does not recognise BooleanType (NameError))
        # assert type(debug) == BooleanType
        #check to see via boolean 'obj' variable whether the user wants to check the instance's deck or the class' deck
        if debug:
            #if test of input boolean argument determines True specify deck attribute as the object instance's tuple
            deck = self.deck
        else:
            #if test of boolean is False assign deck to the class' tuple
            deck = self.cards

        #test if the length of the tuple is 52 items long (52 card deck), if not raise assertion error
        assert len(deck) == 52, "Amount of cards within given deck is incorrect, 52 expected {} receieved.".format(len(deck))
        #call test function to verfiy the data for card objects within the deck
        cardIter(self.deck, debug_prints, suit_name, face_val)
        return True


class Card(object):
    def __init__(self, value, suit):
        #assign variables passed into init to the object
        self.value = value
        self.suit = suit
    def __str__(self):
        """
        standard output of object's attributes for a print() call for the given object
        """
        return "{} of {}.".format(self.value, self.suit)


class Hand(object):

    def __init__(self, deck_inst):
        """
        Hand will not initiate without an object instance for deck *test for this*. Intiates an attribute for hand instance of .hand
        Calls makeHand (used for Hand.__init__ only) to generate the hand from the given deck instance
        """
        self.hand = ()
        #call the makeHand function with the input argument dack instance
        makeHand(deck_inst)

    def __str__(self):
        out_tup = ()
        for card in self.hand:
            out_tup += (card,)
        return out_tup

    def makeHand(self, deck_in):
        """
        Create a hand for the current player from a deck instance passed in as object and remove it from the deck instance's deck attribute
        """
        #initialise a variable for pciking a card from the deck
        pick_card = 0

        #assign the deck's list to a temporary variable
        while len(self.hand) < 6:

            #take a card from the input Deck instance and append it to the 'hand' tuple
            self.hand += deck_in.deck[pick_card]

            #convert self.deck to list and save to variable
            deck_lst = list(deck_in.deck)

            #remove this card from the current deck instance such that it cannot be re-picked within the given deck instance
            deck_lst.remove(pick_card)

            #overwrite the original <deck_instance>.deck with the new modified tuple
            deck_in.setattr("deck", tuple(deck_lst))

            #increment index of for loop
            pick_card += 1

def generateFaceVals(royalty, face_val):
    # iterate over 10 values with a counter starting from 1
    for i in range(1, 10):
        #add current index no to tuple
        face_val += (str(i),)

    #add the names of the monarchy titles to face_val title
    face_val += royalty

    return face_val

#assign boolean to toggle testing events in-script
debug = True

#flag whether test functions should output a print statement
debug_prints = True

#attribute base data
suit_name = ("Hearts", "Diamonds", "Spades", "Clubs")
royalty = ("Jack", "Queen", "King", "Ace")
face_val = ()
face_val = generateFaceVals(royalty, face_val)

#check the face_val list to ensure correct values
if debug:
    checkFaceVals(face_val)

deck1 = Deck(suit_name, face_val, debug_prints)

#such a redundant test case, but regardless... (check to see if item is an instance of Deck)
confInstance(deck1, Deck)

if debug:
    deck1.deckCheck(False, debug_prints)
    deck1.deckCheck(True, debug_prints)

hand1 = Hand(deck1)

print(hand1)

print(hand1)
