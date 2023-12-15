import pygame
import sys

pygame.init()

game_state = "Menu"
player_turn = "Circle"

FIELD_SIZE = 48

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
LIGHT_GREY = (52, 55, 58)
GREY = (43, 45, 48)
DARK_GREY = (23, 25, 28)

button_text = "Play"
button_rect = pygame.Rect(300, 250, 200, 100)

quit_button_text = "Quit"
quit_button_rect = pygame.Rect(300, 250, 200, 100)

reset_button_text = "Reset Game"
reset_button_rect = pygame.Rect(300, 250, 200, 100)

font = pygame.font.Font(None, 36)
text_surface = font.render('\'s turn', False, WHITE)
winner_text = font.render('is the winner', False, WHITE)
draw_text = font.render('Game is a draw', False, WHITE)

win_delay = 1000
turn_counter = 0

field_index = {}
board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
for key in range(1, 10):
    field_index["show_circle_{0}".format(str(key))] = False
    field_index["show_cross_{0}".format(str(key))] = False


def change_player(state):
    if state == "Circle":
        return "Cross"
    else:
        return "Circle"


def reset_game():
    pygame.display.flip()
    pygame.time.delay(win_delay)

    for key_reset in field_index:
        field_index[key_reset] = False
        field_index[key_reset] = False

    for i in range(3):
        for j in range(3):
            board[i][j] = 0

    global turn_counter
    turn_counter = 0


