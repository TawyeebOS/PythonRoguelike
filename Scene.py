import abc
from abc import ABC, abstractmethod
from collections import deque

class Scene(ABC):
    """
    Abstract scene class represents an specific environment 
    and contains its own valid set of commands
    """
    _VALID_COMMANDS = ("help", "quit")
    
    """ 
    help - displays to the player information about the current scene
        and provides a list of commands that can be used
    quit - quits the game

    """

    def __init__(self, name: str, description, str):
        """
        Name: Name of the Scene
        Description: What the scene represents

        Assumes name and descrition are Strings
        """

        self._name = name
        self._description = description

    def getSceneName(self):
        """Returns the name of the scene"""
        return self._name

    
    def quit(self, command: Command):
        """
        Checks to see if only "quit" was entered before quitting the game
        Returns a boolean True if only "quit" was typed and False otherwise
        """

        if command.hasSecondWord():
            print("Quit what")
            return False
        else:
            return True     # this signals that we want to quit the game
    
    def isCommand(self, word: str):
        """
        Assumes word is a string
        Returns True if word is a command word, false otherwise
        """

        for i in range(len(validCommands)):
            if (validCommands[i] == word):
                return True

        return False

    def showAll(self):
        """Prints all valid commands for this scene to standard output"""
        for command in validCommands:
            print(command + " ", end="\r")

        print()


    @abstractmethod
    def printHelp(self):
        """ Displays some useful information about the current scene"""
        pass


class OverworldScene(Scene):
    """
    A Class extending the Scene ABC. It defines the actions a player can take
    when moving across the map
    """
    
    __movementStack = deque() # stores the path to the starting room
    __VALID_COMMANDS = ("help", "quit", "go", "search", "back")
    
    """
    Scene specific commands

    go [direction] - moves the player in a particular direction
    search [object] - searches the specified object
    back - undos the previous movement command

    e.g:
    You are in the chamber of secrets
    > go north

    You are in the deathly hallows
    > search room
    
    You found a key!
    > back

    You are in the chamber of secrets
    """

    def __init__(self, currentRoom: Room):
        """
        currentRoom: The room the player is current occupying 
        Assumes currentRoom is a Room object.
        """
        super().__init__("Overworld", "Movement inside and between room")
        self.__currentRoom: Room = currentRoom 
        self.__tempInv: Item = None # temporary inventory for storing discovered items

    def goRoom(self, command: Command):
        """
        Assumes command is a Command
        Attempts to move to a room in the direction specified
            by the command, if unable throws an error
        Returns a Room object
        """
        
        # checks to see it there is a second word
        if (not (command.hasSecondWord())):
            print("Go Where")
            return currentRoom
        
        # if so, assign to the direction variable
        direction: str = command.getSecondWord()
        
        # attempt to leave the current room via specified direction
        nextRoom: Room = currentRoom.getExit(direction)

        # checks to see if an exit in that direction 
        if nextRoom == None:
            print("There is no door!")
        else:
            movementStack.append(Room.oppositeDirection(direction))
            currentRoom = nextRoom
            print(currentRoom.getDescription())

        return currentRoom
        
    def goBack(self):
            """
            Moves the player to the previous accessed room. If the player is 
                back at the start, this does nothing.
            Returns a Room object
            """
            if len(movementStack) == 0:
                print("You can't turn back here")
                return currentRoom

            direction: str = movementStack.pop()
            nextRoom: Room = cuurentRoom.getExit(direction)

            if nextRoom == None:
                print("There is no door!")
            else:
                currentRoom = nextRoom
                print(currentRoom.getDescription())

            return currentRoom

    def accessTempInv(self):
        """
        Returns the item in the temporary inventory
        """
        item = Item(tempInv)
        tempInv = None
        return item


    def printHelp(self):
        """
        Displays useful information about the current scene
        """
    
        print("Overworld")
        print("You can move between rooms and search for items")
        print("Let's hope you don't run into anything while searching")
        print("Your command words are:")
        self.showAll()


