import pygame
import random

class circle:

    def __init__(self):

        # Initialize the circle's color to be random
        self.red     =   random.randint(0,255)
        self.green   =   random.randint(0,255)
        self.blue    =   random.randint(0,255)

        # Set the circle's color to the randomized color
        self.color = [self.red, self.green, self.blue]

        # Initialize the circle's position to be random
        self.X = random.randint(0, 1920)
        self.Y = random.randint(0, 1080)

        # Initialize the circle's size
        self.Size = 100

        # Set the circle's position to be the randomized position
        # Set the circle's size to be 100x100
        self.circleRect = [self.X, self.Y, self.Size, self.Size]

        # Initialize the circle's velocity to be random
        self.horizontalVelocity  = random.randint(1,5)
        self.verticalVelocity    = random.randint(1,5)
        randVar = random.randint(0,3)

        if randVar == 1 or randVar == 3:
            self.horizontalVelocity *= -1

        if randVar == 2 or randVar == 3:
            self.verticalVelocity *= -1
        
    # Randomizes the circle's horizontal velocity
    def randomHorizontalVelocity(self):
        randVar = random.randint(1,5)
        self.horizontalVelocity = randVar
        return randVar

    # Randomizes the circle's vertical velocity
    def randomVerticalVelocity(self):
        randVar = random.randint(1,5)
        self.verticalVelocity = randVar
        return randVar

    # Randomizes the circle's horizontal velocity
    def randomNegativeHorizontalVelocity(self):
        randVar = random.randint(1,5)
        self.horizontalVelocity = -randVar
        return randVar

    # Randomizes the circle's vertical velocity
    def randomNegativeVerticalVelocity(self):
        randVar = random.randint(1,5)
        self.verticalVelocity = -randVar
        return randVar

    # Randomizes the circle's color
    def randomColor(self):
        self.red     =   random.randint(0,255)
        self.green   =   random.randint(0,255)
        self.blue    =   random.randint(0,255)

        self.color = [self.red, self.green, self.blue]
        return self.color

def bounce():

    # Initialize a pygame window
    pygame.display.init()
    pygame.font.init()

    # Set the Width and Height of the window
    windowSize = pygame.display.get_desktop_sizes()
    windowWidth = windowSize[0][0]
    windowHeight = windowSize[0][1]

    # Create a window and set it's size to the dimensions of the monitor
    window = pygame.display.set_mode((windowWidth,windowHeight))

    # Set the caption for the window
    pygame.display.set_caption("Bounce")

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
        circles.append(circle())

    # Keep running until the user stops
    while running:

        # Update each circle
        for myCircle in circles:

            # Draw a window color circle to erase the previous circle
            #pygame.draw.ellipse(window, (windowColor), myCircle.circleRect)

            # Move the circle
            myCircle.circleRect[0] += myCircle.horizontalVelocity
            myCircle.circleRect[1] += myCircle.verticalVelocity

            # If the circle passes the left wall...
            if myCircle.circleRect[0] < 0:

                # ... Change the circle's horizontal velocity
                #   to random int 1 through 5
                myCircle.randomHorizontalVelocity()
                

            # If the circle passes the right wall...
            elif myCircle.circleRect[0] > (windowWidth - myCircle.Size):

                # ... Change it's horizontal velocity
                #   to a random int -1 through -5
                myCircle.randomNegativeHorizontalVelocity()
                

            # If the circle passes through the ceiling...
            if myCircle.circleRect[1] < 0:

                # ... Change it's vertical velocity
                #   to a random int 1 through 5
                myCircle.randomVerticalVelocity()

            # If the circle passes through the floor...
            elif myCircle.circleRect[1] > (windowHeight - myCircle.Size):

                # ... Change it's vertical velocity
                #   to a random int -1 through -5
                myCircle.randomNegativeVerticalVelocity()

            # Draw the red circle in its new location                    
            pygame.draw.ellipse(window, myCircle.color, myCircle.circleRect)

        # Update the window with the new drawing
        pygame.display.update()

        # Pause and Quit handler
        # Check for events...
        for event in pygame.event.get():

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

                    """
### NEW STUFF START ###
                    """
                    print(pygame.font.get_fonts())
                    font = pygame.font.Font(pygame.font.match_font('impact'), 320)
                    text = font.render("Paused", True, (255,255,255), (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (windowWidth // 2, windowHeight // 2)
                    window.blit(text,textRect)
                    pygame.display.update()
                    """
### NEW STUFF STOP  ###
                    """

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
