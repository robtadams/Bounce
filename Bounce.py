import pygame
from Circle import circle

def bounce():

    # Initialize a pygame window
    pygame.display.init()
    pygame.font.init()

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

    # You're running, so keep running
    running = True

    # Initialize an empty list for the circles to be stored
    circles = []

    # Add a number of circles to the circles[] list
    for i in range(100):
        thisCircle = circle()
        thisCircle.color = (0,0,255)
        circles.append(thisCircle)

    redCircle = circles[-1]
    redCircle.color = (255,0,0)

    # Keep running until the user stops
    while running:

        # Update each circle
        for myCircle in circles:
            
            # Move the circle
            myCircle.moveCircle()

            # Draw the circle in its new location
            pygame.draw.ellipse(window, myCircle.color, myCircle.circleRect)

        # Update the window with the new drawing
        pygame.display.update()

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
                            running = False

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
                    text = font.render("Paused", True, (255,255,255), (0,0,0))

                    # Set the coordinates for the text
                    textRect = text.get_rect()
                    textRect.center = (windowWidth // 2, windowHeight // 2)

                    # Draw the Paused text
                    window.blit(text,textRect)
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

        # Erase all the circles
        window.fill(windowColor)
                                    
        # Wait
        pygame.time.wait(2)

    # Quit out of the game and then end the program
    pygame.quit()
    return True

def main():
    bounce()
    
main()
