from twoPlayerAiGame.stateGame import StateGame

class StateSG(StateGame):
    """
    Class wich represent a state of the game "Stick Game" from the french TV show "Fort Boyard"
    """    
    def __init__(self, maxPlayer, nbStick, nbMaxTook=3):
        """
        Create a state of the game.
        
        Important information for the game is the number of stick (at the beginning), 
        the first player and the max number that a player can take in one turn.
        
        :param nbStick: The number of stick at the beginning of the game
        :param maxPlayer: The player wich begin. True for the "MAX" player and False for "MIN" player
        :param nbMaxTook: The maximum number of sticks that a player can take in one turn
        
        :type nbStick: int
        :type maxPlayer: boolean
        :type maxPlayer: int
        
        :return: The state with the choosen information
        :rtype: StateSG
        """
        self.nbStick = nbStick
        self.maxPlayer = 1 if maxPlayer==True else -1
        self.nbMaxTook = nbMaxTook

        
    def calculateScore(self):
        """
        Calculate the score of the current state if it's a terminal state (then return 0)
        
        This function can be modify to estimate the score for a non terminal state.
        
        :return: The score of the current state
        :rtype: int
        """
        if(self.nbStick==0):
            return self.maxPlayer 
        return False #To indicate no one win for now. Can be replace by a function which estimate the score
    
    def getChoices(self):
        """
        Get the different choice for the player for the current state.
        
        :return: Every choices that the player can make. 
        :rtype: list[int]
        """
        nbMaxTurn = self.nbMaxTook if self.nbMaxTook<= self.nbStick else self.nbStick
        return [i for i in range(1, nbMaxTurn+1)]
        
    def doChoice(self, choice, inNewState = False):
        """
        Apply the choice to the current state (inplace or not)
        
        :param choice: The number of stick that the player want to take
        :param inNewState: To choose if the choice is apply inplace (on the current state) or not (on a copy of the current state)
        
        :type choice: int
        :type inNewState: boolean
        
        :return: Nothing if it's inplace then the new state.
        :rtype: StateSG or None
        """
        if(inNewState == False):
            self.nbStick -= choice
            self.maxPlayer *= -1
            return None
        else:
            return StateSG(self.nbStick-nb, -self.maxPlayer)
            
    def undoChoice(self, choice, inNewState = False):
        """
        Undo the given choice for the current state (inplace or not)
        
        :param choice: The number of stick that the player want to take
        :param inNewState: To choose if the choice is apply inplace (on the current state) or not (on a copy of the current state)
        
        :type choice: int
        :type inNewState: boolean
        
        :return: Nothing if it's inplace then the new state.
        :rtype: StateSG or None
        """
        return self.doChoice(-choice, inNewState)
    
    def toKey(self):
        """
        Get the unique ID of the state.
        
        This ID is useful to use memoization in different algorithms
        
        :return: the ID of the current state
        :rtype: string
        """
        return str(self.nbStick)+";"+str(self.maxPlayer)+";"+str(self.nbMaxTook)
    
    def printBeforeGame(self):
        """
        Print information before the beginning of the game
        """
        print("##############################\nThis is the game : Sticks Game\n##############################\n")
        boardStr = ""
        for i in range(self.nbStick):
            boardStr += "|"
        boardStr += " ("+str(self.nbStick)+" sticks)"
        print(boardStr)
    
    def printInfoPlayer(self):
        """
        Print information before the turn of the current player
        """
        currentPlayer = 1 if self.maxPlayer==1 else 2
        choices = self.getChoices()
        print("\n################")
        print("Turn of player",currentPlayer)
        print("\nChoose your choice in this list (enter le number of the choosen item) :")
        for i in range(len(choices)):
            print(i+1,") Take",choices[i],"sticks")
    
    def printResultAction(self, choice):
        """
        Print information after the turn of the current player
        
        :param choice: The choice wich was just played
            
        :type choice: int
        """
        print("\nThe player takes",choice,"sticks from the board")
        boardStr = ""
        for i in range(self.nbStick):
            boardStr += "|"
        boardStr += " ("+str(self.nbStick)+" sticks)"
        print(boardStr)
    
    def printAfterGame(self):
        """
        Print information after the end of the game
        """
        winner = 1 if self.calculateScore() else 2
        print("\n#####################")
        print("The winner is player", winner)