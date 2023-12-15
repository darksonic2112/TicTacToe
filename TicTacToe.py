import pygame
import sys

pygame.init()

game_state = "Menu"

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

white = (255, 255, 255)
dark_grey = (43, 45, 48)
darker_grey = (23, 25, 28)
light_grey = (52, 55, 58)

button_text = "Play"
button_rect = pygame.Rect(300, 250, 200, 100)

quit_button_text = "Quit"
quit_button_rect = pygame.Rect(300, 250, 200, 100)

reset_button_text = "Reset Game"
reset_button_rect = pygame.Rect(300, 250, 200, 100)

field_height = 48
field_width = 48

font = pygame.font.Font(None, 36)
text_surface = font.render('\'s turn', False, white)
winner_text = font.render('is the winner', False, white)
draw_text = font.render('Game is a draw', False, white)

win_delay = 1000
turn_counter = 0

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

field_index = {}

for key in range(1, 10):
    field_index["show_circle_{0}".format(str(key))] = False
    field_index["show_cross_{0}".format(str(key))] = False
print(field_index)


def change_player(state):
    if state == "Circle":
        return "Cross"
    else:
        return "Circle"


player_turn = "Circle"


def reset_game():
    pygame.display.flip()
    pygame.time.delay(win_delay)
    for key in range(1, 10):
        field_index["show_circle_{0}".format(str(key))] = False
        field_index["show_cross_{0}".format(str(key))] = False

    for i in range(3):
        for j in range(3):
            board[i][j] = 0

    global turn_counter
    turn_counter = 0

reset_game()

def check_for_winner():
    #  Check Rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] == 1:
            window.blit(winner_text, (window_width/2, window_height/4))
            pygame.draw.line(window, white, (250, window_height/4-10), (290, window_height/4+30), 7)
            pygame.draw.line(window, white, (290, window_height/4-10), (250, window_height/4+30), 7)
            reset_game()


        if all(cell == row[0] for cell in row) and row[0] == 2:
            window.blit(winner_text, (window_width / 2, window_height / 4))
            pygame.draw.circle(window, white, (window_width / 2 - 30, window_height / 4 + 10), 20, 5)
            reset_game()

    #  Check columns
    for col in range(3):
        if all(row[col] == board[0][col] for row in board) and board[0][col] == 1:
            window.blit(winner_text, (window_width / 2, window_height / 4))
            pygame.draw.line(window, white, (250, window_height / 4 - 10), (290, window_height / 4 + 30), 7)
            pygame.draw.line(window, white, (290, window_height / 4 - 10), (250, window_height / 4 + 30), 7)
            reset_game()

        if all(row[col] == board[0][col] for row in board) and board[0][col] == 2:
            window.blit(winner_text, (window_width / 2, window_height / 4))
            pygame.draw.circle(window, white, (window_width / 2 - 30, window_height / 4 + 10), 20, 5)
            reset_game()

    #  Check diagonals
    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] == 1:
        window.blit(winner_text, (window_width / 2, window_height / 4))
        pygame.draw.line(window, white, (250, window_height / 4 - 10), (290, window_height / 4 + 30), 7)
        pygame.draw.line(window, white, (290, window_height / 4 - 10), (250, window_height / 4 + 30), 7)
        reset_game()

    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] == 2:
        window.blit(winner_text, (window_width / 2, window_height / 4))
        pygame.draw.circle(window, white, (window_width / 2 - 30, window_height / 4 + 10), 20, 5)
        reset_game()

    if all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] == 1:
        window.blit(winner_text, (window_width / 2, window_height / 4))
        pygame.draw.line(window, white, (250, window_height / 4 - 10), (290, window_height / 4 + 30), 7)
        pygame.draw.line(window, white, (290, window_height / 4 - 10), (250, window_height / 4 + 30), 7)
        reset_game()

    if all(board[i][2 - i] == board[0][2] for i in range(3)) and board[0][2] == 2:
        window.blit(winner_text, (window_width / 2, window_height / 4))
        pygame.draw.circle(window, white, (window_width / 2 - 30, window_height / 4 + 10), 20, 5)
        reset_game()

    if turn_counter == 9:
        window.blit(draw_text, (window_width / 2, window_height / 4))
        reset_game()

    return False


