"""
fixed value for hotel value cost - kept outside of function
so it can only be referenced and not changed in function scope
"""
accom_per_night = 70
#set fixed variable for car hire per-day cost (without considering discounts)
car_hire = 30
#create an array of city names as strings corresponding to their value (GBP) to get to them by airline
airl_costs = {"New York": 2000, "Auckland": 790, "Venice": 154, "Glasgow": 65}
#array of class names and correponding
airl_class = {"Economy": 1.0, "Premium Economy": 1.3, "Business Class": 1.6, "First Class": 1.9}

#define a function which creates an array of indexed values from an existing associative array
def key_index(array):
    #create an assoc array from the key of the associative array referenced as arg in data_entry
    indexed_array = list(array.keys())
    return indexed_array

#function template used to individually assign to different variables using
#subject is the data subject to be selected (such as city), array arg passes list of options as string
def data_entry(subject, array):

    #assign output of key_index(array) function to a specific key list
    key_list = key_index(array)

    #iterate through city_index.items()
    while 1:

        #enter blank line for visual clarity for user
        print("")

        iterator = 0

        for i, value in enumerate(key_list):
            # print(i)
            # iterator = str(i)
            #for each entry in the list print an index number and the location string so the correct spelling can be identified
            print(f"Location {i}:   \"{value}\".")

        #take city name input from user
        choice = int(input("\n\nPlease copy a corresponding number for the {} name from above to choose that option: ".format(subject)))

        #initialise variable to index iterations in for loop
        index = 0

        #iterate through key
        for target in key_list:
            if choice == index:
                #success message (debug: for loop works for a selection)
                print(f"\n{subject} successfully chosen.")
                #assign value to be returned associated value of index selected variable in LIST of keys created by key_index(array)
                choice_key = key_list[index]
                #for loop condition achieved - break out of for loop
                return choice_key
            index +=1
        #if for loop exhausts all iterations and match is not found alert user that selection has not been found - restart while
        print(f"\n{subject} entered does not match a recognised {subject} within this program. \n Please read list and try again.")

#define a function to take arg 'nights' and calculate the cost of a stay
def hotel_costs(nights):
    #times fixed accom_per_night value by amount of nights stayed within accomodation - assign to accom_cost
    accom_cost = accom_per_night * nights
    #return accom_cost
    return accom_cost

#define a function which calculates the total cost of airline travel to a destination
def plane_ticket_cost(city, airl_class):
    ticket_value = airl_costs[city] * airl_class
    return ticket_value

def rental_car_cost(days):

    #times argument integer 'days' by the fixed car hire cost
    rental_cost = car_hire * days

    #apply a conditional statement to days to find out if rental period is greater than 7 days
    if days > 7:
        #apply associated discount for rental period >7 days
        rental_cost = rental_cost - 50

    #apply else if conditional to days to find out if rental period is greater than 3 days (have proven not greater than 7)
    elif days > 3:
        #apply associated discount for rental period >3 days
        rental_cost = rental_cost -30

    #return calculated rental cost
    return rental_cost

def total_costs(city, days):
    #input both user-specified city and airl_class variables into plane_ticket_cost() function to calculate total airline cost
    #airl_class is global so referencable in this scope.
    plane_c = plane_ticket_cost(city, airl_class)

    #calculate hotel costs based on the user-specified no of nights/days.
    #Argument nights is in global scope so if referenceable within this scope
    hotel_c = hotel_costs(nights)

    #calculate car hire costs based on specified trip length (days)
    #days is global so referencable in scope.
    rental_c = rental_car_cost(days)

    #prints output of each indvidual calculation for cost and all added together
    print(f"\nThankyou for supplying the requested information.\n\n Based on your inputs I calculate your airline charges will be {plane_c}, your hotel charges will be {hotel_c} and your rental will be {rental_c}")
    total_c = plane_c + hotel_c + rental_c
    print(f"This means that the estimated total cost of your trip is {total_c}")

#welcome message
print("Welcome to SA's trip travel cost calculator...\n\n\n")

#ask user for integer input of number of nights and convert to int
days = int(input("\nPlease enter the number of days you wish to stay at your specified destination (in whole numbers): "))

#calculate corresponding number of nights to days
nights = days - 1

#ask user for city destination selection - return value - an index value corresponding to specific entry in dict
city = data_entry("city", airl_costs)

#ask user for airline class selection -
airl_class = data_entry("Airline class", airl_class)

#call function which calls all relevant associated functions to calulate all other
total_costs(city, days)
