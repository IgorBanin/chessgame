class Spot:
    piece = None
    x = None
    y = None

    #constructor
    def __init__(self, x, y, piece):
        self.setPiece(piece)
        self.setX(x)
        self.setY(y)

    def getPiece(self):
        return self.piece

    def setPiece(self, p):
        self.piece = p

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y



