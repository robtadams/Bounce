import random
import pygame

class circle:

    def __init__(self, color=None, coords=None, size=100):

        """ Color Initialization"""

        # If color is not defined...
        if not color:
            
            # ... Initialize the circle's color to be random
            self.red     =   random.randint(0,255)
            self.green   =   random.randint(0,255)
            self.blue    =   random.randint(0,255)

            # Set the circle's color to the randomized color
            self.color = [self.red, self.green, self.blue]

        # If color is defined...
        else:

            # ... Set the circle's color to the user provided values
            self.color = color

        """ Coordinates Initialization """

        # If coordinates are not defined...
        if not coords:

            # ... Initialize pygame and get the size of the desktop
            pygame.init()
            windowSize = pygame.display.get_desktop_sizes()[0]

            # Set windowWidth and windowHeight to the X and Y values of windowSize
            windowWidth     = windowSize[0] # windowSize[0] is the width of the screen
            windowHeight    = windowSize[1] # windowSize[1] is the height of the screen

            # Initialize the circle's position to be random
            self.X = random.randint(0, windowWidth)
            self.Y = random.randint(0, windowHeight)
            self.coords = [self.X, self.Y]

        # If the coordinates are defined...
        else:

            # ... Set the coordinate points X and Y to the user provided values
            self.X = coords[0]
            self.Y = coords[1]
            self.coords = coords

        """ Size Initialization """

        # Initialize the circle's size
        self.size = size

        """ Elipse Initialization """

        # Create the rectangle that pygame will use to draw the circle with
        # Rect --> [X coordinate, Y coordinate, Length, Width]
        # X and Y are either set by the user or randomly placed
        # The length and width should be the same for the image to be a circle
        self.circleRect = [self.X, self.Y, self.size, self.size]

        """ Velocity Initialization """

        # Initialize the circle's velocity to be random
        self.horizontalVelocity  = random.randint(1,5)
        self.verticalVelocity    = random.randint(1,5)

        # Randomly determine the direction of the circle's velocity
        randVar = random.randint(0,3)

        # Case 0: Positive X velocity, Positive Y velocity
        # Case 1: Negative X velocity, Positive Y velocity
        # Case 2: Positive X velocity, Negative Y velocity
        # Case 3: Negative X velocity, Negative Y velocity
        match randVar:
            case 0:
                pass
            case 1:
                self.horizontalVelocity = -self.horizontalVelocity
            case 2:
                self.verticalVelocity   = -self.verticalVelocity
            case 3:
                self.horizontalVelocity = -self.horizontalVelocity
                self.verticalVelocity   = -self.verticalVelocity
        
    # Randomizes the circle's horizontal velocity
    def randomVelocity(self, direction, positive=True):

        # Randomly determine the circle's new velocity
        randVar = random.randint(1,5)

        # If the velocity should be negative...
        if not positive:

            # ... Set the velocity to be negative
            randVar = -randVar

        # Set the new velocity to the circle's horizontalVelocity or verticalVelocity variable
        match direction:
            case "horizontal":
                self.horizontalVelocity = randVar

            case "vertical":
                self.verticalVelocity   = randVar

            # If direction isn't set to "horizontal" or "vertical" then throw a ValueError
            case other:
                raise Exception("ValueError: randomVelocity must be given a string argument of either 'horizontal' or 'vertical'.")
            
        return randVar

    # Randomizes the circle's color
    def randomColor(self): 
        self.red     =   random.randint(0,255)
        self.green   =   random.randint(0,255)
        self.blue    =   random.randint(0,255)

        self.color = [self.red, self.green, self.blue]
        return self.color

    # Moves the circle around the screen
    def moveCircle(self, windowWidth=None, windowHeight=None):

        """ Set Velocity """
        
        # Update the X and Y coordinates of the circle
        self.X += self.horizontalVelocity
        self.Y += self.verticalVelocity

        # Update the rectangle for the circle to be drawn
        self.circleRect[0] = self.X
        self.circleRect[1] = self.Y

        """ Get windowWidth and windowHeight """

        # If either windowWidth or windowHeight aren't set...
        if windowWidth == None or windowHeight == None:

            # ... Initialize pygame
            pygame.init()

            # Set windowSize to be the width and height of the desktop
            windowSize = pygame.display.get_desktop_sizes()[0]

        # If windowWidth isn't set...
        if windowWidth == None:

            # ... Set windowWidth to the width of the desktop
            windowWidth = windowSize[0]

        # If windowHeight isn't set...
        if windowHeight == None:

            # ... Set windowHeight to the height of the desktop
            windowHeight = windowSize[1]

        """ Initialize bounced """

        # Initialize whether the circle has bounced off of a wall
        bounced = False

        """ Check for bounces """

        # If the circle passes the left wall...
        if self.X <= 0:

            # ... Change the circle's horizontal velocity
            #   to random int 1 through 5
            self.randomVelocity("horizontal")
            bounced = True
            
        # If the circle passes the right wall...
        elif self.X >= (windowWidth - self.size):

            # ... Change it's horizontal velocity
            #   to a random int -1 through -5
            self.randomVelocity("horizontal", False)
            bounced = True
            
        # If the circle passes through the ceiling...
        if self.Y <= 0:

            # ... Change it's vertical velocity
            #   to a random int 1 through 5
            self.randomVelocity("vertical")
            bounced = True

        # If the circle passes through the floor...
        elif self.Y >= (windowHeight - self.size):

            # ... Change it's vertical velocity
            #   to a random int -1 through -5
            self.randomVelocity("vertical", False)
            bounced = True

        # Return True if the circle bounced off of a wall, otherwise return False
        return bounced
