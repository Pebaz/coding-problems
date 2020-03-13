"""
Create a function has_won() to see if a player has won a game of Tic-Tac-Toe.
"""

def has_won(player, board):
    """
    Time: O(N * 7) / O(N)
    Space: O(1)
    """
    n = len(board)
    return any((
        all(p == player for p in board[0]),
        all(p == player for p in board[-1]),
        all(p == player for p in [board[i][0] for i in range(n)]),
        all(p == player for p in [board[i][n // 2] for i in range(n)]),
        all(p == player for p in [board[i][n - 1] for i in range(n)]),
        all(p == player for p in [board[i][i] for i in range(n)]),
        all(p == player for p in [board[i][n - 1 - i] for i in range(n)])
    ))


if __name__ == '__main__':
    print(has_won(1, [
        [1, 1, 1],
        [0, 2, 0],
        [0, 2, 0]
    ]))

    print(has_won(2, [
        [1, 1, 1],
        [0, 2, 0],
        [0, 2, 0]
    ]))

    print(has_won(1, [
        [1, 1, 0],
        [0, 1, 0],
        [0, 2, 1]
    ]))

    print(has_won(1, [
        [2, 1, 1],
        [0, 1, 0],
        [1, 2, 2]
    ]))

    print(has_won(2, [
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0]
    ]))

    print(has_won(1, [
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0]
    ]))

    print(has_won(1, [
        [1, 0, 1, 0, 0],
        [2, 0, 1, 0, 0],
        [2, 0, 1, 0, 0],
        [2, 0, 1, 0, 0],
        [2, 0, 1, 0, 0]
    ]))
