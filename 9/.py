

def printBoard (board): 
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            print ("I", end = "")
            print (board[i][j], end = "i")
        print ()
    printBoard(board)         