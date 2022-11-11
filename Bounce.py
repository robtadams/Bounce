import pygame
import random
from Circle import circle

def startMenu(window, windowWidth, windowHeight):

    # If start is True, then stay on the Start Menu
    # If start is False, then leave the Start Menu
    start = True

    # Scale the size of the Start Menu to the size of the window
    startX = windowWidth // 4
    startY = windowHeight // 3

    # Make the Start Menu text color white
    startTextColor = (255,255,255)

    # Initialize the Start Menu rectangle and draw it to the screen
    startRect = [startX, startY, windowWidth // 2, windowHeight // 3]
    pygame.draw.rect(window, startTextColor, startRect)

    # Set the font
    font = pygame.font.Font(pygame.font.match_font('impact'), windowWidth // 6)

    # Render the Start font
    startText = font.render("Start", True, (0,0,0))

    # Set the coordinates for the text
    startTextRect = startText.get_rect()
    startTextRect.center = (windowWidth // 2, windowHeight // 2)

    # Draw the Start text
    window.blit(startText, startTextRect)

    pygame.display.update()

    while start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos    = pygame.mouse.get_pos()
                    mouseX      = mousePos[0]
                    mouseY      = mousePos[1]
                    if mouseX >= startX and mouseX <= windowWidth - startX:
                        if mouseY >= startY and mouseY <= windowHeight - startY:
                            start = False
                            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    start = False

def bounce():

    """ Pygame Initialization """

    # Initialize a pygame window
    pygame.display.init()
    pygame.font.init()

    """ Window Initialization and Construction """

    # Set the Width and Height of the window
    windowSize = pygame.display.get_desktop_sizes()[0]
    windowWidth = windowSize[0]
    windowHeight = windowSize[1]

    # Create a window and set it's size to the dimensions of the monitor
    window = pygame.display.set_mode((windowWidth,windowHeight))

    # Set the caption for the window
    pygame.display.set_caption("Bounce!")

    # Set the color to fill the window
    windowColor = [0,0,0]

    # Fill the screen with the window color
    window.fill(windowColor)

    """ Running Initialization """

    # You're running, so keep running
    running = True

    """ Start Menu """

    # Launch the Start Menu
    startMenu(window, windowWidth, windowHeight)

    """ Circle Initialization and Construction """

    # Initialize an empty list for the circles to be stored
    circles = []

    # Add a number of circles to the circles[] list
    for i in range(100):
        thisCircle = circle()
        thisCircle.color = (0,0,255)
        circles.append(thisCircle)

    """ Red Circle Initialization and Coloration """

    redCircle = circles[-1]
    redCircle.color = (255,0,0)

    """ Initialize Time and Clock """

    # Set the pygame Clock
    clock = pygame.time.Clock()

    # Initialize the current time to be 0
    currentTime = 0

    """ Main Loop Start """

    # Keep running until the user stops
    while running:

        # Update each circle
        for myCircle in circles:
            
            # Move the circle
            myCircle.moveCircle(windowWidth, windowHeight)

            # Draw the circle in its new location
            pygame.draw.ellipse(window, myCircle.color, myCircle.circleRect)

        # Update the window with the new drawing
        #pygame.display.update()

        # Pause and Quit handler
        # Check for events...
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos    = pygame.mouse.get_pos()
                mouseX      = mousePos[0]
                mouseY      = mousePos[1]
                if mouseX >= redCircle.X and mouseX <= (redCircle.X + redCircle.size):
                    if mouseY >= redCircle.Y and mouseY <= (redCircle.Y + redCircle.size):
                        circles.pop()
                        if len(circles) > 0:
                            redCircle = circles[-1]
                            redCircle.color = (255,0,0)
                        else:
                            bounce()

            # ... If the user presses a key...
            if event.type == pygame.KEYDOWN:

                # ... If the user presses escape...
                if event.key == pygame.K_ESCAPE:

                    # ... End the program on the next loop
                    running = False

                # ... If the user presses space...
                if event.key == pygame.K_SPACE:

                    # ... Pause the game
                    paused = True

                    # Set the font
                    font = pygame.font.Font(pygame.font.match_font('impact'), 320)

                    # Render the Paused font
                    pauseText = font.render("Paused", True, (255,255,255), (0,0,0))

                    # Set the coordinates for the text
                    pauseTextRect = pauseText.get_rect()
                    pauseTextRect.center = (windowWidth // 2, windowHeight // 2)

                    # Draw the Paused text
                    window.blit(pauseText,pauseTextRect)
                    pygame.display.update()

                    # While the game is paused...
                    while paused:

                        # ... Check for events...
                        for event in pygame.event.get():

                            # ... If the user presses a button...
                            if event.type == pygame.KEYDOWN:

                                # ... and that button is space...
                                if event.key == pygame.K_SPACE:

                                    # ... unpause the game
                                    paused = False

                                # ... and that button is escape...
                                if event.key == pygame.K_ESCAPE:

                                    # ... unpause the game and exit the program
                                    running = False
                                    paused = False

        """ Time Stuff """
        currentTime += clock.tick(60)
        currentTime *= 2
        printTime = str(currentTime // 1000)
        myStr = "{:<10}".format(printTime)
        
        font = pygame.font.Font(pygame.font.match_font('impact'), 32)
        timeText = font.render(myStr, True, (255,0,0))
        timeTextRect = timeText.get_rect()
        timeTextRect.center = (100, 100)
        window.blit(timeText, timeTextRect)

        # Update the display and erase the screen
        pygame.display.update()
        window.fill(windowColor)
                      
        # Wait
        #pygame.time.wait(2)

    # Quit out of the game and then end the program
    pygame.quit()
    return True

def main():
    bounce()
    
main()
