import pygame

def windowClick():
    windowWidth = 600
    windowHeight = 600

    window = pygame.display.set_mode((windowWidth, windowHeight))

    running = True
    clicked = False

    pygame.draw.rect(window, (255,0,0), [100, 100, 100, 100])
    pygame.display.update()

    while running:

        pygame.event.get()

        if pygame.mouse.get_pressed()[0]:
            if clicked != True:
                
                clicked = True
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                if mouseX >= 100 and mouseX <= 200:
                    if mouseY > 100 and mouseY <= 200:
                        print("You clicked on the box!")
                

        else:
            clicked = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()
    return True

def main():
    windowClick()
    
main()
