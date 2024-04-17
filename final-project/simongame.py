import random
import sys
import time
import pygame
from pygame.locals import *

# Constants for the game
FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BUTTONSIZE = 100
BUTTONGAPSIZE = 20
FLASHSPEED = 500  # in milliseconds
FLASHDELAY = 200  # in milliseconds
TIMEOUT = 4  # seconds before game over if no button is pushed.

# Define colors / made additions to the original code
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
BRIGHTORANGE = (255, 165, 0)
ORANGE = (255, 140, 0)
BRIGHTPURPLE = (128, 0, 128)
PURPLE = (75, 0, 130)
BRIGHTPINK = (255, 105, 180)
PINK = (255, 20, 147)
BRIGHTCYAN = (0, 255, 255)
CYAN = (0, 139, 139)
BRIGHTGRAY = (169, 169, 169)
GRAY = (128, 128, 128)

# Background color
bgColor = BLACK

# Calculate margins
XMARGIN = int((WINDOWWIDTH - (3 * BUTTONSIZE) - (2 * BUTTONGAPSIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (3 * BUTTONSIZE) - (2 * BUTTONGAPSIZE)) / 2)

# Rect objects for each of the nine buttons / added more rect objects for the extra tiles
BUTTONRECTS = [
    pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), YMARGIN, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN, YMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE),
    pygame.Rect(XMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), YMARGIN + 2 * (BUTTONSIZE + BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE)
]

colors = [YELLOW, BLUE, RED, GREEN, ORANGE, PURPLE, PINK, CYAN, GRAY]

# Initialize Pygame
pygame.init()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Simulate')

# Font initialization
BASICFONT = pygame.font.Font(pygame.font.get_default_font(), 16)


def main():
    global FPSCLOCK, waitingForInput, pattern, currentStep, lastClickTime, score

    FPSCLOCK = pygame.time.Clock()

    # Initialize some variables for a new game
    pattern = []  # stores the pattern of colors
    currentStep = 0  # the color the player must push next
    lastClickTime = 0  # timestamp of the player's last button push
    score = 0
    waitingForInput = False

    while True:  # Main game loop
        clickedButton = None  # Button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.fill(bgColor)

        drawButtons()

        drawScore()

        checkForQuit() # added more elif commands for the added tiles
        for event in pygame.event.get():  # Event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
                print("Mouse clicked at position:", mousex, mousey)
                print("Clicked button:", clickedButton)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_e:
                    clickedButton = RED
                elif event.key == K_a:
                    clickedButton = GREEN
                elif event.key == K_s:
                    clickedButton = ORANGE
                elif event.key == K_d:
                    clickedButton = PURPLE
                elif event.key == K_z:
                    clickedButton = PINK
                elif event.key == K_x:
                    clickedButton = CYAN
                elif event.key == K_c:
                    clickedButton = GRAY


        if not waitingForInput:
            # Play the pattern
            print("Pattern:", pattern)  # Print the generated pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN, ORANGE, PURPLE, PINK, CYAN, GRAY))) #added extra colors
            for button in pattern:
                print("Button:", button)  # Print the button being flashed 
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # Wait for the player to enter buttons
            if clickedButton is not None and clickedButton == pattern[currentStep]:
                # Pushed the correct button
                flashButtonAnimation(clickedButton, animationSpeed=FLASHSPEED)  # Pass the color of the clicked button
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # Pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0  # Reset back to first step

            elif (clickedButton is not None and clickedButton != pattern[currentStep]) or (
                    currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # Pushed the incorrect button, or has timed out
                gameOverAnimation()
                # Reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def flashButtonAnimation(button_color, animationSpeed=50):
    flashColor = getBrightColor(colors.index(button_color))  # Get the bright color corresponding to the button color

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()

    for start, end, step in ((0, 255, 1), (255, 0, -1)):  # Animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill(flashColor + (alpha,))
            DISPLAYSURF.blit(flashSurf, BUTTONRECTS[colors.index(button_color)].topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))


def drawButtons():
    for i, rect in enumerate(BUTTONRECTS):
        color = getColor(i + 1)
        pygame.draw.rect(DISPLAYSURF, color, rect)


def drawScore():
    scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 100, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed):  # Animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons()  # Redraw the buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor


def gameOverAnimation(color=WHITE, animationSpeed=50):
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()

    r, g, b = color
    for i in range(3):  # Do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationSpeed * step):  # Animation loop
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def getButtonClicked(x, y):
    for i, rect in enumerate(BUTTONRECTS):
        if rect.collidepoint((x, y)):
            return colors[i]  # Return color (not index)
    return None


def getColor(index):
    return colors[index - 1]  # Get color corresponding to index (1-based)


def getBrightColor(index):
    bright_colors = [BRIGHTYELLOW, BRIGHTBLUE, BRIGHTRED, BRIGHTGREEN, BRIGHTORANGE, BRIGHTPURPLE, BRIGHTPINK, BRIGHTCYAN,
              BRIGHTGRAY]
    if isinstance(index, int):
        index = min(max(index, 1), len(bright_colors))
        return bright_colors[index - 1]  # Get bright color corresponding to index (1-based)
    else:
        # Handle invalid index here (e.g., return a default color)
        return WHITE  # Default color if index is invalid


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()