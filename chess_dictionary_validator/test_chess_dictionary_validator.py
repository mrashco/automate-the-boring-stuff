from chess_dictionary_validator import isValidChessBoard

def test_isValidChessBoard_default():
    assert isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2h': 'bbishop', '5h': 'bqueen', '3e': 'wking'}) == True
    assert isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2h': 'bbishop', '5g': 'bqueen', '3e': 'wking'}) == False
