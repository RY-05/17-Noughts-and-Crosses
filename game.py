import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
FONT_SIZE = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("17-Tic-Tac-Toe")
screen.fill(WHITE)

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Check if a player has won
def check_win(player):
    target_sum = 17
    # Check rows
    for row in board:
        if sum(row) == target_sum:
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if sum(row[col] for row in board) == target_sum:
            return True
    # Check diagonals
    if board[0][0] + board[1][1] + board[2][2] == target_sum:
        return True
    if board[0][2] + board[1][1] + board[2][0] == target_sum:
        return True
    return False

# Check if the board is full
def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

# AI opponent's move
def ai_move():
    available_positions = [(i, j) for i in range(BOARD_ROWS) for j in range(BOARD_COLS) if board[i][j] == 0]
    return random.choice(available_positions)

# Draw the grid lines
def draw_lines():
    # Horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw the X and O symbols
def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != 0:
                x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                text = font.render(str(board[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)

# Main game loop
def main():
    player = 1
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if player == 1:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE
                    if board[row][col] == 0:
                        board[row][col] = 17 - sum(board[row])  # Ensure rows add up to 17
                        if check_win(player):
                            print("Player 1 wins!")
                            game_over = True
                        elif is_board_full():
                            print("It's a draw!")
                            game_over = True
                        player = 2
                else:
                    ai_row, ai_col = ai_move()
                    board[ai_row][ai_col] = 17 - sum(board[i][ai_col] for i in range(BOARD_ROWS))  # Ensure columns add up to 17
                    if check_win(player):
                        print("AI wins!")
                        game_over = True
                    elif is_board_full():
                        print("It's a draw!")
                        game_over = True
                    player = 1

        screen.fill(WHITE)
        draw_lines()
        draw_symbols()
        pygame.display.flip()

if __name__ == "__main__":
    main()
