import pygame
import sys

pygame.init()

game_state = "Menu"
player_turn = "Cross"

FIELD_SIZE = 50
line_width = 5

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
LIGHT_GREY = (52, 55, 58)
GREY = (43, 45, 48)
DARK_GREY = (23, 25, 28)

play_button_text = "Play"
play_button_rect = pygame.Rect(300, 250, 200, 100)

quit_button_text = "Quit"
quit_button_rect = pygame.Rect(300, 250, 200, 100)

reset_button_text = "Reset Game"
reset_button_rect = pygame.Rect(300, 250, 200, 100)

font = pygame.font.Font(None, 36)
text_surface = font.render('\'s turn', False, WHITE)
winner_text = font.render('is the winner', False, WHITE)
draw_text = font.render('Game is a draw', False, WHITE)

win_delay = 1000

field_rects = {}
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def start_menu():
    #  Play button
    play_button_surface = font.render(play_button_text, True, WHITE)
    play_text_rect = play_button_surface.get_rect()
    play_text_rect.center = play_button_rect.center
    pygame.draw.rect(window, DARK_GREY, play_button_rect)
    play_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)

    #  Quit button
    quit_button_surface = font.render(quit_button_text, True, WHITE)
    quit_text_rect = quit_button_surface.get_rect()
    quit_text_rect.center = quit_button_rect.center
    pygame.draw.rect(window, DARK_GREY, quit_button_rect)
    quit_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it changes to lighter shade
    # -100 is the offset from the button to window center
    if (WINDOW_WIDTH / 2 - play_button_rect.width / 2 <= mouse[0] <= WINDOW_WIDTH / 2 + play_button_rect.width / 2 and
            WINDOW_HEIGHT / 2 - play_button_rect.height / 2 - 100 <= mouse[
                1] <= WINDOW_HEIGHT / 2 + play_button_rect.height / 2 - 100):
        pygame.draw.rect(window, LIGHT_GREY, play_button_rect)
    else:
        pygame.draw.rect(window, DARK_GREY, play_button_rect)

    if (WINDOW_WIDTH / 2 - quit_button_rect.width / 2 <= mouse[
        0] <= WINDOW_WIDTH / 2 + quit_button_rect.width / 2 and
            WINDOW_HEIGHT / 2 - quit_button_rect.height / 2 + 100 <= mouse[
                1] <= WINDOW_HEIGHT / 2 + quit_button_rect.height / 2 + 100):
        pygame.draw.rect(window, LIGHT_GREY, quit_button_rect)
    else:
        pygame.draw.rect(window, DARK_GREY, quit_button_rect)

    window.blit(play_button_surface, play_text_rect)
    window.blit(quit_button_surface, quit_text_rect)


