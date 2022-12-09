import pygame
import random
from Circle import circle

def startMenu(window, windowWidth, windowHeight):

    """ Start Text Initialization """

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
    startFont = pygame.font.Font(pygame.font.match_font('impact'), windowWidth // 6)

    # Render the Start font
    startText = startFont.render("START", True, (0,0,0))

    # Set the coordinates for the text
    startTextRect = startText.get_rect()
    startTextRect.center = (windowWidth // 2, windowHeight // 2)

    # Draw the Start text
    window.blit(startText, startTextRect)

    """ Slider Initialization """

    # Set the coordinates for the slider line
    lineStartPos = [windowWidth // 4, 3 * windowHeight // 4]
    lineEndPos = [3 * windowWidth // 4, 3 * windowHeight // 4]

    # Set the color for the slider line
    lineColor = [255, 255, 255]

    # Draw the slider line
    pygame.draw.line(window, lineColor, lineStartPos, lineEndPos)

    # Set the coordinates for the slider circle
    circleMinPos = [windowWidth // 4, 3 * windowHeight // 4]
    circleMaxPos = [3* windowWidth // 4, 3 * windowHeight // 4]
    circlePos = circleMinPos

    # Set the color for the slider circle
    circleColor = [0, 0, 255]

    # Draw the slider circle
    pygame.draw.circle(window, circleColor, circlePos, 20)

    # Set the number of circles to be drawn
    numberOfCircles = 1

    numberFont = pygame.font.Font(pygame.font.match_font('impact'), windowWidth // 10)
    numberText = numberFont.render(str(numberOfCircles), True, (255, 255, 255))
    numberTextRect = numberText.get_rect()
    numberTextRect.center = [windowWidth // 8, windowHeight // 2]

    window.blit(numberText, numberTextRect)

    """ Start Loop """

    # While start is True...
    while start:

        # Get each event from the event queue...
        for event in pygame.event.get():

            # ... If the user pressed the left mouse button ...
            if event.type == pygame.MOUSEBUTTONDOWN:

                    # ... Get the X and Y position of the mouse
                    mousePos    = pygame.mouse.get_pos()
                    mouseX      = mousePos[0]
                    mouseY      = mousePos[1]

                    # If the X and Y position of the mouse is over the Start button ...
                    if mouseX >= startX and mouseX <= windowWidth - startX:
                        if mouseY >= startY and mouseY <= windowHeight - startY:

                            # ... Set start to False, which begins the game on the next loop
                            start = False

                    # If the X and Y position of the mouse is over the slider circle ...
                    if mouseX >= circlePos[0] - 20 and mouseX <= circlePos[0] + 20:
                        if mouseY >= circlePos[1] - 20 and mouseY <= circlePos[1] + 20:

                            # Set mouseButtonDown to True until the user releases the left mouse button
                            mouseButtonDown = True

                            # While the user keeps the left mouse button down...
                            while mouseButtonDown:

                                # ... Check if the user presses a button ...
                                for event in pygame.event.get():

                                    # ... If the user releases the left mouse button ...
                                    if event.type == pygame.MOUSEBUTTONUP:

                                        # ... set mouseButtonDown to false, exiting the loop
                                        mouseButtonDown = False
                                
                                # Erase previous circle
                                pygame.draw.circle(window, (0, 0, 0), circlePos, 20)

                                # Redraw the line
                                pygame.draw.line(window, lineColor, lineStartPos, lineEndPos)

                                # Get the mouse coordinates
                                mousePos = pygame.mouse.get_pos()
                                mouseX = mousePos[0]
                                mouseY = mousePos[1]

                                # If mouseX is less than the length of the slider line...
                                if mouseX <= windowWidth // 4:

                                    # ... set mouseX to the minimum point on the slider line
                                    mouseX = windowWidth // 4

                                # If mouseX is greater than the length of the slider line...
                                elif mouseX >= 3 * (windowWidth // 4):

                                    # ... set mouseX to the maximum point on the slider line
                                    mouseX = 3 * (windowWidth // 4)                                    
                                
                                # Set the X position of the circle to the X position of the mouse
                                circlePos[0] = mouseX

                                # Draw the circle at the mouse coordinates
                                pygame.draw.circle(window, circleColor, circlePos, 20)

                                sliderDistance = windowWidth // 2
                                sliderUnit = sliderDistance / 100
                                minCirclePoint = windowWidth // 4

                                numberOfCircles = (circlePos[0] - minCirclePoint) // sliderUnit

                                if numberOfCircles <= 1:
                                    numberOfCircles = 1

                                numberFont = pygame.font.Font(pygame.font.match_font('impact'), windowWidth // 10)
                                numberText = numberFont.render(str(int(numberOfCircles)), True, (255, 255, 255))
                                numberTextRect = numberText.get_rect()
                                numberTextRect.center = [windowWidth // 8, windowHeight // 2]

                                pygame.draw.rect(window, (0,0,0), [0, windowHeight // 3,
                                                                   windowWidth // 4, windowHeight // 3])

                                window.blit(numberText, numberTextRect)

                                # Update the screen
                                pygame.display.update()

            # ... If the user pressed a key ...          
            if event.type == pygame.KEYDOWN:

                # ... and that key is Escape ...
                if event.key == pygame.K_ESCAPE:

                    # ... Quit out of the game
                    pygame.quit()
                    return True

                # ... and that key is Space or Enter ...
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                    # ... Set start to False, which begins the game on the next loop
                    start = False

        # Update the screen
        pygame.display.update()

    return numberOfCircles

def bounce():

    """ Pygame Initialization """

    # Initialize a pygame window
    pygame.display.init()
    pygame.font.init()

    """ Window Initialization and Construction """

    # Set the Width and Height of the window
    windowSize = pygame.display.get_desktop_sizes()[0]
    windowWidth = windowSize[0] // 2
    windowHeight = windowSize[1] // 2

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
    numberOfCircles = int(startMenu(window, windowWidth, windowHeight))

    """ Circle Initialization and Construction """

    # Initialize an empty list for the circles to be stored
    circles = []

    # Add a number of circles to the circles[] list
    for i in range(numberOfCircles):
        thisCircle = circle(windowSize=(windowWidth, windowHeight))
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

        """ Pause and Quit Handler """

        # Check for events...
        for event in pygame.event.get():
            
            # ... If the user clicks on the mouse ...
            if event.type == pygame.MOUSEBUTTONDOWN:

                # ... Get the coordinates of the cursor ...
                mousePos    = pygame.mouse.get_pos()
                mouseX      = mousePos[0]
                mouseY      = mousePos[1]

                # ... If the mouse is over the Red Circle ...
                if mouseX >= redCircle.X and mouseX <= (redCircle.X + redCircle.size):
                    if mouseY >= redCircle.Y and mouseY <= (redCircle.Y + redCircle.size):

                        # ... Get rid of that circle
                        circles.pop()

                        # Then, if there are still more circles on screen ...
                        if len(circles) > 0:

                            # ... Set another circle as the Red Circle
                            redCircle = circles[-1]
                            redCircle.color = (255,0,0)

                        # Otherwise, if there are no more circles on screen ...
                        else:

                            # ... Reset the game
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
                    pauseFont = pygame.font.Font(pygame.font.match_font('impact'), 320)

                    # Render the Paused font
                    pauseText = pauseFont.render("PAUSED", True, (0,0,0), (255,255,255))

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
                                    clock.tick(60)

                                # ... and that button is escape...
                                if event.key == pygame.K_ESCAPE:

                                    # ... unpause the game and exit the program
                                    running = False
                                    paused = False

        """ Time Stuff """

        currentTime += clock.tick(60)
        seconds = str((currentTime // 1000) % 60).zfill(2)
        minutes = currentTime // 60000
        
        timeFont = pygame.font.Font(pygame.font.match_font('impact'), 32)
        timeText = timeFont.render(f"{minutes}:{seconds}".format(minutes, seconds), True, (255,0,0))
        window.blit(timeText, (50, 50))

        # Update the display and erase the screen
        pygame.display.update()
        window.fill(windowColor)

    # Quit out of the game and then end the program
    pygame.quit()
    return True

if __name__ == "__main__":
    bounce()
