"""
Program to analyse song lyrics.

1) Function retreives a string with all lyrics of a song within it

2) A regex to find each word without surrounding punctuation and use re.findall() to save into a list where each item is a word string (will be duplicates)

3) Use the set() function on the saved list of strings and save as a new variable - this will reduce the returned list in 2) to ONLY unique value
    - print output

4)

Initially the program will analyse the frequency of each unique word, saving the string
- number pair in a dictionary each time

The program should also find the 'mode' word/s (or most frequent word) -storing in a list

The program should also return a tuple containing the list
mentioned above and the frequency.

A secondary function of the script is to ask for a user input (int only).

Following this input a list should be returned and printed to screen of tuple pairs:
(words_for_freq, freq_int). Only lyrics with a frequency count higher than the user input should
be output to screen for this.

Information required:

- lyrics text to interpret (string)
- user-defined integer

"""
import re

song_1 = """Just somethin' about you
Way I'm lookin at you whatever
keep lookin at me
Gettin' scared now, right?
Don't fear me baby, it's just Justin
It feel good right?
Listen
"""

#note_to_self: python parses string with a newline as: Alkjsdflds/slkajsdas/n (newline char on same line, not line after)

def word_freq_dict(song_name):
    """
    This function takes a song's lyrics in a string as an argument.

    It then calls a regex referenced in global scope and the re module's findall() to separate all the words in the program into a long list (non_unique).

    Iterating throught the output of this list from within the 'set()' function (unique values only) we then check via nested for
    loop for the frequency of this word within the lyrics - the corresponding word and frquency pair are stored in a dictionary to be returned
    """
    #convert all alphabetic characters the input string of lyrics of the input string to lowercase and save back to save variable name
    song_name = song_name.lower()

    #declare empty dict to return
    freq_dict = {}

    #return list of all word matches within the lyrics string
    word_list = re.findall(word_match, song_name)

    print(" ")
    print(" ")
    print(word_list)
    #set a variable to hold the 'set' (all unique values) in a list
    word_set = set(word_list)

    #convert word_set beck to a list and reassign to itself
    word_set = list(word_set)

    kind = type(word_list)
    #debug: print output of word_list
    print(f"word_list's data type is {kind}")
    # print(word_list)


    for item in word_set:

        print("This item in word_set is: ", item)

        #intiate an int value to index the amount of times 'if' tests true within nested for loop
        freq_count = 0

        #initiate nested for to iterate through the list of stored
        #this is using nested for to search for matches of 1 list item x number of times in another - is there a predefined function to do this?
        for wrd in word_list:
            #conditional for equivalent strings when converted to lowercase
            if wrd is item:
                #increment inde value by 1 if the target word is found within the lyrics
                freq_count += 1
                print(wrd + str(freq_count))
        #save index number and corresponding word to dict
        freq_dict[item] = freq_count

    return freq_dict

word_match = re.compile(r"[\w'\.]+", re.IGNORECASE)


out = word_freq_dict(song_1)


print(out)
