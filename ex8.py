#placeholder variable
current_savings = 0.0

#placeholder variable
annual_salary = 0

#placeholder variable
portion_saved = 0

#placeholder value (semi_annual raise value)
semi_annual = 0.0

#placeholder value total cost
total_cost = 0

#multiplier for 'r'
interest_multiplier = 1.004

#take input from user in GBP as whole number for annual_salary
annual_salary = input('Enter your annual salary: ')

#conv ann. salary to float
annual_salary = float(annual_salary)

monthly_salary  = annual_salary / 12

#taking user input with prompt for semi-annual raise percentage and converting to int, then saving into variable
semi_annual = float(input('Please enter your expected semi_annual raise amount as a decimal percentage: '))

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
    #print('Entered while!')
    #print(current_savings)

    #using modulo to ascertain if month incrementation in 'while' is divisible by 6 (semi-annual)
    #if this is the case trigger 'if'
    if months % 6 == 0 :
        print("Raise gained!")
        print(f"New salary is {annual_salary}")
        #calculate raise effect on annual salary. The rest of the figures will recalculate dynamically
        annual_salary = annual_salary + (semi_annual * annual_salary)

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
