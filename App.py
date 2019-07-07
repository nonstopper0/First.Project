import pygame

pygame.init()
display_height = 720
display_width = 1280
displayWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tycoon")
clock = pygame.time.Clock()

black = (10, 10, 10)
white = (255, 255, 255)
red = (255, 0, 0)
light_red = (50, 0, 0)
grey = (100, 100, 100)
# second github test
number = 0
numcolor = [0, 0, 0]


def text(location, text, size, color):
    # text objects
    font = pygame.font.SysFont("Myriad Pro", size)
    render = font.render(text, True, color)

    # get rect of text to return for use in collide-point functions below
    fontrect = render.get_rect()
    fontrect = fontrect.move(location)

    # display to screen
    displayWindow.blit(render, fontrect)

    # return rectangle of text for use with collidepoint
    return fontrect

# github upload test
def visuals():
    global numberButton, upButton, downButton, resetButton, number

    # fill display
    displayWindow.fill(grey)

    # interactive buttons using the text function above
    numberButton = text((display_width/2-15, 150), str(number), 100, numcolor)
    upButton = text((display_width/2 - 15, 50), "UP", 40, white)
    downButton = text((display_width/2 - 40, 300), "DOWN", 40, white)
    resetButton = text((60, 20), "RESET", 50, white)

    # border rectangles
    pygame.draw.rect(displayWindow, white, pygame.Rect(20, 20, 20, 680), 2)
    pygame.draw.rect(displayWindow, white, pygame.Rect(1240, 20, 20, 680), 2)

    # update the display
    pygame.display.update()


crashed = False

while not crashed:
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if numberButton.collidepoint(mouse):
                number = number * 2
            if upButton.collidepoint(mouse):
                if number < 10:
                    number += 1
                else:
                    number = int(number)*.2 + int(number)
            if downButton.collidepoint(mouse):
                number += -1
            if resetButton.collidepoint(mouse):
                number = 0

        if number >= 100 < 1000:
            numcolor[0] = 40
        if number >= 1000 < 10000:
            numcolor[0] = 70
        if number >= 10000 < 100000:
            numcolor[0] = 90
        if number >= 100000 < 1000000:
            numcolor[0] = 130
        if number >= 1000000 < 10000000:
            numcolor[0] = 170
        if number >= 10000000 < 1000000000:
            numcolor[0] = 200
        if number >= 1000000000 < 100000000000:
            numcolor[0] = 255

    visuals()
    clock.tick(20)

pygame.quit()

