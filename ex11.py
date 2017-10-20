#import randominteger function from random module
from random import randint

#set starting lower bound for guess
low = 0

#set starting upper bound for guess
high = 75

"""
create random integer to guess through randint() and save to the obj_number variable

Note to self: this number will stay as the same value because it is not continually being re-parsed by
the for loop, as it is not within the for loop's local scope
"""
obj_number = randint(low, high)

#create a boolean variable for while loop to test each time until false
guessed = False

#loop until guessed is true
while guessed == False:
    """
    ask for a user input between specified ranges - range will be dynamic based on previous guesses, so string is formatted to include 'high' and 'low' variables.
    """
    user_guess = int(input("Please enter a whole number between {} and {}: ".format(low, high)))
    #validation condition to ensure that user's guess was not below or above the specified range
    if user_guess < low or user_guess > high:
        #print message informing user of incorrect guess attempt
        print("\nUser's guess is outside of expected range of numbers, please try again.\n")
        #use continue to reset back to the top of the 'for' loop without processing any more of the code below
        continue
    
    #check if user's guess is equal to the generated randint() number
    if user_guess == obj_number:
        #break while loop
        break
    #if the user guess was too low
    if user_guess < obj_number:
        #inform user of guess result
        print("Too low...")
        #set lower bound of guess range to current guess
        low = user_guess
    #use else with assumption that the number guessed has to be higher than obj_number (it has been tested for all other conditions)
    else:
        #inform user of guess result
        print("Too high...")
        #set upper bound of guess range to current guess
        high = user_guess

#congratulations message when while loop exits
print(f"Well done you guessed the number {obj_number} correctly!")
