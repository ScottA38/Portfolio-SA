# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #iterate through characters in secret_word starting from index 0
    for char in secret_word:
        #condition to test if the current position in the string has not been guessed in the
        #letters_guessed array
        if char not in letters_guessed:
            #debug statement to ensure if has been/hasn't been triggered
            # print("\n*debug*Char does not match letters - return false.")
            return False
    #if for loop runs without triggering conditional return true
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #set empty string as output for user of current guessed letters
    string_output = ""
    #iterate through secret_word with iterator variable char
    for char in secret_word:
        #for each iteration test if the current position in the string matches any items in letters_guessed
        if char in letters_guessed:
            #if above condition is true append the current position in secret_word to the output string
            string_output += char
        #if above conditional is not true
        else:
            #for the current iteration add an underscore to the output string
            string_output += "_"
    #return string_output
    return string_output


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #intialise a variable 'alphabet' to hold a full lowercase alphabet list (each letter is a string in list)
    alphabet = list(string.ascii_lowercase)

    #intialise a string variable for return value
    letters = ""

    #iterate through letters_guessed list item by item
    for item in alphabet:
        if item in letters_guessed:
            #remove the specified iterable 'item' from list
            alphabet.remove(item)
    #debug
    # print(f"1st stage: new alphabet is - {alphabet}")

    #use for loop to iterate over all values in alphabet and return them back to string (following list() call) by concatenating on to letters variable each time
    for char in alphabet:
        letters = letters + str(char)
    #debug
    # print(f"2nd stage: new strinf is - {alphabet}")


    #previously to this I had string.ascii_lowercase still as a string, intitialised within the function and used exactly the same logic but with
    #alphabet.replace(item, "") - it worked intially but always reset itself after a loop, but now I cannot get it to work?

    #return not(letters_guessed) where U = string.ascii_lowercase
    return letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    #intialise a 'tries' variable as int
    user_attempts = 0

    #intialise amount of lives as an int remember to set condition to exit if the user's lives less than or equal to 1
    user_lives = 6

    #initialise string to hold successfully guessed letters in the secret_word
    letters_guessed = []

    #initialise a string which holds the character for user's guess
    user_guess = ""

    #set variable to hold output for get_guessed_word()
    display_current = get_guessed_word(secret_word, letters_guessed)

    print("Welcome to hangman. \nYour objective is to guess the letters before you run out of lives.")

    #message informing of length of word to be guessed
    print(f"\n\nYour opponent has selected a random word which is {len(secret_word)} characters long.")

    #enter while loop which will exit when user_lives is less than or equal to 1
    while user_lives > 0:

        #increment the user_attempts int value
        user_attempts +=1

        #informing user
        print(f"Your current amount of lives is: {user_lives}.")


        print("\n",get_guessed_word(secret_word, letters_guessed))

        print("\n\nThe range of letters which have not been guessed are as follows:\n")
        print(get_available_letters(letters_guessed))
        #intialise exit condition for while
        guess_ok = False
        #set up while with above bool variable as exit condition
        while guess_ok == False:
            #ask user for input of a single letter guess
            user_guess = str(input("Please enter a single character of the letters you wish to guess: ->"))
            #if guess is more than 1 character long
            if len(user_guess) > 1:
                #error message
                print("\n\nGuess was not a single letter, try again...")
            #else if guess does not match a character within string.ascii_lowercase
            elif user_guess not in string.ascii_lowercase:
                #error message
                print("\n\nGuess was not a recognised letter, try again (ensure lowercase)...")

            else:
                #debug to show that else is triggered
                # print("*debug*Guess is ok.")

                #.append() letters_guessed with user_guess if verification of entry has been passed
                letters_guessed.append(user_guess)

                #activate while exit condition
                guess_ok = True
        #conditional for if guessed char is within the secret_word
        if user_guess in secret_word:
            #success message
            print(f"\n\nThe guess {user_guess} is a letter in the target word!")
            #if is_word_guessed return value evaulates to true (all chars in word are successfully guessed)
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(f"\n\nWell done you have successfully guessed the word {secret_word}!\nIt took you {user_attempts} attempts.")
                break #use exit() or break??
        else:
            print(f"\n\nThe guess {user_guess} is not a letter in the target word")
            user_lives -= 1
        #debug
        # print(f"Here are all letters guessed so far: {letters_guessed}")

        #debug to check output of get_available letters before while loops
        # print("End of loop, available letters: ", get_available_letters(letters_guessed), "letters_guessed: ", letters_guessed)

    #comiseration if user runs out of guesses
    print(f"Unlucky, you ran out of guesses.... The secret word was {secret_word}\n\n")


secret_word = choose_word(wordlist)
hangman(secret_word)
