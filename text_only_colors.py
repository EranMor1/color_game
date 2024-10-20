import random

BOARD_SIZE = 18
COLORS = ['R', 'B', 'G', 'Y']
MAX_MOVES = 21


class game_board():
    def __init__(self):
        self.board = [[random.choice(COLORS) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.moves = 0

    def color_board(self, x, y, original_color, new_color):
        if self.board[0][0] == new_color:
            return

        if self.board[x][y] == original_color:
            if x < BOARD_SIZE - 1:
                self.color_board(x + 1, y, original_color, new_color)
            if y < BOARD_SIZE - 1:
                self.color_board(x, y + 1, original_color, new_color)
            self.board[x][y] = new_color


    def start_game(self):
        print("Game Started!")
        self.print_board()

        while self.moves < MAX_MOVES:

            if not self.choose_color():
                continue
            self.print_board()

            if self.check_board():
                print("Congratulations! You win the game!")
                return

        print("Game over! no more moves.")
        print("Final board:")
        self.print_board()

    def check_board(self):
        color = self.board[0][0]
        for row in range(BOARD_SIZE):
            if any(cell != color for cell in self.board[row]):
                return False
        return True

    def print_board(self):
        # Print the current board in a grid format
        for row in self.board:
            print(' '.join(row))
        print()

    def choose_color(self):
        print(f"Move {self.moves + 1}/{MAX_MOVES}")
        new_color = input("Choose a color R (Red), G (Green), B (Blue), Y (Yellow): ").upper()

        if new_color not in COLORS:
            print("Invalid color! Please choose R, G, B, or Y.")
            return False
        self.color_board(0, 0, self.board[0][0], new_color)
        self.moves += 1
        return True


if __name__ == '__main__':
    game = game_board()
    game.start_game()
