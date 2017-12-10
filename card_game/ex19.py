from random import shuffle
import ex19_tests
from types import *

class Deck(object):
    card_names = ()
    def __init__(self):
        #intialise an empty tuple to store all card names in - note: needs to be populated in order to be able to use - *test this*
        self.deck = ()

    def deckOCards(self):
        """Nested iteration through card attribute base data:
        create unique names by concatenating base data values,
        create object of Card for each iteration utilising iterated base data as attribute values.
        Create an item in card_names of each object name created"""
        for_var = 0
        nested_var = 0
        while for_var < 4:
            for suit in suit_name:
                for value in face_val:
                    print(f"face_val = {value}, suit_name = {suit})
                    #concatenated for_var and nested_var in a string (separated by an underscore)
                    Deck.card_names += (str(for_var) + "_" + str(nested_var))
                    #create the card object for this specific case, with the name being referenced from Deck.card_names (name will be dyamically replaced by compiler)
                    Deck.card_names[-1] = Card(value, suit)
                    #increment nested_var for each nested iteration
                    nested_var += 1
            for_var += 1

    def deckCheck(self, obj):
        """
        Test function to try and verify the consistency of object data within the deck.
        Written with boolean argument to denote whether checking instance's deck attribute or Deck class' card_names attribute
        """
        assert type(obj) == BooleanType
        #check to see via boolean 'obj' variable whether the user wants to check the instance's deck or the class' deck
        if obj == True:
            #if test of input boolean argument determines True specify deck attribute as the object instance's tuple
            deck = self.deck
        else:
            #if test of boolean is False assign deck to the class' tuple
            deck = Deck.card_names

        #test if the length of the tuple is 52 items long (52 card deck), if not raise assertion error
        assert len(deck) == 52, "Amount of cards within given deck is incorrect."
        #call test function to verfiy the data for card objects within the deck
        cardIter(deck)
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
        return "the face value is {} & the suit is {}.".format(self.value, self.suit)

class Hand(object):

    def __init__(self, deck_inst):
        """
        Take the deck instance from the Deck class and introduce it inti
        """
        self.hand = ()
    def __str__(self):
        #intialise an empty string to take the final printed output
        out_hand = ""
        #initialise a for loop index, enumerate over self. hand in order to access an index
        for i, card in enumerate(self.hand):
            #this should give the index of the current iteration as the 'card number' followed by a triggering of the card class' in-built __str__ call
            #append this string value to the current out_hand string
            out_hand.append("Card {} is: {}\n".format(i, card))


    def makeHand(self, deck_in):
        while len(self.hand) < 7:
            #select a random number to index the current deck instance by using the current length of the deck argument instance and 1 as range
            index = (randint(1, len(deck_in.deck)) - 1)
            self.hand += deck_in.deck[index]

suit_name = ("Hearts", "Diamonds", "Spades", "Clubs")
royalty = ("Jack", "Queen", "King", "Ace")
face_val = ()

# iterate over 10 values with a counter starting from 1
for i in range(0, 9):
    #add current index no to tuple
    face_val += ((i + 1),)

#add the names of the monarchy titles to face_val title
face_val += royalty

#check the face_val list to ensure proper
if debug is True:
    checkFaceVals(face_val)

#generate a base tuple for the Deck class which holds the names of card objects
Deck.deckOCards()

if debug is True:
    Deck.deckCheck(False)
