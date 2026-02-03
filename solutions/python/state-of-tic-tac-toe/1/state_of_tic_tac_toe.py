def gamestate(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    
    x_wins = has_won(board, 'X')
    o_wins = has_won(board, 'O')
    
    if x_wins and o_wins:
        raise ValueError('Impossible board: game should have ended after the game was won')
    
    if x_wins and x_count != o_count + 1:
        raise ValueError("Continued playing after win")
    
    if o_wins and x_count != o_count:
        raise ValueError("Continued playing after win")
    
    if x_wins or o_wins:
        return "win"
    
    if x_count + o_count == 9:
        return "draw"
    
    return "ongoing"


def has_won(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False
