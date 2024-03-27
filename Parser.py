class Parser:
    """ 
    A class used to process text input from the user
    into a form that the game can understand
    """

    def get_command(self):
        """
        Asks the user to input a command into the terminal
            and process the command
       ` Returns a command object with first 2 words from the users
            input
        """

        word1 = None
        word2 = None

        user_input = str(input("> ")) #Input prompt

        wordList = user_input.split()
        pointer = 0

        if len(wordList) > 0 and wordList[pointer]:
            word1 = wordList[pointer] # Gets first word
            pointer += 1
            if len(wordList) > 1 and wordList[pointer]:
                word2 = wordList[pointer] # Gets second word
                #ignores the rest

        return Command(word1, word2)

class Command:
    """ 
    A class used to hold information about commands. Commands consist of a command word and
    at least one secondary word. 

    
    Example: "Go North" consists of the command word 'Go' and the secondary word 'North'
    """

    def __init__(self, firstWord: str, secondWord: str):
        """
        Assumes firstWord and secondWord are strings
        """
        
        self.__commandWord = firstWord
        self.__secondWord = secondWord
    
    
    def getCommand(self):
        """
        Returns the first word of the command
        """
        
        return self.__commandWord

    
    def getSecondWord(self):
        """
        Returns the second word of the command
        """
        
        return self.__secondWord

    
    def isUnknown(self):
        """
        Returns true if the command doesn't have a command word
        """

        return (self.__commandWord == None)

    def hasSecondWord(self):
        """
        Returns true if the command has a a second word
        """

        return (self.__secondWord != None)


if __name__ == "__main__":
    
    def get_command_test():
        parser = Parser()
        command = parser.get_command()

        print(command.getCommand())
        print(command.getSecondWord())
        print("Is command none ", command.isUnknown())
        print("Has second word ", command.hasSecondWord())

    get_command_test()


