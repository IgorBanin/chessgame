from abc import ABC, abstractmethod

class Piece(ABC):

    killed = False;
    white = False;

    #Initializes a piece
    def __init__(self, white):
        self.setWhite(white)

    def isWhite(self):
        return self.white == True

    #Defines the color of a piece
    def setWhite(self, white):
        self.white = white

    def isKilled(self):
        return self.killed == True;

    def setKilled(self, killed):
        self.killed = killed

    def canMove(self, board, start, end):
        pass

class Pawn(Piece):
    def Pawn(self, white):
        super(white)

    def canMove(self, board, start, end):
        if (end.getPiece().isWhite() == self.isWhite()):
            return False
        '''Need to include logic of pawns only being able to 
        move forward two spots on the first move, and one after that'''
        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        return x * y == 2

class Rook(Piece):
    def Rook(self, white):
        super(white)

    def canMove(self, board, start, end):
        if (end.getPiece().isWhite() == self.isWhite()):
            return False
        '''Need to include the logic rooks only moving in straight lines'''
        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        return x * y == 2

class Bishop(Piece):
    def Bishop(self, white):
        super(white)

    def canMove(self, board, start, end):
        if (end.getPiece().isWhite() == self.isWhite()):
            return False
        '''Need to include the logic of there being two bishops
        and how they can move in diagonals'''
        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        return x * y == 2

class Knight(Piece):
    def Knight(self, white):
        super(white)

    def canMove(self, board, start, end):
        if(end.getPiece().isWhite() == self.isWhite()):
            return False

        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        return x * y == 2

class King(Piece):
    castlingDone = False

    def King(self, white):
        super(white)

        return self.isCastlingDone() == True

    def setCastlingDone(self, castlingDone):
        self.castlingDone = castlingDone

    def canMove(self, board, start, end):
        #we can'tmove the piece to a spot that has a piece of the
        #same color
        if(end.getPiece().isWhite() == self.isWhite()):
            return False

        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        if((x+y) == 1):
            #check if this move will not result in the king
            #being attacked if so return true
            return True

        return self.isValidCastling(board, start, end)

    def isValidCastling(self, board, start, end):
        if(self.isCastlingDone()):
            return False
        #logic for returning true or false

    def isCastlingMove(self, start, end):
        #check if starting and ending positions are correct


class Queen(Piece):
    def Queen(self, white):
        super(white)

    def canMove(self, board, start, end):
        if (end.getPiece().isWhite() == self.isWhite()):
            return False
        '''Include logic of how the queen can move'''
        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())
        return x * y == 2







