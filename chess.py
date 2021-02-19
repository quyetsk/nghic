Chess = {'xe': '!', 'ma': '@', 'tinh': '#', 'hau': '$', 'vua': '%',
         'tinh': '#', 'ma': '@', 'xe': '!',
         'tot': '*', 'tot': '*', 'tot': '*', 'tot': '*', 'tot': '*', 'tot': '*', 'tot': '*', 'tot': '*', }


def isValidChessBoard(chessboard):
    print(chessboard['xe'], '|', chessboard['ma'], '|', chessboard['tinh'], '|', chessboard['hau'], '|',
          chessboard['vua'], '|',
          chessboard['tinh'], '|', chessboard['ma'], '|', chessboard['xe'])
    print('-----------------------------')
    print(chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|',
          chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'])
    print('--+---+---+---+---+---+---+--')
    print('--+---+---+---+---+---+---+--')
    print('--+---+---+---+---+---+---+--')
    print('--+---+---+---+---+---+---+--')
    print('--+---+---+---+---+---+---+--')
    print('--+---+---+---+---+---+---+--')
    print(chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|',
          chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'], '|', chessboard['tot'])

    print(chessboard['xe'], '|', chessboard['ma'], '|', chessboard['tinh'], '|', chessboard['hau'], '|',
          chessboard['vua'], '|',
          chessboard['tinh'], '|', chessboard['ma'], '|', chessboard['xe'])


isValidChessBoard(Chess)