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
                print("LoL.")

    window.fill(dark_grey)

    pygame.draw.rect(window, darker_grey, button_rect)

    button_surface = font.render(button_text, True, white)
    text_rect = button_surface.get_rect()
    text_rect.center = button_rect.center  # Die Position des Texts auf die Mitte des Rechtecks setzen

    window.fill(dark_grey)
    pygame.draw.rect(window, darker_grey, button_rect)

    button_rect.center = (window_width // 2, window_height // 2 - 100)
    window.blit(button_surface, text_rect)
    # Bild auf das Fenster zeichnen
    #window.blit(image, (0, 0))

    pygame.display.flip()

pygame.quit()
