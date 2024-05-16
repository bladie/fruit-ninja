# pygame template - skeleton for a new pygame project; alt+cmd+L
import pygame
import random

WIDTH = 600 # 480
HEIGHT = 400 # 600
FPS = 60  # frames per second

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# initialize pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FRUIT NINJA")
image = ''

# For the timer
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 30

# Game graphics
background = pygame.image.load('wood.png')
fruit_images = []
fruit_list = ['apple.png', 'orange.png', 'pineapple.png', 'mango.png', 'watermelon.png', 'pear.png',
              'banana.png', 'lemon.png', 'pomegranate.png', 'pitaya.png']
for img in fruit_list:
    fruit_images.append(pygame.image.load(img))

# loading sounds

#shoot = pygame.mixer.Sound('shoot.ogg')
#bomb = pygame.mixer.Sound('bomb.ogg')
#pygame.mixer.music.load('bg.ogg')  # for background music


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('war.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()  # gives a list of key presses
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        # to keep within boundaries of the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        #shoot.play()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(fruit_images)
        self.image = self.image_orig
        img = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)  # to make them move diagonally
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360  # to prevent rotation more than 360 degrees
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


'''class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load('bomb.png')
        self.image = self.image_orig
        img = self.image_orig
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)  # to make them move diagonally
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360  # to prevent rotation more than 360 degrees
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)'''


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('blade.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()  # A group to make a collection of sprites
mobs = pygame.sprite.Group()  # for collision purposes
# bombs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()  # class name
all_sprites.add(player)
for i in range(8):  ##
    m = Mob()
    # n = Bomb()
    all_sprites.add(m)
    # all_sprites.add(n)
    mobs.add(m)
    # bombs.add(n)

score = 0
lives = 3
font = pygame.font.Font('freesansbold.ttf', 19)
textX = 10
textY = 10
liveX = 500
liveY = 10


def show_score(x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


'''def show_lives(x, y):
    global lives
    life = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(life, (x, y))'''

#pygame.mixer.music.play(loops=-1)  # to keep on playing once it reaches the end
# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    if output_string == "Time left: 00:00":
        screen.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text_surface = font.render("TIME UP", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        screen.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text_surface = font.render("Final score: " + str(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()

    # Blit to the screen
    text = font.render(output_string, True, WHITE)

    screen.blit(text, [450, 1])

    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)  # 2 to delete both mob and bullet if collision happens
    for hit in hits:  # new mobs generated when bullet hits them
        print(hit)
        score += 1
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        print(score)

    '''collisions = pygame.sprite.groupcollide(bombs, bullets, True, True)
    for collision in collisions:
        print(collision)
        lives = lives - 1
        n = Bomb()
        all_sprites.add(n)
        bombs.add(n)
        print(lives)
        print('BOMB!')
        bomb.play()
        if lives == 0:
            # running= False
            print("GAME OVER")
            screen.fill(BLACK)
            font = pygame.font.Font('freesansbold.ttf', 30)
            text_surface = font.render("GAME OVER", True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH / 2, HEIGHT / 2)
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(3000)
            screen.fill(WHITE)
            font = pygame.font.Font('freesansbold.ttf', 30)
            text_surface = font.render("Final score: " + str(score), True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH / 2, HEIGHT / 2)
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()'''

    # Render/draw
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display (Double buffering)
    show_score(textX, textY)
    # show_lives(liveX, liveY)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()

pygame.quit()