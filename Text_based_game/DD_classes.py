class Player(object):
    """
    1 object per game. Created at start of script.
    """
    #list of all possible command keywords (prefix to a command subject) that can be entered by the user
    cmd_keywords = ["go", "inspect", "grab", "inventory", "inv", "quit_game"]

    def __init__(self):
        #will be assigned intially in startup functions. Always references Room.room_names[index]
        current_room = ""
        propertiesDict = {}
        try:
            mid_name = str(input("Please enter the middle name for Dullard Dave"))
        except ValueError:
            print("These values are not recognised as string.")
        #concatenate the 2 preset strings and input by user
        self.name = "Dullard " + mid_name + "Dave"

    def __str__(self):
        """
        Print description of player's character to screen
        """
        print(f"Player {self.name} looks on in a fashion which suggests only mild consciousness. Flies circle above him.")

    def eventMethod(self, command):
        pass


class Room(object):
    """
    Object blueprint specifying each room environment in the game
    """
    room_names = ()

    def __init__(self):
        """
        Intialise an instance of Room.
        Contents may need to be generated dynamically
        """
        contents = []
    pass

class RoomP(RoomB):
    """
    Object blueprint for an altered room design (child to Room)

    Will overwrite some attributes and properties of the original Item instance
    """
    def __init__(self):

    pass

class Item(object):
    """
    Object blueprint defining each in-game object
    """
    def __init__():
        propertiesDict = {}
    pass

class ItemP(ItemB):
    """
    Object blueprint defining altered in-game objects (child to Item)

    Will overwrite some basic attributes and properties of the original Item instance
    """
    pass

def cmdInterpret():
    #saved complex string to save typing
    cmd_format = "[recognised_keyword] [recognised_item | recognised_room_name]""
    command = str(input("Please enter a command ->"))
    valid = False
    while valid == False:
        try:
            word_list = command.split()
        except AttributeError:
            print(f"Your command seems to be in an incorrect data format, please try: {cmd_format}}")
        except ValueError:
            print("Incorrect command, please ensure you separate the command keyword and subject with a a single space:\n {cmd_format}")

    if len(word_list) != 2:
         print(f"The required format for data entry is -> \" \n Please try again")
         #skip back to start of while loop
         continue

    elif word_list[0] in Player.cmd_keywords | word_list[1] in <subject_list>:
