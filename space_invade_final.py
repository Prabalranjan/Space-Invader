#I'VE DISABLE ALL THE Y-AXIS MOVEMENT OF THE PLAYER AT THE BEGGINING.

import pygame
#random is import because we need enemy to respawn/ appear in the random coordinates.
import random
import math
#to innsert music or sound into the game use mixer form pygame
from pygame import mixer

#initilize the pygame
pygame.init()

#create the screen
width, height= 800,600
screen = pygame.display.set_mode((800,600)) #width and height

#title and icon
pygame.display.set_caption("space invaders")    #use the set the name on the title bar.
icon=pygame.image.load("ufo.png")               #set the variable for the the icon name.png file is downloaded form flaticon.com
pygame.display.set_icon(icon)                   #initialize the variable.

#add backgrund. image is download form freepik.com. 
#here we only assign the background variable. adn we gona draw it inside the while loop.
# pygame.transform.scale is used to fit the picture with the window.
background=pygame.transform.scale(pygame.image.load("gameBG.jpg"),(width,height)) 


#background music.
mixer.music.load("background.mp3")
#now we want to play this music for the long time thorughout the game.
#so we use (-1) to play it in a loop.
mixer.music.play(-1)


#making player. picture is taken form flaticon.com
playerImg=pygame.image.load("player.png")


#in this cartesian product the center(0,0) is considered as the top left corner. 
#so imagine and guess a spot according to the game window size.
playerX=370
playerY=480
playerX_change=0
playerY_change=0

#multiple enemies
#we can add all the enemies on the list and display one by one it'll looks like it runs simultaneously.
enemyImg=[]
# enemyImg2=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

# enemyImg=[]
enemyImg2 = []
enemyX2 = []
enemyY2 = []
enemyX_change2 = []
enemyY_change2 = []
num_of_enemies2 = 2

#we've created list of all the characteristics of enemy and display them all together. 
#use the for loop to add the value to the lists.
#making the enemy. ive draw the picture. same as the player.
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    # enemyImg2.append(pygame.image.load("enemy_2.png"))
    #random is used here to appear/ respawn the enemy on the random places.
    enemyX.append(random.randint(0,735))
    enemyY.append(0)
    #this is important cause enemy will move by itself so enemyX and Y
    #will be have to  specify in earlier. not like the the player in the key binding.
    enemyX_change.append(0.5)
    enemyY_change.append(0.5) #enemy droping speed.

#enemy_2
# for i in range(num_of_enemies2):
#     enemyImg2.append(pygame.image.load("enemy_2.png"))
#     enemyX2.append(random.randint(0,735))
#     enemyY2.append(-4)
#     enemyX_change2.append(0.1)
#     enemyY_change2.append(0.1)
#     num_of_enemies2=2


#making of bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
#we shoot the bullet from the exact position of the ship( more accurately form the tip of the ship)
bulletY=480
bulletX_change = 0
bulletY_change = 0
#ready state means you cant see the bullet on screen. it  is ready but not appeard.
#fire state means you can see the bulle in the screen. it fired and appeared in the screen.
bullet_state="ready"



#score variable to count the score
# score=0
score_value=0
#this is for display score text in the game. we are using font,Font object.this is inbulid.
#the ttf faile be download fromm anywhere and the pasrticular file should have been in the same directory with the game file. 
font=pygame.font.Font("Roboto-Bold.ttf",32) #to check wheather a font style is in the system type this- print(pygame.font.get_fonts())
#this is the coordinates.
textX=0
textY=10


#game over text
over_font=pygame.font.Font("Roboto-Bold.ttf",100)

#now we create a function to draw the player icon the game window.
#blit is is used to draw the icon. it takes two parameter. the icon and the axes.
#here the x & y is 370 and 480 cause the look at the bottom ,there the the function is called
#and playerX and playerY is passed and in the function making x & y's value becomes the 370 & 480.

def player(x,y):
    screen.blit(playerImg,(x,y))


#same as the player we make a function for enemy.
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
    

# def enemy2(x,y,i):
    # screen.blit(enemyImg2[i], (x,y))

