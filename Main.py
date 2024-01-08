import pygame
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#set up variables for flake 1 position
flake1x = 20
flake1y = -100 #start above the screen

#set up variables for flake 2 position
flake2x = 300
flake2y = -50

flake3x = 255
flake3y = -75

flake4x = 200
flake4y = -30

flake5x = 290
flake5y = -45

flake6x = 195
flake6y = -60

flake7x = 225
flake7y = -25

flake8x = 175
flake8y = -70

flake9x = 240
flake9y = -15

flake10x = 265
flake10y = -95

flake5x = 235
flake5y = -70

flake5x = 200
flake5y = -70


while(1): #omg game lup---------
    clock.tick(60) #FPS
    
    #physics section----
    
    #move flakes
    flake1y+=2 #this one moves faster
    flake2y+=1
    flake3y+=2
    flake4y+=1
    flake5y+=3
    flake6y+=1
    flake7y+=2
    flake8y+=2
    flake9y+=1
    flake10y+=1
 
    #reset flakes to top of screen
    if flake1y > 500:
        flake1y = -100
    if flake2y > 500:
        flake2y = -50
    if flake3y > 500:
        flake3y = -60
    if flake4y > 500:
        flake4y = -30
    if flake5y > 500:
        flake5y = -70
    if flake6y > 500:
        flake6y = -20
    if flake7y > 500:
        flake7y = -45
    if flake8y > 500:
        flake8y = -85
    if flake9y > 500:
        flake9y = -35
    if flake10y > 500:
        flake10y = -90

    
    
    
    #render section---
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255, 255, 255), (flake1x, flake1y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake2x, flake2y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake3x, flake3y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake4x, flake4y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake5x, flake5y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake6x, flake6y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake7x, flake7y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake8x, flake8y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake9x, flake9y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake10x, flake10y), 3)
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()

