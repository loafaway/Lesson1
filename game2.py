import pygame

pygame.init()
surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Second Game!")
game_over = False

WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
AQUA = (0, 255, 255)

soundObj = pygame.mixer.Sound('diesel-horn.wav')

fontObj = pygame.font.Font('freesansbold.ttf', 24)
'''
fontObj.set_bold(True)
fontObj.set_italic(True)
fontObj.set_underline(True)
'''

FPS = 5
fpsClock = pygame.time.Clock()

catImg = pygame.image.load('padepokan-small.png')
catx, caty = 10, 10
W, H = catImg.get_width(), catImg.get_height()

text = fontObj.render(f'Width: {W}, Height: {H}', True, WHITE, BLUE)
textrect = text.get_rect()
textrect.center = (textrect.width//2, textrect.height//2)
X, Y = W, H+textrect.height

while not game_over:

    surface.fill(AQUA)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

    surface.blit(text, textrect)
    surface.blit(catImg, (X, Y))

    if X < 500-W and Y < 500-H:
        X += catx
        Y += caty
        if X < 0 or Y < 0:
            X, Y = W, H+textrect.height
            catx = -catx
            caty = -caty
    else:
        soundObj.play()
        pygame.time.wait(1000)
        soundObj.stop()

        catx = -catx
        caty = -caty
        X += catx
        Y += caty

    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)