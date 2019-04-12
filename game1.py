import pygame

pygame.init()
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game!")
game_over = False

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
AQUA = (0, 255, 255)

fontObj = pygame.font.SysFont('arial', 64)
#'''
fontObj.set_bold(True)
fontObj.set_italic(True)
fontObj.set_underline(True)
#'''

# smooth edge with anti-alias
# textObj = fontObj.render('ABCDEFGHabcdefgh', True, WHITE, BLUE)
# jagged edge without anti-alias

textObj = fontObj.render('ABCDEFGHabcdefgh', False, WHITE, BLUE)
textRectObj = textObj.get_rect()
textRectObj.center = (textRectObj.width//2, textRectObj.height//2)

while not game_over:

    surface.fill(AQUA)
    surface.blit(textObj, textRectObj)

    text = fontObj.render('L'+str(textRectObj.height)+'R', True, GREEN, WHITE)
    textrect = text.get_rect()
    textrect.center = (300+textrect.width//2, 300+textrect.height//2)
    surface.blit(text, textrect)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

    pygame.display.flip()
    pygame.display.update()