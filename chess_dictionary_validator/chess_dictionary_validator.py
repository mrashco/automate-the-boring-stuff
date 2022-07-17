### 
#
# Chess Dict Validator
#
# https://automatetheboringstuff.com/chapter3/
#
###

def main(): 
    testBoard = {'1h': 'bking', '6c': 'wqueen', '2h': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    print(isValidChessBoard(testBoard), end='')

# 1 black/white king, total 16 pieces, 8 pawns, valid spaces 1a to 8h e.g. != 9z
# Names start with either 'w' or 'b'
def isValidChessBoard(t):
    for item in t:
        # Check key's 1st char is between 1-8
        if int(item[0]) not in [1,2,3,4,5,6,7,8]: return False
        # Check key's 2nd char is between a-h
        if item[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h']: return False
        # Checks value's 1st char of each pair is either 'w' or 'b'
        if t[item][0] not in ['w', 'b']: return False
        # Check value from 2nd char's is a valid piece
        if t[item][1:] not in ['king', 'queen', 'bishop', 'pawn', 'rook', 'knight']: return False
    return True

if __name__ == '__main__': main()