def start_game():
    global player_turn
    global turn_counter
    pygame.draw.line(window, white, (100, 100), (100, 250), 5)
    pygame.draw.line(window, white, (150, 100), (150, 250), 5)
    pygame.draw.line(window, white, (50, 150), (200, 150), 5)
    pygame.draw.line(window, white, (50, 200), (200, 200), 5)
    window.blit(text_surface, (window_width/2, 15))

    reset_button_surface = font.render(reset_button_text, True, white)
    reset_text_rect = reset_button_surface.get_rect()
    reset_text_rect.center = reset_button_rect.center
    pygame.draw.rect(window, darker_grey, reset_button_rect)
    reset_button_rect.center = (window_width // 2 + 150, window_height // 2 - 50)

    mouse = pygame.mouse.get_pos()

    if (window_width / 2 + 150 - reset_button_rect.width / 2 <= mouse[0] <= window_width / 2 +
            reset_button_rect.width / 2 + 150 and
            window_height / 2 - reset_button_rect.height / 2 - 50 <= mouse[
                1] <= window_height / 2 + reset_button_rect.height / 2 - 50):
        pygame.draw.rect(window, light_grey, reset_button_rect)
    else:
        pygame.draw.rect(window, darker_grey, reset_button_rect)

    window.blit(reset_button_surface, reset_text_rect)

    #  Field 1
    field_1_rect = pygame.Rect(50, 100, 48, 48)
    pygame.draw.rect(window, dark_grey, field_1_rect)
    if not field_index["show_circle_1"] and not field_index["show_cross_1"]:
        if 50 <= mouse[0] <= 50 + field_width and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_1_rect)
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
    pygame.draw.rect(window, dark_grey, field_2_rect)
    if not field_index["show_circle_2"] and not field_index["show_cross_2"]:
        if 103 <= mouse[0] <= 103 + 45 and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_2_rect)
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
    pygame.draw.rect(window, dark_grey, field_3_rect)
    if not field_index["show_circle_3"] and not field_index["show_cross_3"]:
        if 154 <= mouse[0] <= 154 + 45 and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_3_rect)
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
    pygame.draw.rect(window, dark_grey, field_4_rect)
    if not field_index["show_circle_4"] and not field_index["show_cross_4"]:
        if 50 <= mouse[0] <= 50 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_4_rect)
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
    pygame.draw.rect(window, dark_grey, field_5_rect)
    if not field_index["show_circle_5"] and not field_index["show_cross_5"]:
        if 103 <= mouse[0] <= 103 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_5_rect)
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
    pygame.draw.rect(window, dark_grey, field_6_rect)
    if not field_index["show_circle_6"] and not field_index["show_cross_6"]:
        if 154 <= mouse[0] <= 154 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_6_rect)
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
    pygame.draw.rect(window, dark_grey, field_7_rect)
    if not field_index["show_circle_7"] and not field_index["show_cross_7"]:
        if 50 <= mouse[0] <= 50 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_7_rect)
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
    pygame.draw.rect(window, dark_grey, field_8_rect)
    if not field_index["show_circle_8"] and not field_index["show_cross_8"]:
        if 100 <= mouse[0] <= 100 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_8_rect)
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
    pygame.draw.rect(window, dark_grey, field_9_rect)
    if not field_index["show_circle_9"] and not field_index["show_cross_9"]:
        if 150 <= mouse[0] <= 150 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_9_rect)
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

    window.fill(dark_grey)

    if game_state == "Menu":

        button_surface = font.render(button_text, True, white)
        quit_button_surface = font.render(quit_button_text, True, white)

        text_rect = button_surface.get_rect()
        text_rect.center = button_rect.center

        quit_text_rect = quit_button_surface.get_rect()
        quit_text_rect.center = quit_button_rect.center

        window.fill(dark_grey)
        pygame.draw.rect(window, darker_grey, button_rect)
        pygame.draw.rect(window, darker_grey, quit_button_rect)

        button_rect.center = (window_width // 2, window_height // 2 - 100)
        quit_button_rect.center = (window_width // 2, window_height // 2 + 100)

        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        # -100 is the offset from the button to window center
        if (window_width/2-button_rect.width/2 <= mouse[0] <= window_width/2+button_rect.width/2 and
                window_height/2-button_rect.height/2-100 <= mouse[1] <= window_height/2+button_rect.height/2-100):
            pygame.draw.rect(window, light_grey, button_rect)
        else:
            pygame.draw.rect(window, darker_grey, button_rect)

        if (window_width/2-quit_button_rect.width/2 <= mouse[0] <= window_width/2+quit_button_rect.width/2 and
                window_height/2-quit_button_rect.height/2+100 <= mouse[1] <= window_height/2+quit_button_rect.height/2+100):
            pygame.draw.rect(window, light_grey, quit_button_rect)
        else:
            pygame.draw.rect(window, darker_grey, quit_button_rect)

        window.blit(button_surface, text_rect)
        window.blit(quit_button_surface, quit_text_rect)

    elif game_state == "Game":
        start_game()

        #  Player's turn
        if player_turn == "Cross":
            pygame.draw.line(window, white, (250, 10), (290, 50), 7)
            pygame.draw.line(window, white, (290, 10), (250, 50), 7)
        if player_turn == "Circle":
            pygame.draw.circle(window, white, (window_width / 2 - 30, 30), 20, 5)

        #  Circles
        if field_index["show_circle_1"] and not field_index["show_cross_1"]:
            pygame.draw.circle(window, white, (75, 125), 20, 5)
        if field_index["show_circle_2"] and not field_index["show_cross_2"]:
            pygame.draw.circle(window, white, (125, 125), 20, 5)
        if field_index["show_circle_3"] and not field_index["show_cross_3"]:
            pygame.draw.circle(window, white, (177, 125), 20, 5)
        if field_index["show_circle_4"] and not field_index["show_cross_4"]:
            pygame.draw.circle(window, white, (75, 175), 20, 5)
        if field_index["show_circle_5"] and not field_index["show_cross_5"]:
            pygame.draw.circle(window, white, (126, 175), 20, 5)
        if field_index["show_circle_6"] and not field_index["show_cross_6"]:
            pygame.draw.circle(window, white, (177, 175), 20, 5)
        if field_index["show_circle_7"] and not field_index["show_cross_7"]:
            pygame.draw.circle(window, white, (75, 225), 20, 5)
        if field_index["show_circle_8"] and not field_index["show_cross_8"]:
            pygame.draw.circle(window, white, (125, 225), 20, 5)
        if field_index["show_circle_9"] and not field_index["show_cross_9"]:
            pygame.draw.circle(window, white, (177, 225), 20, 5)

        #  Crosses
        if field_index["show_cross_1"] and not field_index["show_circle_1"]:
            pygame.draw.line(window, white, (54, 103), (94, 143), 7)
            pygame.draw.line(window, white, (94, 103), (54, 143), 7)
        if field_index["show_cross_2"] and not field_index["show_circle_2"]:
            pygame.draw.line(window, white, (105, 103), (145, 143), 7)
            pygame.draw.line(window, white, (145, 103), (105, 143), 7)
        if field_index["show_cross_3"] and not field_index["show_circle_3"]:
            pygame.draw.line(window, white, (156, 103), (196, 143), 7)
            pygame.draw.line(window, white, (196, 103), (156, 143), 7)
        if field_index["show_cross_4"] and not field_index["show_circle_4"]:
            pygame.draw.line(window, white, (54, 155), (94, 195), 7)
            pygame.draw.line(window, white, (94, 155), (54, 195), 7)
        if field_index["show_cross_5"] and not field_index["show_circle_5"]:
            pygame.draw.line(window, white, (105, 155), (145, 195), 7)
            pygame.draw.line(window, white, (145, 155), (105, 195), 7)
        if field_index["show_cross_6"] and not field_index["show_circle_6"]:
            pygame.draw.line(window, white, (156, 155), (196, 195), 7)
            pygame.draw.line(window, white, (195, 155), (156, 195), 7)
        if field_index["show_cross_7"] and not field_index["show_circle_7"]:
            pygame.draw.line(window, white, (54, 208), (94, 248), 7)
            pygame.draw.line(window, white, (94, 208), (54, 248), 7)
        if field_index["show_cross_8"] and not field_index["show_circle_8"]:
            pygame.draw.line(window, white, (105, 208), (145, 248), 7)
            pygame.draw.line(window, white, (145, 208), (105, 248), 7)
        if field_index["show_cross_9"] and not field_index["show_circle_9"]:
            pygame.draw.line(window, white, (156, 208), (196, 248), 7)
            pygame.draw.line(window, white, (195, 208), (156, 248), 7)

        check_for_winner()

    pygame.display.flip()

pygame.quit()
