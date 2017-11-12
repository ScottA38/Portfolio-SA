"""
Program to analyse song lyrics.

1) Open a .txt file and read() contents to a string (song lyrics)

2) A regex to find each word without surrounding punctuation and using re.findall()

3) Save results of 2) into a list (will be duplicates)

3) Use the set() function on the saved list of strings and save as a new variable - reduce the returned list in 2) to ONLY unique values

5) initiate an empty dict value

4)iterate through the unique values in the list with set() applied, and through a nested iteration within this loop to check how many times the unique list item
    matches with all the words in the song (from return of 3))

5)For each match of a string value from the unique list within the full list of lyric word items increment a frequency count by 1
    Make sure this frequency count is reset to 0 for each new unique word (each new iteration of the 1st for loop - non-nested)

6) Each time the nested for loop completes save the results to the dict as empty_dict[unique_word] = frequency_count

Objectives:

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
from sys import argv
import re

script, txt_name = argv

def open_txt(txt_name):
    #txt_name append with ".txt"
    song_name = txt_name + ".txt"

    #open txt_file in 'read' mode
    lyrics_file = open(song_name, "r")

    #read contents of file and save to a variable
    song_lyrics = lyrics_file.read()
    return song_lyrics

#take 2 arguments for input function, subject string and maximum frequency number
def take_input(subject, max_no):
    #print statement to inform user what upper bound of frequency entry is
    print(f"\nInteger entry: the maximum number to enter is {max_no}")

    #initiate empty variable to hold number entered by user, save as string so as not to satisfy while conditon
    usr_num = ""

    #intiate while loop with open condition (infinite)
    while True:
        try:
            #take user input as an integer
            usr_num = int(input("\nPlease enter a minimum {} frequency number: ".format(subject)))
            if (usr_num > max_no | usr_num < 0):
                #giving user notification of the fault
                print("\nPlease enter a number within the range of: 0 and {max_no}")
                #technically not necessary
                continue
            else:
                return usr_num
        except ValueError:
            print("Please enter an integer value!")

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

    #compile regex statement to capture all words without spaces or parenthesis but including backticks in their use
    word_match = re.compile(r"[\w'\.]+", re.IGNORECASE)

    #return list of all word matches within the lyrics string
    word_list = re.findall(word_match, song_name)

    #set a variable to hold the 'set' (all unique values) in a list
    word_set = set(word_list)

    #convert word_set beck to a list and reassign to itself
    word_set = list(word_set)

    #debug by printing output of word_set
    print(f"\n\nword_set is: {word_set}")

    #debug to show output of word_list
    print(f"\n\nword_list is: {word_list}")

    #debug: print type output of word_list
    # print(f"word_list's data type is {type(word_list)}")

    #count for 1st loop
    loop_count = 0

    # iterate through all items in word_set (unique words in the song)
    for item in word_set:

        #debug loop count for nested for loop
        nested_count = 0

        #debug to check what words from word_set the first for loop is iterating over
        print("This item in word_set is: ", item)

        #intiate an int value to index the amount of times 'if' tests true within nested for loop
        freq_count = 0

        #this is using nested for to search for the iteration variable in the first for loop within the items of word_list
        for wrd in word_list:

            #Compares iteration variable (item from word_set, lyric words listed uniquely) with the word_list value corresponding with the current index
            #this was previously not function due to the comparison method used in an 'is' statement. I presume that the state of 'item' changed after one matches
            #because after freq_count reached one for all words it would not go higher despite finding matches
            if item == word_list[nested_count]:

                #debug to ouput that 'if' has triggered
                print(f"If' triggered!")

                #increment inde value by 1 if the target word is found within the lyrics
                freq_count += 1

            #debug to return status indicators of nested 'for'
            # print(f"loop_count, nested_count = {loop_count},{nested_count}, current word in word_list = {word_list[nested_count]}, current freq_count = {freq_count}")

            #nested loop count increment
            nested_count += 1

        #save index number and corresponding word to dict
        freq_dict[item] = freq_count

        #increment intial loop's count
        loop_count += 1

        print(f"loop_count = {loop_count}")

    return freq_dict

#function to return a shorter dict where all frequency values are above the input integer
def min_freq(min_int):

    #debug of input arg
    print(f"\n\nmin_int = {min_int}")
    #initiate an empty list to hold return values
    flist = []

    #intialise an empty tuple for holding ([list], freq) pairs
    out_tup = ()

    #iterate over the keys of 'out' dict, incrementing an int value by 1 each time and hoping to get the right answer
    for i, word in enumerate(out.keys()):
        #debug to check loop variables
        print(f"the current freq_iterable is: {freq_iterable} and word is {word}.\n\nout[word] = {out[word]}")

        #conditonal to check whether the loop has iterated through to higher than the maximum possible frequency value
        if freq_iterable > max(out.values()):
            return out_tup

        #check to see if current key value word has a corresponding frequency EQUAL TO frequency_iterable
        elif out[word] == freq_iterable:
            #debug to see if conditional triggers and
            print(f"{word} matches count of freq_iterable!")
            flist.append[word]

        #concatenate the list of words for the given frequency to the original out_tup
        out_tup = out_tup + (flist, freq_iterable)

        #increment freq_iterable by 1
        freq_iterable +=1
    return out_tup


#call function to a local .txt file listed with argv
lyrics = open_txt(txt_name)

#calls function which analyses frequencies of each unique word in the lyrics and returns a dict of
#"word: frequency pairs"
out = word_freq_dict(lyrics)

print(f"The max lyric frequency in the dict is: {max(out.values())}")

#save tuple output for maximum frequency words in lyrics to 'max_tuple' by specifying the maximum frequency value in the dicts
max_tuple = min_freq(max(out.values()))

print(max_tuple)

#call function to take input from user as integer for minimum frequency
user_int  = take_input("lyric", max(out.values()))
