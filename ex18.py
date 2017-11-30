"""
Program to create a 'blueprint' for a car with specific attributes

Allows creation of car 'objects' with attributes that can be manipulated after creations
"""
import string

def setVals():
    """
    basic function to concatenate all the numbers from 0 to 9 on the end of the english alphabet (all accepted characters)
    and a space
    """
    str_vals = string.ascii_lowercase
    for i in range(1,10):
        str_vals = str_vals + str(i)
    #add a space into character range
    str_vals = str_vals + " "
    return str_vals


def attrEntry(attr_name):
    """
    Takes NewCar.attrs dict
    as argument (intended usage)
    """
    #intialise a boolean exit condition to upcoming while loop
    exit_state = False

    #intialise variable for flagging if string has any illegal characters (break out if fault found with word)
    verif = True

    #create loop for program execution unless exit specified by user
    while exit_state == False:

        #initialise reference to required data type of the attribute value being taken. indexes into NewCar.attrs
        attr_type = str(type(NewCar.attrs[attr_name]))

        #take input from user as to the value for a given object attribute
        new_attr = input("Please enter the {} of your car as {} with no spaces here -> ".format(attr_name, attr_type))
        print(f"New value for {attr_name} is {new_attr}.")
        #debug
        # print(f"List of accepted characters is '{setVals()}'")
        #ask if string matched inside of stored string for attr_type
        if "str" in attr_type:
            #iterate through characters in input string
            for char in new_attr:
                #debug
                # print(f"Current word char is {char}.")
                #convert iterated character to lowercase in order to ensure it matches with lowercase alphabet (string.ascii_lowercase)
                if char.lower() not in NewCar.str_val:
                    print("One or more characters entered for text (string) value not allowed.")
                    #reassign value of verif to FALSE - skip rest of while block and restart input (condition maintained: exit_state == False)
                    verif = False
                    break
            #debug
            print(f"Verif after for loop is: {verif}")
            if verif == True: #if an illegal character hasn't been found
                return new_attr

        elif 'int' in attr_type:
            try:
                int(new_attr)
                return new_attr
                #catch error assigning to correct data type
            except ValueError:
                #give error report
                print("A whole number (integer) value is required, please try again.")
        elif 'float' in attr_type:
            try:
                float(new_attr)
                return new_attr
            except ValueError:
                #give error report
                print("An decimal point (floating point) number is required, please try again.")
        else:
            raise Exception("An error occurred recognising data type in attrEntry")

class NewCar(object):
    # template dict for filling in variables about the instance
    attrs = {"manufacturer": "", "model": "", "doors": 0, "shape": "", "engine": 0.0, "colour": ""}
    str_val = setVals()

    def __init__(self):
        self.valueInputs()

    def __str__(self):
        #initalise an empty string for return value
        printout = ""

        for i, key in enumerate(NewCar.attrs.keys()):
            #if iterating over "model" then continue as this infomation is displayed in all other print statements
            if key == "model":
                continue
            else:
                attr_name = key
                #return stored value for a attribute name stored in object and save to attr_value
                attr_value = getattr(self, attr_name)
                if i == 0:
                    printout = "\nYour {}\'s {} is {}\n".format(self.model, attr_name, attr_value)
                else:
                    printout = printout + "\nYour {}\'s {} is {}\n".format(self.model, attr_name, attr_value)
        return printout

    def valueInputs(self):
        #iterate through keys and (currently empty value of)
        for i, key in enumerate(NewCar.attrs.keys()):

            #save variable for easy referencing in print(f"")
            type_req = type(NewCar.attrs[key])

            #taking input from the user
            attr_in = attrEntry(key)

            #debug
            print(f"*valueInputs* New attribute entry is: '{attr_in}'")
            #assign the value of attr_in
            setattr(self, key, attr_in)

    def terminate(self):
        while True:
            make_change = str(input("\nDo you want to amend any details of the car entered? enter 'Y' for yes and 'N' for no ->"))
            if 0 > len(make_change) | len(make_change) > 1:
                print("Too many/too few characters entered.")
            elif make_change.lower() == 'y':
                return True
            elif make_change.lower() == 'n':
                exit(0)
            else:
                print("Character entered not of correct value, please try again")

    def changeAttr(self):
        #terminate function should only be able to return true or exit the program altogether
        self.terminate()
        print("Which feature of your car would you like to amend?")
        #iterate through attribute names from dict stored in class
        for i, value in enumerate(NewCar.attrs.keys()):
            print(f"[{i}]: The {value}")
        verif = False
        while verif == False:
            try:
                attr_select = int(input("Please enter a number from the above list matching the attribute you wish to change ->"))
                if attr_select in range(0, (len(self.attrs) - 1)):
                    verif = True
                else:
                    print("Number entered is out of the range of possible values, please try again.")

            except ValueError:
                print("Incorrect data type entered, please try again.")

        #use for loop to re-access key indexes from NewCar.attrs dict and therefore determine what the selection was that was made by the user
        for i, value in enumerate(NewCar.attrs.keys()):
            if i == attr_select:
                confirmed_attribute = value
        new_value = attrEntry(confirmed_attribute)
        setattr(self, confirmed_attribute, new_value)

print("Here is a car blueprinter! Programmed by SA")

#ideally I'd like to be able to program class names dynamically but I can't see a way to do this yet in Python that I can understand
AnInst = NewCar()

#print using __str__() function to output all attributes
print(AnInst)

AnInst.changeAttr()
