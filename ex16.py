"""
Program to analyse song lyrics.

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

I kind of noticed something wasn't right
In your colorful face
It's kind of weird to me
Since you're so fine
If it's up to me your face'll change......

If you smilin', that should set the tone
Just be limber
And If you let go, the music should groove your bones
Just remember
Sing this song with me

Ain't nobody love you like I love you
You're a good girl and that's what makes me trust ya
Late at night, I talk to you
You will know the difference when I touch you

People are so phony
Nosy cause they're lonely
Aren't you sick of the same thing?
They say so and so was dating
Love you or they're hating
When it doesn't matter anyway
Cause we're here tonight

If you smiling, that should set the tone
Just be limber baby
And If you let go, the music should groove your bones
Baby just remember
Sing this song with me

Ain't nobody love you like I love you
You're a good girl and that's what makes me trust ya
Late at night, I talk to you
You will know the difference when I touch you

Yeah, you know I can make ya happy
I could change your life
If you give me that chance
To be your man
I won't let you down baby
If you give me that chance
To be your man
Here baby, put on my jacket
And then ...

Maybe we'll fly the night away (I just wanna love you baby)
Yeah, yeah, yeah
Girl
Maybe we'll fly the night away(I just wanna love you baby)
Girl ...

Ma, what you wanna do?
I'm in front of you
Grab a friend, see I can have fun with two
Or me and you put on a stage show
And the mall kids, that's how to change low
From them you heard "wow, it's the same glow"
Look at me, I say "yeah, it's the same dough"
We the same type, you my air of life
You have me sleeping in the same bed, every night

Go rock with me, you deserve the best
Take a few shots
Let it burn in your chest
We could ride down
Pumping N.E.R.D. in the deck
Funny how a few words turn into sex
Play this free, joint called "brain"
(I just love your, Brain)
Ma, take a hint
Make me suerve in the lane
The name Malicious
And I burn every track
Clipse and J. Timberlake
Now how heavy is that?

Maybe we'll fly the night away (I just wanna love you baby)
Yeah, yeah, yeah
Girl
Maybe we'll fly the night away(I just wanna love you baby)
Girl ...

Ain't nobody love you like I love you
(Can't love you like I do)
You're a good girl and that's what makes me trust ya
(Trust ya like I do)
Late at night, I talk to you
(Hey)
You will know the difference when I

Break this down

You know, I used to dream about this when I was a
little boy
I never thought it would end up this way, Drums
(Hey)
It's kind of special right? yeah
You know, you think about it
Sometimes people just destined
Destined to do what they do
And that's what it is
Now everybody dance.
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
        #save index number and corresponding word to dict
        freq_dict[item] = freq_count

    return freq_dict

word_match = re.compile(r"[\w'\.]+", re.IGNORECASE)


out = word_freq_dict(song_1)


print(out)
