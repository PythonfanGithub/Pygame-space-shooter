import pygame #Hippity hoppity your library is now my property
import random #Hippity hoppity your module is now my property
from os import path
#Default settings

WIDTH = 480
HEIGHT = 600
FPS = 60
#load all game graphics
background = pygame.image.load('blue.png')
background_rect = background.get_rect()
player_img = pygame.image.load('PlayerShip.png')
meteor_img = pygame.image.load('meteor.png')
enemy_img = pygame.image.load('EnemyShip.png')
bullet_img = pygame.image.load('laser.png')
#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)


    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    mobs.add(m)

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 590
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate [pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self. rect.y += self.speedy
        #remove it if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
bullets = pygame.sprite.Group()

#Initialize pygame and create the window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(m)
#Game LÖÖP
running = True
while running:
    #Keep loop running at the right speed
    clock.tick(FPS)
    #Check to see if a mob hit the Player
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False


    #Procces input
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player.shoot()
    #Update
    all_sprites.update()

    #Draw / render

    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
    screen.fill(BLACK)


pygame.quit()
