#type 'python3 <scriptname>' in terminal

#enter data as

my_name = input('Please enter your full name-->')
my_age = input('Please enter your age-->')
my_age = int(my_age)
my_height = input('Please enter your height in metres-->')
my_height = float(my_height)
my_weight = int(input('Please enter your weight-->'))
my_eyes = input('Please enter your eye colour-->')
my_hair = input('Please enter your hair-->')

eye_colours = {"blue": "Blaues augen!", "green": "Green as spring leaves....", "brown": "Brown as the autumn foliage...", "red": "WTF!", "yellow": "Sorry?!", "white": "See a doctor."}
hair_colours = {"brown": "Braune haare!", "blonde": "Ja, naturlich! Das ist schon.", "red": "Is it dyed??", "ginger": "Brother from an another mother..", 'white': 'Is it dyed??'}

def check_age(age):
    if age < 20:
        print("Spring chicken!")
    elif age > 45:
        print("Still young! :)")
    else:
        print("Hello young man/woman!")

def check_height(height):
    if height < 1.5:
        print("Grab a footstool!")
    elif height > 1.8:
        print("Duck for the door!")
    else:
        print("MittelgroB")

def check_weight(weight):
    print("Weight is irrelevant, be happy!")

def check_eyes(eyes, eye_colours):
    message = ""
    for col, text in eye_colours.items():
        if col == eyes:
            message = text
            return message
    message = 'Your eye colour is not recognised :/.'
    return message

def check_hair(hair, hair_colours):
    message = ""
    for col, text in hair_colours.items():
        if col == hair:
            message = text
            return message
    message = 'Your hair colour is not recognised :/'
    return message


#print name value in sentence
print(f"Let's talk about {my_name}.")

#print age value in sentence and draw corresponding evaluation function
print(f"He is {my_age} years old.")
check_age(my_age)

#print height value in sentence and draw correspondingn evaluatuion function
print(f"He is {my_height} metres tall.")
check_height(my_height)

#print weight value in sentence and draw correspondingn evaluatuion function
print(f"He's {my_weight} kgs in weight.")
check_weight(my_weight)

print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print('Eyes: ', check_eyes(my_eyes, eye_colours))
print('Hair: ', check_hair(my_hair, hair_colours))

total = my_age + my_height + my_weight
print(f"If I add {my_age}, and {my_weight} I get {total}")