def check_for_winner():
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

    if cross_won:
        window.blit(winner_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        pygame.draw.line(window, WHITE, (250, WINDOW_HEIGHT / 4 - 10), (290, WINDOW_HEIGHT / 4 + 30), 7)
        pygame.draw.line(window, WHITE, (290, WINDOW_HEIGHT / 4 - 10), (250, WINDOW_HEIGHT / 4 + 30), 7)
        reset_game()
    if circle_won:
        window.blit(winner_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        pygame.draw.circle(window, WHITE, (WINDOW_WIDTH / 2 - 30, WINDOW_HEIGHT / 4 + 10), 20, 5)
        reset_game()
    if turn_counter == 9:
        window.blit(draw_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
        reset_game()

    return False


def start_game():
    global player_turn
    global turn_counter
    pygame.draw.line(window, WHITE, (100, 100), (100, 250), 5)
    pygame.draw.line(window, WHITE, (150, 100), (150, 250), 5)
    pygame.draw.line(window, WHITE, (50, 150), (200, 150), 5)
    pygame.draw.line(window, WHITE, (50, 200), (200, 200), 5)
    window.blit(text_surface, (WINDOW_WIDTH/2, 15))

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

    #  Field 1
    field_1_rect = pygame.Rect(50, 100, 48, 48)
    pygame.draw.rect(window, GREY, field_1_rect)
    if not field_index["show_circle_1"] and not field_index["show_cross_1"]:
        if 50 <= mouse[0] <= 50 + FIELD_SIZE and 100 <= mouse[1] <= 100 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_1_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_1_rect.collidepoint(event.pos) and board[0][0] == 0:
            if player_turn == "Circle":
                field_index["show_circle_1"] = True
                player_turn = change_player(player_turn)
                board[0][0] = 2
            elif player_turn == "Cross":
                field_index["show_cross_1"] = True
                player_turn = change_player(player_turn)
                board[0][0] = 1
            turn_counter += 1


    #  Field 2
    field_2_rect = pygame.Rect(103, 100, 45, 48)
    pygame.draw.rect(window, GREY, field_2_rect)
    if not field_index["show_circle_2"] and not field_index["show_cross_2"]:
        if 103 <= mouse[0] <= 103 + 45 and 100 <= mouse[1] <= 100 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_2_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_2_rect.collidepoint(event.pos) and board[0][1] == 0:
            if player_turn == "Circle":
                field_index["show_circle_2"] = True
                player_turn = change_player(player_turn)
                board[0][1] = 2
            elif player_turn == "Cross":
                field_index["show_cross_2"] = True
                player_turn = change_player(player_turn)
                board[0][1] = 1
            turn_counter += 1

    #  Field 3
    field_3_rect = pygame.Rect(154, 100, 47, 48)
    pygame.draw.rect(window, GREY, field_3_rect)
    if not field_index["show_circle_3"] and not field_index["show_cross_3"]:
        if 154 <= mouse[0] <= 154 + 45 and 100 <= mouse[1] <= 100 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_3_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_3_rect.collidepoint(event.pos) and board[0][2] == 0:
            if player_turn == "Circle":
                field_index["show_circle_3"] = True
                player_turn = change_player(player_turn)
                board[0][2] = 2
            elif player_turn == "Cross":
                field_index["show_cross_3"] = True
                player_turn = change_player(player_turn)
                board[0][2] = 1
            turn_counter += 1

    #  Field 4
    field_4_rect = pygame.Rect(50, 153, 48, 45)
    pygame.draw.rect(window, GREY, field_4_rect)
    if not field_index["show_circle_4"] and not field_index["show_cross_4"]:
        if 50 <= mouse[0] <= 50 + 45 and 150 <= mouse[1] <= 150 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_4_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_4_rect.collidepoint(event.pos) and board[1][0] == 0:
            if player_turn == "Circle":
                field_index["show_circle_4"] = True
                player_turn = change_player(player_turn)
                board[1][0] = 2
            elif player_turn == "Cross":
                field_index["show_cross_4"] = True
                player_turn = change_player(player_turn)
                board[1][0] = 1
            turn_counter += 1

    #  Field 5
    field_5_rect = pygame.Rect(103, 153, 45, 45)
    pygame.draw.rect(window, GREY, field_5_rect)
    if not field_index["show_circle_5"] and not field_index["show_cross_5"]:
        if 103 <= mouse[0] <= 103 + 45 and 150 <= mouse[1] <= 150 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_5_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_5_rect.collidepoint(event.pos) and board[1][1] == 0:
            if player_turn == "Circle":
                field_index["show_circle_5"] = True
                player_turn = change_player(player_turn)
                board[1][1] = 2
            elif player_turn == "Cross":
                field_index["show_cross_5"] = True
                player_turn = change_player(player_turn)
                board[1][1] = 1
            turn_counter += 1

    #  Field 6
    field_6_rect = pygame.Rect(154, 153, 47, 45)
    pygame.draw.rect(window, GREY, field_6_rect)
    if not field_index["show_circle_6"] and not field_index["show_cross_6"]:
        if 154 <= mouse[0] <= 154 + 45 and 150 <= mouse[1] <= 150 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_6_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_6_rect.collidepoint(event.pos) and board[1][2] == 0:
            if player_turn == "Circle":
                field_index["show_circle_6"] = True
                player_turn = change_player(player_turn)
                board[1][2] = 2
            elif player_turn == "Cross":
                field_index["show_cross_6"] = True
                player_turn = change_player(player_turn)
                board[1][2] = 1
            turn_counter += 1

    #  Field 7
    field_7_rect = pygame.Rect(50, 203, 47, 48)
    pygame.draw.rect(window, GREY, field_7_rect)
    if not field_index["show_circle_7"] and not field_index["show_cross_7"]:
        if 50 <= mouse[0] <= 50 + 45 and 200 <= mouse[1] <= 200 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_7_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_7_rect.collidepoint(event.pos) and board[2][0] == 0:
            if player_turn == "Circle":
                field_index["show_circle_7"] = True
                player_turn = change_player(player_turn)
                board[2][0] = 2
            elif player_turn == "Cross":
                field_index["show_cross_7"] = True
                player_turn = change_player(player_turn)
                board[2][0] = 1
            turn_counter += 1

    #  Field 8
    field_8_rect = pygame.Rect(103, 203, 45, 48)
    pygame.draw.rect(window, GREY, field_8_rect)
    if not field_index["show_circle_8"] and not field_index["show_cross_8"]:
        if 100 <= mouse[0] <= 100 + 45 and 200 <= mouse[1] <= 200 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_8_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_8_rect.collidepoint(event.pos) and board[2][1] == 0:
            if player_turn == "Circle":
                field_index["show_circle_8"] = True
                player_turn = change_player(player_turn)
                board[2][1] = 2
            elif player_turn == "Cross":
                field_index["show_cross_8"] = True
                player_turn = change_player(player_turn)
                board[2][1] = 1
            turn_counter += 1

    #  Field 9
    field_9_rect = pygame.Rect(154, 203, 47, 48)
    pygame.draw.rect(window, GREY, field_9_rect)
    if not field_index["show_circle_9"] and not field_index["show_cross_9"]:
        if 150 <= mouse[0] <= 150 + 45 and 200 <= mouse[1] <= 200 + FIELD_SIZE:
            pygame.draw.rect(window, LIGHT_GREY, field_9_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_9_rect.collidepoint(event.pos) and board[2][2] == 0:
            if player_turn == "Circle":
                field_index["show_circle_9"] = True
                player_turn = change_player(player_turn)
                board[2][2] = 2
            elif player_turn == "Cross":
                field_index["show_cross_9"] = True
                player_turn = change_player(player_turn)
                board[2][2] = 1
            turn_counter += 1

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game_state = "Game"
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if reset_button_rect.collidepoint(event.pos):
                turn_counter = 9

    window.fill(GREY)

    if game_state == "Menu":

        button_surface = font.render(button_text, True, WHITE)
        quit_button_surface = font.render(quit_button_text, True, WHITE)

        text_rect = button_surface.get_rect()
        text_rect.center = button_rect.center

        quit_text_rect = quit_button_surface.get_rect()
        quit_text_rect.center = quit_button_rect.center

        window.fill(GREY)
        pygame.draw.rect(window, DARK_GREY, button_rect)
        pygame.draw.rect(window, DARK_GREY, quit_button_rect)

        button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)
        quit_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        # -100 is the offset from the button to window center
        if (WINDOW_WIDTH/2-button_rect.width/2 <= mouse[0] <= WINDOW_WIDTH/2+button_rect.width/2 and
                WINDOW_HEIGHT/2-button_rect.height/2-100 <= mouse[1] <= WINDOW_HEIGHT/2+button_rect.height/2-100):
            pygame.draw.rect(window, LIGHT_GREY, button_rect)
        else:
            pygame.draw.rect(window, DARK_GREY, button_rect)

        if (WINDOW_WIDTH/2-quit_button_rect.width/2 <= mouse[0] <= WINDOW_WIDTH/2+quit_button_rect.width/2 and
                WINDOW_HEIGHT/2-quit_button_rect.height/2+100 <= mouse[1] <= WINDOW_HEIGHT/2+quit_button_rect.height/2+100):
            pygame.draw.rect(window, LIGHT_GREY, quit_button_rect)
        else:
            pygame.draw.rect(window, DARK_GREY, quit_button_rect)

        window.blit(button_surface, text_rect)
        window.blit(quit_button_surface, quit_text_rect)

    elif game_state == "Game":
        start_game()

        #  Player's turn
        if player_turn == "Cross":
            pygame.draw.line(window, WHITE, (250, 10), (290, 50), 7)
            pygame.draw.line(window, WHITE, (290, 10), (250, 50), 7)
        if player_turn == "Circle":
            pygame.draw.circle(window, WHITE, (WINDOW_WIDTH / 2 - 30, 30), 20, 5)

        #  Circles
        if field_index["show_circle_1"] and not field_index["show_cross_1"]:
            pygame.draw.circle(window, WHITE, (75, 125), 20, 5)
        if field_index["show_circle_2"] and not field_index["show_cross_2"]:
            pygame.draw.circle(window, WHITE, (125, 125), 20, 5)
        if field_index["show_circle_3"] and not field_index["show_cross_3"]:
            pygame.draw.circle(window, WHITE, (177, 125), 20, 5)
        if field_index["show_circle_4"] and not field_index["show_cross_4"]:
            pygame.draw.circle(window, WHITE, (75, 175), 20, 5)
        if field_index["show_circle_5"] and not field_index["show_cross_5"]:
            pygame.draw.circle(window, WHITE, (126, 175), 20, 5)
        if field_index["show_circle_6"] and not field_index["show_cross_6"]:
            pygame.draw.circle(window, WHITE, (177, 175), 20, 5)
        if field_index["show_circle_7"] and not field_index["show_cross_7"]:
            pygame.draw.circle(window, WHITE, (75, 225), 20, 5)
        if field_index["show_circle_8"] and not field_index["show_cross_8"]:
            pygame.draw.circle(window, WHITE, (125, 225), 20, 5)
        if field_index["show_circle_9"] and not field_index["show_cross_9"]:
            pygame.draw.circle(window, WHITE, (177, 225), 20, 5)

        #  Crosses
        if field_index["show_cross_1"] and not field_index["show_circle_1"]:
            pygame.draw.line(window, WHITE, (54, 103), (94, 143), 7)
            pygame.draw.line(window, WHITE, (94, 103), (54, 143), 7)
        if field_index["show_cross_2"] and not field_index["show_circle_2"]:
            pygame.draw.line(window, WHITE, (105, 103), (145, 143), 7)
            pygame.draw.line(window, WHITE, (145, 103), (105, 143), 7)
        if field_index["show_cross_3"] and not field_index["show_circle_3"]:
            pygame.draw.line(window, WHITE, (156, 103), (196, 143), 7)
            pygame.draw.line(window, WHITE, (196, 103), (156, 143), 7)
        if field_index["show_cross_4"] and not field_index["show_circle_4"]:
            pygame.draw.line(window, WHITE, (54, 155), (94, 195), 7)
            pygame.draw.line(window, WHITE, (94, 155), (54, 195), 7)
        if field_index["show_cross_5"] and not field_index["show_circle_5"]:
            pygame.draw.line(window, WHITE, (105, 155), (145, 195), 7)
            pygame.draw.line(window, WHITE, (145, 155), (105, 195), 7)
        if field_index["show_cross_6"] and not field_index["show_circle_6"]:
            pygame.draw.line(window, WHITE, (156, 155), (196, 195), 7)
            pygame.draw.line(window, WHITE, (195, 155), (156, 195), 7)
        if field_index["show_cross_7"] and not field_index["show_circle_7"]:
            pygame.draw.line(window, WHITE, (54, 208), (94, 248), 7)
            pygame.draw.line(window, WHITE, (94, 208), (54, 248), 7)
        if field_index["show_cross_8"] and not field_index["show_circle_8"]:
            pygame.draw.line(window, WHITE, (105, 208), (145, 248), 7)
            pygame.draw.line(window, WHITE, (145, 208), (105, 248), 7)
        if field_index["show_cross_9"] and not field_index["show_circle_9"]:
            pygame.draw.line(window, WHITE, (156, 208), (196, 248), 7)
            pygame.draw.line(window, WHITE, (195, 208), (156, 248), 7)

        check_for_winner()

    pygame.display.flip()

pygame.quit()
