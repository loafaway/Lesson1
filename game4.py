import pygame
import pygame.freetype

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Fourth Game!")
game_over = False

FPS = 5
fpsClock = pygame.time.Clock()

AQUA = (0, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)

fontObj1 = pygame.font.Font('freesansbold.ttf', 24)
fontObj2 = pygame.font.Font(r'c:\windows\fonts\kaiu.ttf', 28)
fontObj2.set_bold(True)
fontObj3 = pygame.freetype.Font(r'c:\windows\fonts\mingliu.ttc', 16)

textObj = fontObj2.render('\u516c\u5b6b\u975e\u8c61\xb0\xfe\xff Hello world!', True, BLUE, WHITE)
textRectObj = textObj.get_rect()
textRectObj.center = (200, 150)

stops= [(220, 150), (240, 150), (260, 150), (280, 150), (300, 150), (320, 150), (340, 150), (360, 150),
    (360, 160), (360, 170), (360, 180), (360, 190), (360, 200),
    (360, 220), (360, 240), (360, 260), (360, 280), (360, 300),
    (330, 300), (290, 300), (260, 300), (230, 300), (200, 300),
    (200, 280), (200, 260), (200, 240), (200, 220), (200, 200), (200, 180), (200, 160), (200, 150)]

cnt = 0
circles = []

while not game_over:

    surface.fill(AQUA)

    for circle in circles:
        pygame.draw.circle(surface, YELLOW, (stops[circle][0]-30, stops[circle][1]-30), 10, 2)

    fontObj3.render_to(surface, (surface.get_width()//2, 20), f'{cnt}/{len(circles)}', BLACK)
    pygame.time.wait(500)
    textRectObj.center = stops[cnt]

    if (cnt+1)%len(stops) == 0:
        cnt = 0
        circles = []
    else:
        cnt += 1
        circles.append(cnt)
 
    surface.blit(textObj, textRectObj)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            cnt = 0
            circles = []

    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
