import pygame
import random
from Ship import Ship
from Alien import Alien
from ShipBullet import ShipBullet
from AlienBullet import AlienBullet

#Color constants
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()

#Display constants
display_width = 600
display_height = 800
velocity = 20

#List encapsulating bullets on field
shipBulletList = []
alienBulletList = []

#List encapsulating aliens on field
alienList = []

shipImage = pygame.image.load('player.png')

shipImage = pygame.transform.scale(shipImage, (100, 160))

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Alien Game')

clock = pygame.time.Clock()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def updateShip(x, y):
    gameDisplay.blit(shipImage, (x, y))


def displayShotAliens(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Shot Aliens: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def shootBullet(): #TODO: ADD TIME CONSTRAINT instead of length?
    if(len(shipBulletList) > 4):
        return
    bullet = ShipBullet(gameDisplay, ship)
    shipBulletList.append(bullet)

def updateShipBullets():
    for bullet in shipBulletList:
        if bullet.y < 0:
            #Garbage collection
            shipBulletList.remove(bullet)
            del bullet
            continue
        bullet.update()

def shootAlienBullet(alien):
    if (len(alienBulletList) > 4):
        return
    bullet = AlienBullet(gameDisplay, alien)
    alienBulletList.append(bullet)

def updateAlienBullets():
    for bullet in alienBulletList:
        if bullet.y > display_height:
            alienBulletList.remove(bullet)
            del bullet
            continue
        bullet.update()


#ADD MAXES TO EACH, 3 bullets at once, 4 aliens at once

#TODO: AFTER 100, ADD ANOTHER ALIEN?

def createAlien():
    if(len(alienList) > 4):
        return
    randomAI = random.randrange(1, 3)
    alien = Alien(gameDisplay, randomAI)
    alienList.append(alien)

def updateAliens():
    for alien in alienList:
        if alien.y > display_height:
            #Garbage collection
            alienList.remove(alien)
            del alien
            continue
        alien.update()
        fire = random.randrange(1, 30)
        if fire == 1:
            shootAlienBullet(alien)


#Check collisions against aliens
def collisionCheckAliens():
    for alien in alienList:
        #Check against ships bullets
        for bullet in shipBulletList:
            if alien.rect.colliderect(bullet.rect):
                if pygame.sprite.collide_mask(alien, bullet):
                    alienList.remove(alien)
                    del alien
                    shipBulletList.remove(bullet)
                    del bullet
                    global shotAliens
                    shotAliens += 1

#Check collisions against ship
def collisionCheckShip(ship):
    for alien in alienList:
        if alien.rect.colliderect(ship.rect):
            if pygame.sprite.collide_mask(alien, ship):
                alienList.remove(alien)
                del alien
                del ship #ADD LOGIC THAT SAYS YOU FAILED
                return True
    for bullet in alienBulletList:
        if ship.rect.colliderect(bullet.rect):
            if pygame.sprite.collide_mask(ship, bullet):
                alienBulletList.remove(bullet)
                del bullet
                del ship
                return True



def game_loop():
    global ship
    ship = Ship(gameDisplay)

    createAlien()

    global shotAliens #Displayed in upper half
    shotAliens = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        #TODO: OR MAYBE EVEN ALIENS IN FORMATION, ADD MOVEMENT LOGIC TO IT
        if keys[pygame.K_LEFT] and ship.x > velocity:
            ship.x -= 40
        if keys[pygame.K_RIGHT] and ship.x < display_width - 100 - velocity:
            ship.x += 40
        if keys[pygame.K_SPACE]:
            shootBullet()

        gameDisplay.fill(white)
        ship.updateShip()
        displayShotAliens(shotAliens)

        #Randomly creates aliens at a certain time
        randomNumber = random.randrange(1, 20)
        if(randomNumber == 1):
            createAlien()

        try:
            collisionCheckAliens()
        except UnboundLocalError as error:
            pass

        #Bullet update, add delay to amount of bullets you can shoot
        updateShipBullets()
        #Alien Updates\
        updateAliens()

        updateAlienBullets()

        if collisionCheckShip(ship):
            #message_display('You Died')
            pygame.time.delay(5000) #TODO: Clear logic and restart
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
quit()
