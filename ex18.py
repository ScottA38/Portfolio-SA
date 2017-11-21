"""
Program to create a 'blueprint' for a car with specific attributes

Allows creation of car 'objects'
"""
import re

def valueInputs(inst_dict):
    #iterate through keys and (currently empty value of)
    for i, key in enumerate(newCar.instance_attrs.keys()):
        # have skipped vaildation temporarily because writing universal data input validation function for Python separately which I can import
        #taking input from the user
        attr_in = int(input(f"Please enter a {type(value)} type value for your car's {key} ->"))
        #assign the retrieved key and value pair to the inst_dict
        inst_dict[key] = attr_in

class newCar:
    # template array for filling in variables about the instance
    instance_attrs = {"manufacturer": "", "model": "", "doors": 0, "shape": "", "engine": 0.0, "colour": ""}

    def __init__(self, inst_dict):
        for key, value in instance_attrs

    def __str__(self):
        print(f"Here are the details about your {manufacturer}{model}")
        print(f"The {model}'s colour is {colour}")
        print(f"The {model}'s engine size is {engine}")
        print(f"Your {model}'s shape is {shape}")
        print(f"

print("Welcome to the car blueprinter! Programmed by SA)
#create loop for program execution unless exit specified by user
while exit_state == False:
    inst_dict = {}
    new_obj = None
    new_obj = str(input("Please enter the model and colour of your car with no spaces here -> "))
    string_check = re.compile(r"^[a-zA-Z]+$")
    if string_check.match(new_obj) == False:
        raise Exception('The value you have entered does not match the format required.')
    else:
        valueInputs(inst_dict)
