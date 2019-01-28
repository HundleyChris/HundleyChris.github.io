import pygame
import time
import random


pygame.init()
white = (255, 255, 255)
green = (51, 204, 51)
Dgreen = (34, 99, 28)
red = (255, 0, 0)
purple = (238, 66, 244)
black = (0, 0, 0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)
img = pygame.image.load("snake.png")
spikeimg = pygame.image.load("spike.png")
appleimg = pygame.image.load("apple.png")
clock = pygame.time.Clock()
SpikeThickness = 25
AppleThickness = 25
block_size = 20
FPS = 30
direction ="right"
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
def randAppleGen():
   randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
   randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0
   return randAppleX, randAppleY
randAppleX, randAppleY = randAppleGen()
#1.Produces spikes randomly across the map "trial and error"
def randSpikeGen():
   randSpikeX = round(random.randrange(0, display_width-SpikeThickness))#/10.0)*10.0
   randSpikeY = round(random.randrange(0, display_height-SpikeThickness))#/10.0)*10.0
   return randSpikeX, randSpikeY
randSpikeX, randSpikeY = randSpikeGen()
def pause():
   paused = True
   while paused:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
               paused = False
            elif event.key ==pygame.K_q:
               pygame.quit()
               quit()
   gameDisplay.fill(white)
   message_to_screen("Paused!", black, -100, size = "large")
   message_to_screen("Press C to continue or Q to quit.", black, -25)
   pygame.display.update()
   clock.tick(5)


def score(score):
   text = smallfont.render("score: " +str(score), True, black)
   gameDisplay.blit(text, [0,0])


def game_intro():
   intro = True
   while intro:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
               intro = False
            if event.key == pygame.K_q:
               pygame.quit()
               quit()        
        #4. Changed start screen "trial and error"
      gameDisplay.fill(black)
      message_to_screen("Welcome to Slither", purple, -100, "large")
      message_to_screen("The objective of the game is to eat red apples", green, -30, "small")
      message_to_screen("The more apples you eat the more apples you get", green, 10, "small")
      message_to_screen("If you run into yourself, or the edges, you die!", green, 50, "small")
      message_to_screen("Press C to play or Q to quit.", white, 180, "small")
      pygame.display.update()
      clock.tick(15)


def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, Dgreen, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX, randAppleY = randAppleGen()
    randSpikeX, randSpikeY = randSpikeGen()
    while not gameExit:
        while gameOver == True:
            #5. Changed background "trial and error"
            gameDisplay.fill(red)
            message_to_screen("Game over!", black, y_displace = -50, size="large")
            message_to_screen("Press C to play again or Q to quit", black, 50, size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                   pause()
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_y += lead_y_change
        lead_x += lead_x_change
        #3.Makes the background green "trial and error"
        gameDisplay.fill(green)
        gameDisplay.blit(spikeimg, (randSpikeX, randSpikeY))
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        snakeHead =[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakeList)
        score(snakeLength-1)
        pygame.display.update()
        if lead_x >randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size< randAppleX + AppleThickness:
            if lead_y >randAppleY and lead_y < randAppleY + AppleThickness:
                print("x and y crossover")
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                print("x and y crossover")
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
        #2.When you hit the spikes you die "trial and error"
        if lead_x >randSpikeX and lead_x < randSpikeX + SpikeThickness or lead_x + block_size > randSpikeX and lead_x + block_size< randSpikeX + SpikeThickness:
            if lead_y >randSpikeY and lead_y < randSpikeY + SpikeThickness:
                print("x and y crossover")
                randSpikeX, randSpikeY = randSpikeGen()
                pygame.quit()
                quit()
            elif lead_y + block_size > randSpikeY and lead_y + block_size < randSpikeY + SpikeThickness:
                print("x and y crossover")
                randSpikeX, randSpikeY = randSpikeGen()
                pygame.quit()
                quit()
        clock.tick(FPS)
    pygame.quit()
    quit()


game_intro()
gameLoop()
