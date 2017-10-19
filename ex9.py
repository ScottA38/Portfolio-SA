#placeholder variable
current_savings = 0.0

#multiplier for semi_annual raise value (percentage)
biannual_raise = 0.07

#property value is £1m
total_cost = 1000000.0

#percentage required for down payment
percentage_deposit = 0.25

down_payment = total_cost * percentage_deposit

#100 pounds leeway for savings amount
epsilon = 100.0

#multiplier for 'r' - a monthly fraction of this (0.04/12) is granted to the user per month based on savings invested?
interest_multiplier = 1.004

#take input from user in GBP as whole number for annual_salary
annual_salary = input('Enter your annual salary: ')
#conv ann. salary to float
annual_salary = float(annual_salary)

monthly_salary  = annual_salary / 12

def calculate_monthly_interest(savings_for_month):
    #caluculate 0.04% monthly interest from current savings amount
    monthly_interest = (savings_for_month * interest_multiplier) /12
    return monthly_interest

def save_per_month(perc_save):
    saving = monthly_salary * perc_save
    return saving

def savings_total(perc_save, annual_salary, current_savings):

    #iterator for the period of 36 months
    for month in range(36):

        #conditional to ascertain if iteration of months is divisible by 6 (biannual_raise) (and that it is not the 1st month of iteration)

        #This is actually a retrospective calculation because due to the 0 index of range function in range months % 6 would actually be the 7th iteration
        #It does not matter in this instance however because the salary multiplier is applied before any calculations are performed upon current_savings
        if month % 6 == 0 and month != 0 :

            #debug to check that if conditional is being triggered
            print("Raise gained!")

            #calculate raise effect on annual salary. The rest of the figures will recalculate dynamically
            annual_salary = annual_salary * biannual_raise

            #debug to check annual raise is increasing correctly
            print(f"New salary is {annual_salary}")

    #add monthly salary to current current savings
    savings_for_month = current_savings + save_per_month(perc_save)

    #calculate interest based upon the total current investiture
    current_savings = calculate_monthly_interest(savings_for_month)

    return current_savings

low = 0

high = 10000

perc_save = (low + high)/2

guess = savings_total(perc_save, annual_salary, current_savings)

exit_clause = False

while exit_clause == False:
    if guess <= (total_cost - epsilon):
        low = guess
    elif guess >= (total_cost + epsilon):
        high = guess
    elif (total_cost - epsilon) <= guess <= (total_cost + epsilon):
        exit_clause = True
    elif high - low < 1:
        print ('The given salary figure cannot achieve the required down payment within the specified 36 month savings period.')
        break

if exit_clause == True:
    #show percentage of salary that was found by bisection as optimal for the constraints
    print(f"The optimal percentage of salary for a 25/% deposit on a £1m home within 36 months is {perc_save}.")
