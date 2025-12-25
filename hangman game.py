import pygame
import math
import random
#setup display
pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption("hangman")


#button variables 
radius = 20
gap = 15
letters = [] #[34,25,"A", true] type is stored
startx = round((800 - (radius*2 + gap)*13)/2)
starty = 400
A = 65

#game variables
hangman_status = 0
words= ["HLLLO", "PYTHON", "PYGAME", "DEVELOPER","IDE"]
word = random.choice(words)
guessed = []


#color
white = (255,255,255)
black = (0,0,0)


for i in range(26):

    x = startx+ gap*2 + ((radius*2+ gap)*(i%13))
    y = starty + ((i//13) *(gap+radius*2))
    letters.append([x,y,chr(A+i),True])

#fonts
font= pygame.font.SysFont("comicsans", 30)
word_font = pygame.font.SysFont("comicsans", 40)
title = pygame.font.SysFont("comicsans", 50)


#load imnage
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i)+ ".png")
    images.append(image)

#game variables

#game loop
def draw ():
    #should run at the speed, 60
    window.fill(white)
    text = title.render("DEVELOPER HANGMAN", 1, black)
    window.blit(text, (800/2 - text.get_width()/2, 20))

    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word+= letter +" "
        else:
            display_word += "_ "
    text = word_font.render(display_word,1,black)
    window.blit(text,(400,200))
    
    
    
    #draw buttons
    for  letter in letters: 
        x, y, ltr, visible = letter
            #alphabets inside a button
        if visible:
            pygame.draw.circle(window, black, (x,y), radius, 3)
            text = font.render(ltr, 1, black)
            window.blit(text, (x-text.get_width()/2 ,y-text.get_height()/2))

    window.blit(images[hangman_status], (150,100)) #depending on status of the hangman,we will draw the image
    pygame.display.update()

def display_message(message):
        pygame.time.delay(1000)
        window.fill(white)
        text = font.render(message, 1, black)
        window.blit(text, (800/2 - text.get_width()/2, 500/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)




FPS = 60
clock = pygame.time.Clock()
run = True



while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my  = pygame.mouse.get_pos ()
            for letter in letters:
                x,y,ltr,visible = letter 
                if visible:

                    dis = math.sqrt((x-mx)**2 + (y-my)**2)
                    if dis <radius:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    draw()
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You WON!")
        break


    if hangman_status==6: 
        display_message("You lost!")
        break
            #later in the game it will compare the position 
            # of cursor with the button on screen, if the cursor and the button-to-be pressed at the same coordinates, press the buttons!

pygame.quit()