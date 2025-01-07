from turtle import Screen
import pygame 
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode(900,700)
b = pygame.image.load("9.png")
screen.blit(b,(0,0))

class Bin(pygame.sprite.Sprite):
    
    # properties/constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("3.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()


#Recyclable sprite
class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

#Non_recyclable sprite
class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('4.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

#List of images for Recyclable class
images=["2.png","5.png","1.png"]
        
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

for i in range(20):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(900)
    item.rect.y = random.randrange(700)
    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    item = Non_recyclable()
    item.rect.x = random.randrange(900)
    item.rect.y = random.randrange(700)
    plastic_list.add(item)
    all_sprites.add(item)

bin = Bin()
all_sprites.add(bin)
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.Font(None, 36)
text = font.render("Score: "+str(score), True, (255,255,255))

#Game loop
running = True
clock.tick(30)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    time_elapsed = time.time() - start_time
    if time_elapsed >= 60:
        if score > 50:
            text = font.render("You win! Score: "+str(score), True, (255,255,255))
        else:                 
            text = font.render("You lost! Score: "+str(score), True, (255,255,255))
        screen.blit(text, (400,350))
    else:
        countdown = font.render("Time left: "+str(60-int(time_elapsed)), True, (255,255,255))
        screen.blit(countdown, (400,350))
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            bin.rect.x -= 5
        if keys[K_RIGHT]:
            bin.rect.x += 5
        if keys[K_UP]:
            bin.rect.y -= 5
        if keys[K_DOWN]:
            bin.rect.y += 5
        screen.blit(text, (0,0))
        all_sprites.draw(screen)
        all_sprites.update()
        
        #Collision detection
        for item in item_list:
            if pygame.sprite.collide_rect(bin, item):
                score += 1
                text = font.render("Score: "+str(score), True, (255,255,255))
                item_list.remove(item)
                all_sprites.remove(item)
        for item in plastic_list:
            if pygame.sprite.collide_rect(bin, item):
                score -= 1
                text = font.render("Score: "+str(score), True, (255,255,255))
                plastic_list.remove(item)
                all_sprites.remove(item)

        screen.blit(text, (0,0))
        all_sprites.draw(screen)
        all_sprites.update()

    pygame.display.update()
pygame.quit()    

        


       
