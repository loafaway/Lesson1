import pygame

AQUA = (0, 255, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

FPS = 60

def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()

    fontObj = pygame.font.SysFont(None, 24)

    img = pygame.image.load('padepokan-small.png')
    imgrect = img.get_rect()
    imgrect.center = (screen.get_width())//2, (screen.get_height())//2

    Drag = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(AQUA)

        clicked = pygame.mouse.get_pressed()
        tx, ty = pygame.mouse.get_pos()
        x, y = imgrect.x, imgrect.y

        posText = fontObj.render(f'Now points at ({tx}, {ty})', True, WHITE, BLUE)
        posTextRect = posText.get_rect()
        posTextRect.x = screen.get_width()//2 - posTextRect.width//2
        screen.blit(posText, posTextRect)

        if (x <= tx and tx < x+imgrect.width) and (y <= ty and ty < y+imgrect.height):
            Drag = 1

        if not clicked[0]:  # left button pressed?
            Drag = 0

        if Drag == 1:       # ready to move the image
            imgrect.center = (tx, ty)

        screen.blit(img, imgrect)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()