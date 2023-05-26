import pygame
import random
import time

# Initializing Pygame
pygame.init()   

#Screen 
widthsc = 860
heightsc = 500
x=500 #rocket position x scale
y=650 #rocket position y scale


# Create the window
screen = pygame.display.set_mode((widthsc,heightsc))
hero= pygame.image.load('rocket.jfif').convert()#1st rocket
rect_hero= hero.get_rect(midbottom=(x,y))
rocket1=pygame.transform.scale(hero,(60,90))
pygame.display.set_caption("Cosmic conquest")
ob1=pygame.transform.scale(pygame.image.load('ob1.jpg').convert(),(20,30))
obs=pygame.transform.scale(pygame.image.load('obstacle.png').convert(),(80,80))
rect_obs=obs.get_rect(midbottom=(400,100))
# colors
black =(0, 0, 0)
white = (255, 255, 255) 

font = pygame.font.SysFont("monospace", 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])


stars = []
# Drawing 100 stars
for i in range(100):
    x = random.randint(0, widthsc)
    y = random.randint(-200, -50)  # Generate stars above the top of the screen
    size = random.randint(1, 3)
    speed = 10
    stars.append([x, y, size, speed])

def start_screen():
    exit_game= False
    while not exit_game:
        screen.fill(black)
        img = pygame.image.load('Cosmic-conquest.jpeg')

        screen.blit(img,(10,40))
        
        text_screen("Press Enter To Start", white,250,400)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_game = True
                    game_loop()
           

# Game Loop
def game_loop():
    # Get the start time
    start_time = time.time()
    bullet_fired = False
    while True:
        # Event Handler
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                # Quitting game
                pygame.quit();
                quit()
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_SPACE:
                    bullet_fired = False
        # Move the stars downwards and redraw them
        screen.fill((0, 0, 0))  # Fill the screen with black color

        
        # Drawing Stars in background
        for i in range(len(stars)):
            # Update the star position
            elapsed_time = time.time() - start_time
            if elapsed_time < 2:
            # Increase the speed for the first 6 seconds
                stars[i][3] = 8
            elif elapsed_time < 4:
                stars[i][3] = 6
            elif elapsed_time < 6:
                stars[i][3] = 4
            else:
                # Decrease the speed after 6 seconds
                stars[i][3] = 2
            stars[i] = [stars[i][0], stars[i][1] + stars[i][3], stars[i][2], stars[i][3]]
            
            # Redraw the entire screen before drawing the star at its new position
            pygame.draw.circle(screen, (0, 0, 0), (stars[i][0], stars[i][1] - stars[i][3]), stars[i][2] + 1)
            pygame.draw.circle(screen, (255, 255, 255), (stars[i][0], stars[i][1]), stars[i][2])

            # If a star has gone off the bottom of the screen, reset it to above the top of the screen
            if stars[i][1] > heightsc:
                stars[i] = [random.randint(0, widthsc), random.randint(-200, -50), stars[i][2], stars[i][3]]
        

        #event handling 
        keys_pressed = pygame.key.get_pressed()
        #moving left
        if keys_pressed[pygame.K_LEFT]:
          rect_hero.x -=1  
        #moving right
        if keys_pressed[pygame.K_RIGHT]:
            rect_hero.x +=1
        #if rocket goes out side the screen
        if rect_hero.x>750:
            rect_hero.x=730
        if rect_hero.x<20:
            rect_hero.x=30
        screen.blit(rocket1,rect_hero)
        screen.blit(obs,rect_obs)
        
        if keys_pressed[pygame.K_SPACE]:
         #bullet code
          # Only fire if the bullet is not already on the screen
            if not bullet_fired:
                bullet_fired = True
                obx=29+rect_hero.x
                oby=rect_hero.y
                rect_ob1 = ob1.get_rect(midbottom=(obx, oby ))
                bullet_speed = 1
            # Move the bullet upwards and redraw it
            if rect_ob1.bottom > 0:
                rect_ob1.y -= bullet_speed
                screen.blit(ob1, rect_ob1)
            # Reset the bullet position and flag when it goes off the screen
            else:
                bullet_fired = False
                rect_ob1 = ob1.get_rect(midbottom=(0, 0))  

        pygame.display.update()

start_screen()