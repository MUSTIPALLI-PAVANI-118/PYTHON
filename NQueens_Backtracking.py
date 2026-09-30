#ROLL NO.:CH.AI.U4AID25028
# N-Queens Problem

def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens are placed successfully
    if row == n:
        return True

    # Try each column in the current row
    for col in range(n):

        # Check whether the position is safe
        if is_safe(board, row, col, n):

            # Place the queen
            board[row][col] = 'Q'

            # Move to the next row
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack and remove the queen
            board[row][col] = '.'

    return False


# Read the size of the chessboard
n = int(input("Enter the value of N: "))

# Create an empty chessboard
board = [['.' for _ in range(n)] for _ in range(n)]

# Display the result
if solve_n_queens(board, 0, n):

    print("\nN-Queens Solution:")

    for row in board:
        print(' '.join(row))

    print("\nSolution found successfully.")

else:
    print("\nNo solution exists.")