#type 'python3 <scriptname>' in terminal to open this script correctly

#printing string that announced calculations
print("These are how many animals I have:")

#The number here uses BIDMAS so the division is operated on the 30 before the 15 is added, making the final number 20

#printing a string followed by a calculation of '15 + 30 / 6' on same line
print ("Cows", 15 + 30 / 6)

#printing a string of 'Sheep' followed by 100 - 30 * 3 % 4

#3 % 4 evaluates to 3? Understand modulos
print("Sheep", 100 - 30 * 3 % 4)

#printing a string announing counting plants
print("Now I will count my plants:")

#printing long calculation using basic operators including modulo - modulo result will be 2
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#printing string with calculation question
print("Is it true that 3 + 2 < 5 - 7?")

#printing calculated number from calculation listed in previuos print statement
print(3 + 2 < 5 - 7)

#printing string with question about addition calculation followd by result on same line
print("What is 3 + 2?", 3 + 2)

#printing string with question about subtraction calculation followed by result on same line
print("What is 5 - 7?", 5 - 7)

#printing question about calculation query above and why the output is 'false'; it is so because '<' operator makes the statement a conditional statement
print("Can you see why that printed False earlier?")

#the example .pdf shows "5 ? -2" here but this is a syntax error on mac

#asking 3 questions about the values of different numbers opposed to each
#other through a greater/equal or less/equal statement and printing the result on the same line
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
