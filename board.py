class Board:
    Spot[][] boxes:

    def __init__(self):

    def getBox(self, x, y):
        if(x < 0 or x > 7 or y < 0 or y > 7):
            raise ValueError('Values not permissable')