def start_game():
    global player_turn
    draw_field_rects()
    draw_game_field()

    #  Reset button
    reset_button_surface = font.render(reset_button_text, True, WHITE)
    reset_text_rect = reset_button_surface.get_rect()
    reset_text_rect.center = reset_button_rect.center
    pygame.draw.rect(window, DARK_GREY, reset_button_rect)
    reset_button_rect.center = (WINDOW_WIDTH // 2 + 150, WINDOW_HEIGHT // 2 - 50)

    mouse = pygame.mouse.get_pos()

    if (WINDOW_WIDTH / 2 + 150 - reset_button_rect.width / 2 <= mouse[0] <= WINDOW_WIDTH / 2 +
            reset_button_rect.width / 2 + 150 and
            WINDOW_HEIGHT / 2 - reset_button_rect.height / 2 - 50 <= mouse[
                1] <= WINDOW_HEIGHT / 2 + reset_button_rect.height / 2 - 50):
        pygame.draw.rect(window, LIGHT_GREY, reset_button_rect)
    else:
        pygame.draw.rect(window, DARK_GREY, reset_button_rect)

    window.blit(reset_button_surface, reset_text_rect)


def draw_game_field():
    pygame.draw.line(window, WHITE, (FIELD_SIZE * 2, FIELD_SIZE * 2),
                     (FIELD_SIZE * 2, FIELD_SIZE * 5 + 5), line_width)
    pygame.draw.line(window, WHITE, (FIELD_SIZE * 3 + 4, FIELD_SIZE * 2),
                     (FIELD_SIZE * 3 + 4, FIELD_SIZE * 5 + 5), line_width)
    pygame.draw.line(window, WHITE, (FIELD_SIZE, FIELD_SIZE * 3),
                     (FIELD_SIZE * 4 + 5, FIELD_SIZE * 3), line_width)
    pygame.draw.line(window, WHITE, (FIELD_SIZE, FIELD_SIZE * 4 + 4),
                     (FIELD_SIZE * 4 + 5, FIELD_SIZE * 4 + 4), line_width)
    window.blit(text_surface, (WINDOW_WIDTH / 2, 15))


def draw_field_rects():
    x = 50
    y = 100
    offset_x = 3
    offset_y = 3
    for field_number in range(1, 10):
        field_rects["field_{0}_rect".format(str(field_number))] = pygame.Rect(x, y, FIELD_SIZE - 2, FIELD_SIZE - 2)
        pygame.draw.rect(window, GREY, field_rects["field_{0}_rect".format(str(field_number))])
        x += 50 + offset_x
        offset_x += 2
        if x >= 200:
            x = 50
            offset_x = 3
            y += 50 + offset_y
            offset_y += 2


def update_symbols():
    global player_turn
    mouse_symbol_position = pygame.mouse.get_pos()
    if 50 < mouse_symbol_position[0] < 200 and 100 < mouse_symbol_position[1] < 250:
        column = mouse_symbol_position[0] // FIELD_SIZE - 1
        row = mouse_symbol_position[1] // FIELD_SIZE - 2
        if event.type == pygame.MOUSEBUTTONDOWN and board[row][column] == 0:
            if player_turn == "Circle":
                player_turn = change_player(player_turn)
                board[row][column] = 2
            elif player_turn == "Cross":
                player_turn = change_player(player_turn)
                board[row][column] = 1


def update_field():
    offset_x = 3
    offset_y = 3
    mouse_hover_position = pygame.mouse.get_pos()
    for column in range(0, 3):
        for row in range(0, 3):
            if board[column][row] == 1:
                pygame.draw.line(window, WHITE, (FIELD_SIZE * row + 54 + (offset_x * row),
                                                 FIELD_SIZE * column + 103 + (offset_y * column)),
                                 (FIELD_SIZE * row + 94 + (offset_x * row),
                                  FIELD_SIZE * column + 143 + (offset_y * column)), 7)
                pygame.draw.line(window, WHITE, (FIELD_SIZE * row + 94 + (offset_x * row),
                                                 FIELD_SIZE * column + 103 + (offset_y * column)),
                                 (FIELD_SIZE * row + 54 + (offset_x * row),
                                  FIELD_SIZE * column + 143 + (offset_y * column)), 7)
            elif board[column][row] == 2:
                pygame.draw.circle(window, WHITE, (FIELD_SIZE * row + 75 + (offset_x * row),
                                                   FIELD_SIZE * column + 125 + (offset_y * column)), 20, 5)
            elif ((FIELD_SIZE * row + 54 + (offset_x * row)) <= mouse_hover_position[0] <= (FIELD_SIZE * row + 54 +
                                                                                            (offset_x * row)) +
                  FIELD_SIZE and (FIELD_SIZE * column + 103 + (offset_y * column)) <= mouse_hover_position[1] <=
                  (FIELD_SIZE * column + 103 + (offset_y * column)) + FIELD_SIZE):
                highlight_button = pygame.Rect(FIELD_SIZE * row + 50 + (offset_x * row) + row, FIELD_SIZE * column +
                                               100 + (offset_y * column) + column, FIELD_SIZE - 2, FIELD_SIZE - 2)
                pygame.draw.rect(window, LIGHT_GREY, highlight_button)


def change_player(state):
    if state == "Circle":
        return "Cross"
    else:
        return "Circle"


def reset_game():
    pygame.display.flip()
    pygame.time.delay(win_delay)

    for i in range(3):
        for j in range(3):
            board[i][j] = 0


def check_for_winner(draw=False):
    #  Check Rows
    cross_won = False
    circle_won = False

    for row in board:
        if all(cell == row[0] for cell in row) and row[0] == 1:
            cross_won = True
        elif all(cell == row[0] for cell in row) and row[0] == 2:
            circle_won = True

    #  Check columns
    for col in range(3):
        if all(row[col] == board[0][col] for row in board) and board[0][col] == 1:
            cross_won = True
        elif all(row[col] == board[0][col] for row in board) and board[0][col] == 2:
            circle_won = True

    #  Check diagonals
    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] == 1:
        cross_won = True
    elif all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] == 1:
        cross_won = True
    elif all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] == 2:
        circle_won = True
    elif all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] == 2:
        circle_won = True

    if not draw:
        draw = True
        for row in board:
            for element in row:
                if element == 0:
                    draw = False
                    break
            if not draw:
                break

    if cross_won:
        window.blit(winner_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        pygame.draw.line(window, WHITE, (250, WINDOW_HEIGHT / 4 - 10), (290, WINDOW_HEIGHT / 4 + 30), 7)
        pygame.draw.line(window, WHITE, (290, WINDOW_HEIGHT / 4 - 10), (250, WINDOW_HEIGHT / 4 + 30), 7)
        reset_game()
    elif circle_won:
        window.blit(winner_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        pygame.draw.circle(window, WHITE, (WINDOW_WIDTH / 2 - 30, WINDOW_HEIGHT / 4 + 10), 20, 5)
        reset_game()
    elif draw:
        window.blit(draw_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        reset_game()

    return False


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game_state = "Game"
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if reset_button_rect.collidepoint(event.pos) and game_state == "Game":
                check_for_winner(True)

    window.fill(GREY)

    if game_state == "Menu":
        start_menu()
    elif game_state == "Game":
        start_game()

        #  Player's turn
        if player_turn == "Cross":
            pygame.draw.line(window, WHITE, (250, 10), (290, 50), 7)
            pygame.draw.line(window, WHITE, (290, 10), (250, 50), 7)
        if player_turn == "Circle":
            pygame.draw.circle(window, WHITE, (WINDOW_WIDTH / 2 - 30, 30), 20, 5)

        update_symbols()
        update_field()
        check_for_winner()

    pygame.display.flip()
pygame.quit()
