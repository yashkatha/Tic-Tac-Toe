import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (0, 0, 255)
O_COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

# Board setup
board = [[None] * 3 for _ in range(3)]
CELL_SIZE = WIDTH // 3
current_player = "X"
game_over = False

# Draw the grid lines
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), 3)
        pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), 3)

# Draw X and O
def draw_xo():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20), 5)
                pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + 20, row * CELL_SIZE + CELL_SIZE - 20),
                                 (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + 20), 5)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, O_COLOR, 
                                   (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 
                                   CELL_SIZE // 2 - 20, 5)

# Check for a win
def check_winner():
    global game_over
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != None:
            game_over = True
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            game_over = True
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != None:
        game_over = True
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        game_over = True
        return board[0][2]
    if all(all(cell != None for cell in row) for row in board):
        game_over = True
        return "Tie"
    return None

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!" if winner != "Tie" else "It's a tie!")
                current_player = "O" if current_player == "X" else "X"
        
        screen.fill(BG_COLOR)
        draw_grid()
        draw_xo()
        pygame.display.update()
