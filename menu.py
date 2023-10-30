import pygame
import sys

pygame.init()

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
font = pygame.font.Font(None, 36)

"""
# Bild laden
image = pygame.image.load("dein_bild.jpg")  # Ersetze "dein_bild.jpg" durch den Dateinamen deines Bildes

# Bild auf die Fenstergröße skalieren
image = pygame.transform.scale(image, (window_width, window_height))
"""

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Prüfen, ob die Mausklickposition innerhalb des Buttons liegt
            if button_rect.collidepoint(event.pos):
                print(button_rect.height)

    window.fill(dark_grey)

    pygame.draw.rect(window, darker_grey, button_rect)

    button_surface = font.render(button_text, True, white)
    text_rect = button_surface.get_rect()
    text_rect.center = button_rect.center

    window.fill(dark_grey)
    pygame.draw.rect(window, darker_grey, button_rect)

    button_rect.center = (window_width // 2, window_height // 2 - 100)

    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it changes to lighter shade
    # -100 is the offset from the button to window center
    if (window_width/2-button_rect.width/2 <= mouse[0] <= window_width/2+button_rect.width/2 and
            window_height/2-button_rect.height/2-100 <= mouse[1] <= window_height/2+button_rect.height/2-100):
        pygame.draw.rect(window, light_grey, button_rect)

    else:
        pygame.draw.rect(window, darker_grey, button_rect)

    window.blit(button_surface, text_rect)

    pygame.display.flip()

pygame.quit()
