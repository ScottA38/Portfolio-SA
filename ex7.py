#placeholder variable
current_savings = 0.0

#placeholder variable
annual_salary = 0

#placeholder variable
portion_saved = 0

#down payment multiplier
dp_multiplier = 0.2

#placeholder value total cost
total_cost = 0

#multiplier for 'r'
interest_multiplier = 1.004

#take input from user in GBP as whole number for annual_salary
annual_salary = input('Enter your annual salary: ')

#conv ann. salary to float
annual_salary = float(annual_salary)

monthly_salary  = annual_salary / 12

#take input from user for portion saved percentage and convert to int
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

#take input of property value and convert to float
total_cost = input('Enter the cost of your dream home: ')
#convert to float
total_cost = float(total_cost)

#find deposit amount given property cost
portion_deposit = total_cost * 0.2 #down payment is assumed ot be 20%

#incrementing index for total months savings required
months = 0

#while loop with condition that current_savings is less than portion_deposit
while current_savings < portion_deposit:
    #debug statement to show while has been triggered correctly
    print('Entered while!')
    print(current_savings)
    #caluculate 0.04% monthly interest from current savings amount
    monthly_interest = (current_savings * interest_multiplier) /12

    #add monthly interest to current savings (before or after salary addition?)
    current_savings = current_savings + monthly_interest

    #current savings is then added on to by percentage contribution for that month
    current_savings = current_savings + monthly_salary * portion_saved

    #increment by 1 the months variable for each loop of 'for'
    months += 1

print()
print()
print(f"The money required for a 20/% deposit on this house is {portion_deposit}.")
print(f"The amount of months required to save for this deposit using the given figures is {months}.")
