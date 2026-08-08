# CODSOFT Task 2 - Tic-Tac-Toe AI
# Minimax Algorithm

HUMAN = "X"
AI = "O"


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Tie"

    return None


def minimax(board, is_maximizing):
    result = check_winner(board)

    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if result == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    best_score = float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = HUMAN
            score = minimax(board, True)
            board[i] = " "
            best_score = min(best_score, score)

    return best_score


def find_best_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    board = [" "] * 9

    print("=" * 45)
    print("          TIC-TAC-TOE AI")
    print("          CODSOFT - TASK 2")
    print("=" * 45)
    print("You are X. The AI is O.")
    print("Choose positions from 1 to 9.")
    print()

    while True:
        print_board(board)

        # Human move
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Please enter a number from 1 to 9.")
                elif board[position] != " ":
                    print("That position is already occupied.")
                else:
                    board[position] = HUMAN
                    break

            except ValueError:
                print("Please enter a valid number.")

        result = check_winner(board)

        if result:
            print_board(board)
            if result == HUMAN:
                print("You win!")
            else:
                print("It's a tie!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move] = AI

        print(f"AI chooses position {ai_move + 1}.")

        result = check_winner(board)

        if result:
            print_board(board)
            if result == AI:
                print("AI wins!")
            else:
                print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
