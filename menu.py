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

field_height = 48
field_width = 48

font = pygame.font.Font(None, 36)

global show_circle_1, show_cross_1
show_circle_1 = False
show_cross_1 = False

global show_circle_2, show_cross_2
show_circle_2 = False
show_cross_2 = False

global show_circle_3, show_cross_3
show_circle_3 = False
show_cross_3 = False

global show_circle_4, show_cross_4
show_circle_4 = False
show_cross_4 = False

global show_circle_5, show_cross_5
show_circle_5 = False
show_cross_5 = False

global show_circle_6, show_cross_6
show_circle_6 = False
show_cross_6 = False

global show_circle_7, show_cross_7
show_circle_7 = False
show_cross_7 = False

global show_circle_8, show_cross_8
show_circle_8 = False
show_cross_8 = False

global show_circle_9, show_cross_9
show_circle_9 = False
show_cross_9 = False


def start_game():
    pygame.draw.line(window, white, (100, 100), (100, 250), 5)
    pygame.draw.line(window, white, (150, 100), (150, 250), 5)
    pygame.draw.line(window, white, (50, 150), (200, 150), 5)
    pygame.draw.line(window, white, (50, 200), (200, 200), 5)

    mouse = pygame.mouse.get_pos()

    #  Field 1
    global show_circle_1, show_cross_1
    field_1_rect = pygame.Rect(50, 100, 48, 48)
    pygame.draw.rect(window, dark_grey, field_1_rect)
    if not show_circle_1 and not show_cross_1:
        if 50 <= mouse[0] <= 50 + field_width and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_1_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_1_rect.collidepoint(event.pos):
            show_circle_1 = True

    #  Field 2
    global show_circle_2, show_cross_2
    field_2_rect = pygame.Rect(103, 100, 45, 48)
    pygame.draw.rect(window, dark_grey, field_2_rect)
    if not show_circle_2 and not show_cross_2:
        if 103 <= mouse[0] <= 103 + 45 and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_2_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_2_rect.collidepoint(event.pos):
            show_circle_2 = True

    #  Field 3
    global show_circle_3, show_cross_3
    field_3_rect = pygame.Rect(154, 100, 47, 48)
    pygame.draw.rect(window, dark_grey, field_3_rect)
    if not show_circle_3 and not show_cross_3:
        if 154 <= mouse[0] <= 154 + 45 and 100 <= mouse[1] <= 100 + field_height:
            pygame.draw.rect(window, light_grey, field_3_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_3_rect.collidepoint(event.pos):
            show_circle_3 = True

    #  Field 4
    global show_circle_4, show_cross_4
    field_4_rect = pygame.Rect(50, 153, 48, 45)
    pygame.draw.rect(window, dark_grey, field_4_rect)
    if not show_circle_4 and not show_cross_4:
        if 50 <= mouse[0] <= 50 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_4_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_4_rect.collidepoint(event.pos):
            show_circle_4 = True

    #  Field 5
    global show_circle_5, show_cross_5
    field_5_rect = pygame.Rect(103, 153, 45, 45)
    pygame.draw.rect(window, dark_grey, field_5_rect)
    if not show_circle_5 and not show_cross_5:
        if 103 <= mouse[0] <= 103 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_5_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_5_rect.collidepoint(event.pos):
            show_circle_5 = True

    #  Field 6
    global show_circle_6, show_cross_6
    field_6_rect = pygame.Rect(154, 153, 47, 45)
    pygame.draw.rect(window, dark_grey, field_6_rect)
    if not show_circle_6 and not show_cross_6:
        if 154 <= mouse[0] <= 154 + 45 and 150 <= mouse[1] <= 150 + field_height:
            pygame.draw.rect(window, light_grey, field_6_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_6_rect.collidepoint(event.pos):
            show_circle_6 = True

    #  Field 7
    global show_circle_7, show_cross_7
    field_7_rect = pygame.Rect(50, 203, 47, 48)
    pygame.draw.rect(window, dark_grey, field_7_rect)
    if not show_circle_7 and not show_cross_7:
        if 50 <= mouse[0] <= 50 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_7_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_7_rect.collidepoint(event.pos):
            show_circle_7 = True

    #  Field 8
    global show_circle_8, show_cross_8
    field_8_rect = pygame.Rect(103, 203, 45, 48)
    pygame.draw.rect(window, dark_grey, field_8_rect)
    if not show_circle_8 and not show_cross_8:
        if 100 <= mouse[0] <= 100 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_8_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_8_rect.collidepoint(event.pos):
            show_circle_8 = True

    #  Field 9
    global show_circle_9, show_cross_9
    field_9_rect = pygame.Rect(154, 203, 47, 48)
    pygame.draw.rect(window, dark_grey, field_9_rect)
    if not show_circle_9 and not show_cross_9:
        if 150 <= mouse[0] <= 150 + 45 and 200 <= mouse[1] <= 200 + field_height:
            pygame.draw.rect(window, light_grey, field_9_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if field_9_rect.collidepoint(event.pos):
            show_circle_9 = True

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

        if show_circle_1:
            pygame.draw.circle(window, white, (75, 125), 20, 5)
        if show_circle_2:
            pygame.draw.circle(window, white, (125, 125), 20, 5)
        if show_circle_3:
            pygame.draw.circle(window, white, (177, 125), 20, 5)
        if show_circle_4:
            pygame.draw.circle(window, white, (75, 175), 20, 5)
        if show_circle_5:
            pygame.draw.circle(window, white, (126, 175), 20, 5)
        if show_circle_6:
            pygame.draw.circle(window, white, (177, 175), 20, 5)
        if show_circle_7:
            pygame.draw.circle(window, white, (75, 225), 20, 5)
        if show_circle_8:
            pygame.draw.circle(window, white, (125, 225), 20, 5)
        if show_circle_9:
            pygame.draw.circle(window, white, (177, 225), 20, 5)

    pygame.display.flip()

pygame.quit()