#fucntion for the bullet to the  called when the spacebar is pressed.
def fire_bullet(x,y):
    #we make  the bullet state global so that that it can acess  formm all over the code.
    global bullet_state
    bullet_state="fire"
    #here the the axes are increse by some values to adjust the bullet image. so it looks likes the the bulllet is fire from the the tip of the rocketship.
    #though the bullet is on the same s-axis of the player , so we adjust it by using test & trail method
    screen.blit(bulletImg, (x+16,y+13))


#function to check the collision of bullet and enemy.
def is_collision(enemyX,enemyY,bulletX,bulletY):
    #this is a very interesting concept. distance will measure the distance between bullet and the enemy and when it is smaller than a certain point the it is considerd as a collision between them. 
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    #when distance is smaller than some value  return true or false , if collided. 
    if distance < 27:
        return True
    else:
        return False


#funtion for score text to appear.
def show_score(x,y):
    #unlike other pictures we render the texts and then display it the game window.
    #
    score=font.render("score :" +  str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

#gam over function
def game_over_text():
    over_text=over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (150,200))



#GAME LOOP
#here we set infinite loop so that the game screen stays in the window for a infinite time, but that will make you your pc hang 
#so use a for loop for each and every events which includes closing the screen. 
running=True
while(True):
    FPS=90
    clock=pygame.time.Clock()
    clock.tick(FPS) #higher the fps faster it'll run. it is used to run the game caonsistant in any other computers faster than yours.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #though it is a event so we have to write it under the loop.
        # this code is used to check whether a key is pressed or not.
        
        if event.type == pygame.KEYDOWN: #this is used to register an event when a key is pressed.
            # print("a key has pressed")
            
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: #used to register a the left arrow key. BUT NOW ONLY THE A BUTTON LIKE A PRO GAMER.                   
                # print("left arrow is pressed")
                playerX_change -= 3 #just the simple control
            
            # if event.key == pygame.K_UP or event.key == pygame.K_w:
                # print("up arrow is pressed") 
                # playerY_change -= 2 #just the simple control 

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #for right arrow key and D button
                # print("right arrow is pressed")
                playerX_change += 3 #just the simple control
            
            # if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # playerY_change += 2 #just the simple control
            
            #this is to solve the problem of pressing space in the middle of bullet traveling.
            #we cant fire another bullet untill the bullet become  the ready state.
            if bullet_state == "ready":
            #fire the bullet in the spacebar.
                if event.key == pygame.K_SPACE:
                    #get the current x-coord of the spaceship.
                    bulletX = playerX #so that it wont follow the player movement after being shot. we store the playerX on bulletX and then we use the bulletX instead.
                    fire_bullet(bulletX,bulletY)
                    #to play the bullet sound it should be written inside the shooting mechanism.
                    #here we use mixer.sound instead of mixer.music casue laser sound is so small as campared to background music.
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
        #this code is to register the event of key up. just like the key down.
        if event.type == pygame.KEYUP:
           
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:   
                # print("key has been released")
                playerX_change = 0  #so that it stops moving whenever the key stroke is released
            
            # if event.key == pygame.K_UP or event.key == pygame.K_w:
                # playerY_change = 0
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                # print("key has been released")   
                 playerX_change = 0 #for both left and right
            
            # if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #   playerY_change = 0
    #R,G,B value to change the background of the game window. it should be inside the loop cause it will be run for the infinity untill
    #user exits it.
    #3 values specify RGB values, higher the value more dark it becomes, 255 is the limit
    #we call that function inside the loop cause we want to repeat and occure the player everytime on the screen.
    #it always call after the screen.fill / rgb cause if dont then ill print under the rgb and we wont be able to see it.
    screen.fill((0,0,0)) 

    #background image is drawn here.
    screen.blit(background, (0,0)) #after adding the pic all  the 
    #movement get slow ( player and enemy both). so we have to increase the speed of everything.

    # here the x co-ord is moving +ve by 0.05. which is to the right.
    # plaing with co ordinates
    # playerX += 0.05 
    #y is 600 and it is downward. the height is fro 0-600 downwards. so -ve will
    #go up and +ve will be low.
    # playerY -= 0.05 


    #here we chnage the playerX with the key control with the help of some simple 
    #arithmatic. 
    #playerX=370 + 0.03 or 370 + (-0.03) acoording to the key strokes.
    playerX += playerX_change
    # playerY += playerY_change 
    
    #here we are going to add the boundary to the both axes. so that the 
    #spaceship doenst move beyond the game window and stays inside it.
    if playerX <= 0:
        playerX = 0
    #i am using 736 cause we have taken the player of 64 pixel so the actual size will be 736. else if we 
    #give the limit 800 then the whole ship would have exceed the game window. 
    #every time it exceed the boundery , loop will delete the player form 0/800 and put it on the 0/736 so fast
    #it looked like it is not exceeding the limit. 
    elif playerX >= 736:
        playerX = 736 

    if playerY <= 0:
        playerY = 0

    elif playerY >= 536:
        playerY = 536

    

    #       ***********enemies movement*************
    #this for loop  is to specify which x/y axis is to move along, cause now there are 6 of them. use list index method and specify them with the help of [i].
    #enemy movement.
    for i in range(num_of_enemies):
        #game over 
        if enemyY[i] > 450:
            #this for loop is to send every enemies to 800 y-axis if one enemy has touch the dedline.
            for j in range (num_of_enemies):
                enemyY[j] =800
                # enemyY2[j]=800
            #game over function is called to show the text.
            game_over_text()
            #to play the sound in game over text.
            game_over_sound=mixer.Sound("horse.ogv")
            game_over_sound.play()
            pygame.mixer.music.pause()
            #to pause the background music in game over.
            pygame.mixer.music.pause()
            #then we come of out of this loop
            break
        enemyY[i] += enemyX_change[i]
        # enemyY2[i] += enemyX_change2[i]
        
    #we also need the the collision section inside the multiple enemy for loop to ensure each collision.
    #make sure this is not inside if or elif. it should be under for only.
        collision=is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        # collision=is_collision(enemyX2[i],enemyY2[i],bulletX,bulletY)
        #if collision occurs then we'll do this changes.
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
        #this is to respawn the enemy on random place after death.
            enemyX[i]=random.randint(0,750) # we change the random number from 800 to 768 so that it wont respawn greater than 768 then come down and get out of the window quickly.
            enemyY[i]=random.randint(-4,0)
            
            # enemyX2[i]=random.randint(0,750)
            # enemyY2[i]=-4
            
            #to make the collision sound 
            bullet_sound=mixer.Sound("explosion.wav")
            bullet_sound.play()
        #enemy function should be also called inside the for loop. 
        #we'll also specify the i in the function parameter to specify which enemy coord value it returns. 
        enemy(enemyX[i],enemyY[i],i)      
        # enemy2(enemyX2[i],enemyY2[i],i)

    #  *******bullet movement*******   #
    if bulletY <=0:
        bulletY = 480 #it came back to its original position which is playerX=480
        bullet_state = "ready" #it comes to ready state , ready to shoot again.
    #to shoot the bullet we have to write it under the while loop
    if bullet_state == "fire":
        #call the function of bullet to fire it.
        fire_bullet(bulletX,bulletY)
        bulletY -= 20

                                
    # #  *******COLLISION*******it is useless now******cause for multiple enemis we add this pasrt inside the multiple enemy loop********   #
    # collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    # #if collision occurs then we'll do this changes.
    # if collision:
    #     bulletY = 480
    #     bullet_state = "ready"
    #     score += 1
    #     print(score)
    #     #this is to respawn the enemy on random place after death.
    #     enemyX=random.randint(0,768) # we change the random number from 800 to 768 so that it wont respawn greater than 768 then come down and get out of the window quickly.
    #     enemyY=random.randint(0,150)



    # this value is sent to the function and new value x & y is is updated adn drawn by 
    #the screen.blit 
    player(playerX,playerY)
    # enemy(enemyX,enemyY) #this line belongs to the multiple enemy for loop. so we pc could know which image is moving.
    show_score(textX, textY)
    # this is very important line and it keeps updated and it should be updating.
    pygame.display.update() 
