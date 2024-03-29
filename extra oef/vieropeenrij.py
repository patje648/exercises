class Player:
    def __init__(self): 
        self.score=0
        self.name= input("please enter your name:")
        self.chip= input("choose your character:")
    # getter
    @property
    def score(self):
        return self.__score()
    
    # setter
    @score.setter
    def score(self,value):
        self.__score=value

    @property
    def name(self,name):
        return self.name
    
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def chip(self):
        return self.__chip
    
    @chip.setter
    def chip(self,symb):
        self.__chip = symb
    
class Board:
    def __init__(self):
        self.clear_board()

    def clear_board(self):
        self.__board=[["o"]*7]*6

    def add_piece(self):
        userinput="5"
        colidx = int(userinput)-1

        for row in range(len(self.__board)):
            ele = row[colidx]
            if ele=="O":
                continue
            else:
                self.__board[row-1][colidx] = Player.chip
