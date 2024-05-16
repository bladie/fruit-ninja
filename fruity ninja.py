import sys
import pygame
import random

pygame.init()

def menu():
    click = False #condition
    white = (255, 255, 255)
    black=(0,0,0)

    X = 580
    Y = 640

    home_page = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("FRUIT  WARRIOR")

    # creates a surface object, image is drawn on it
    image = pygame.image.load("wood3.png")

    while True:
        home_page.fill(white)  # completely fills the surface object with white colour
        home_page.blit(image, (0, 0))

        # buttons
        font1 = pygame.font.SysFont("Elephant", 33)
        text1 = font1.render('Levels', True, black)
        b1= pygame.Rect(30,400,210,60)
        text1Rect = text1.get_rect()
        text1Rect.center = (130,430)
        pygame.draw.rect(home_page,(255,222,173), b1)

        font2 = pygame.font.SysFont("Elephant", 30)
        text2 = font2.render('How to Play', True, black)
        b2 = pygame.Rect(350, 400, 210, 60)
        text2Rect = text2.get_rect()
        text2Rect.center = (455, 430)
        pygame.draw.rect(home_page, (255,222,173), b2)

        font3 = pygame.font.SysFont("Elephant", 33)
        text3 = font3.render('Credits', True, black)
        b3 = pygame.Rect(30, 520, 210, 60)
        text3Rect = text3.get_rect()
        text3Rect.center = (130, 545)
        pygame.draw.rect(home_page, (255,222,173), b3)

        font4 = pygame.font.SysFont("Elephant",33)
        text4 = font4.render('About', True, black)
        b4 = pygame.Rect(350, 520, 210, 60)
        text4Rect = text4.get_rect()
        text4Rect.center = (455, 545)
        pygame.draw.rect(home_page, (255,222,173), b4)

        home_page.blit(text1,text1Rect)
        home_page.blit(text2,text2Rect)
        home_page.blit(text3,text3Rect)
        home_page.blit(text4,text4Rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # quits the program

            if event.type == pygame.KEYDOWN: # for when the cursor is on top of the button
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if b1.collidepoint((mx, my)):
                    levels()

                if b2.collidepoint((mx, my)):
                    how_to()

                if b3.collidepoint((mx,my)):
                    Credits()

                if b4.collidepoint((mx,my)):
                    About()

        pygame.display.update()

def how_to():
    white = (255, 255, 255)
    X = 580
    Y = 640
    howto = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("FRUIT  WARRIOR")
    image = pygame.image.load("wood.png")

    howto.fill(white)
    howto.blit(image, (0, 0))

    while True:

        def blit_text(surface, text, pos, font, color=pygame.Color('black')):
            words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = surface.get_size()
            x, y = pos
            for line in words:
                for word in line:
                    word_surface = font.render(word, 0, color)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]
                y += word_height  # Start on new row

        text = '                        Welcome to Fruit Warrior.\n\n' \
               'The aim of the game is shoot fruits and avoid the bombs.\n\n' \
               'The Shurikens or blades can be shot out by clicking on the spacebar, the tank can be moved left ot right using the arrow keys.\n\n' \
               'Upon clicking on levels in the home page, you get to choose from either Level 1 or Level 2.\n\n' \
               'Level 1 (Classic Mode) is the game with bombs thrown at you along with   some limited lives(3).\n\n' \
               'Level 2 (Zen Mode) is the game with a fixed time of 60 seconds and no bombs or obstacle thrown at you.'
        font = pygame.font.SysFont("Constantia", 18)
        b5 = pygame.Rect(16, 60, 550, 520)
        pygame.draw.rect(howto, (244, 164, 96), b5)

        blit_text(howto, text, (20, 160), font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.display.update()

def Credits():
    white = (255, 255, 255)
    X = 580
    Y = 640
    Creditsg = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("FRUIT  WARRIOR")
    image = pygame.image.load("wood.png")

    Creditsg.fill(white)
    Creditsg.blit(image, (0, 0))

    while True:

        def blit_text(surface, text, pos, font, color=pygame.Color('black')):
            words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = surface.get_size()
            x, y = pos
            for line in words:
                for word in line:
                    word_surface = font.render(word, 0, color)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]
                y += word_height  # Start on new row

        text = "Game Designed by:\n" \
               "Sonakshi Arora\n" \
               "Ishmeen Kaur Garewal\n"\
               "Stuti Ray\n"
        font = pygame.font.SysFont("Lucida Calligraphy", 36)
        b5 = pygame.Rect(40, 60, 490, 500)
        pygame.draw.rect(Creditsg,(244, 164, 96), b5)
        blit_text(Creditsg, text, (55, 200), font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.display.update()

def About():
    white = (255, 255, 255)
    X = 580
    Y = 640
    howto = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("FRUIT  WARRIOR")
    image = pygame.image.load("wood.png")

    howto.fill(white)
    howto.blit(image, (0, 0))
    while True:

        def blit_text(surface, text, pos, font, color=pygame.Color('black')): #multiple line text assignment
            words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = surface.get_size()
            x, y = pos
            for line in words:
                for word in line:
                    word_surface = font.render(word, 0, color)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]
                y += word_height  # Start on new row

        text ='This game has been developed using Pygame and by using Pycharm as the IDE\n\n'\
              'This game was inspired by Fruit Ninja\n\n'\
              'Developed using various inbuilt modules found in Pycharm'
        font = pygame.font.SysFont("Constantia", 20)
        b5 = pygame.Rect(16, 60, 550, 520)
        pygame.draw.rect(howto, (244, 164, 96), b5)

        blit_text(howto, text, (20, 180), font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.display.update()


def levels():
    white = (255, 255, 255)
    black = (0, 0, 0)
    X = 580
    Y = 640
    level = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("FRUIT  WARRIOR")
    image = pygame.image.load("wood.png")

    level.fill(white)
    level.blit(image, (0, 0))
    while True:
        font5 = pygame.font.SysFont("Times New Roman", 63)
        text5 = font5.render('Choose One', True, white)
        font6 = pygame.font.SysFont("Algerian", 30)
        text6 = font6.render('CLASSIC MODE', True, black)
        font7 = pygame.font.SysFont("Algerian", 32)
        text7 = font7.render('ZEN MODE', True, black)
        b5 = pygame.Rect(330, 250, 210, 60)
        b6 = pygame.Rect(40, 250, 210, 60)
        text5Rect = text5.get_rect()
        text6Rect = text6.get_rect()
        text7Rect = text7.get_rect()
        text5Rect.center = (290, 170)
        text6Rect.center = (145, 280)
        text7Rect.center = (435, 280)
        pygame.draw.rect(level, (255, 222, 173), b5)
        pygame.draw.rect(level, (255, 222, 173), b6)
        level.blit(text5, text5Rect)
        level.blit(text6, text6Rect)
        level.blit(text7, text7Rect)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if b6.collidepoint((mx, my)):
                    game()

                if b5.collidepoint((mx, my)):
                    game2()

            if event.type == pygame.QUIT:
                return
            pygame.display.update()


def game2():
    WIDTH = 580  # 480
    HEIGHT = 640  # 600
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
    start_time = 60

    # Game graphics
    background = pygame.image.load('wood.png')
    fruit_images = []
    fruit_list = ['apple.png', 'orange.png', 'pineapple.png', 'mango.png', 'watermelon.png', 'pear.png',
                  'banana.png', 'lemon.png', 'pomegranate.png', 'pitaya.png']
    for img in fruit_list:
        fruit_images.append(pygame.image.load(img))

    # loading sounds

    # shoot = pygame.mixer.Sound('shoot.ogg')
    # bomb = pygame.mixer.Sound('bomb.ogg')
    # pygame.mixer.music.load('bg.ogg')  # for background music

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
            # shoot.play()

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

    class Bomb(pygame.sprite.Sprite):
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
                self.speedy = random.randrange(1, 8)

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

    # pygame.mixer.music.play(loops=-1)  # to keep on playing once it reaches the end
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

        screen.blit(text, [425, 10])

        all_sprites.update()

        # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True,
                                          True)  # 2 to delete both mob and bullet if collision happens
        for hit in hits:  # new mobs generated when bullet hits them
            print(hit)
            score += 1
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            print(score)

        collisions = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for collision in collisions:
            print(collision)
            lives = lives - 1
            n = Bomb()
            all_sprites.add(n)
            mobs.add(n)
            print(lives)
            print('BOMB!')
            mobs.play()
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
                pygame.quit()

        # Render/draw
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display (Double buffering)
        show_score(textX, textY)
        # show_lives(liveX, liveY)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        clock.tick(frame_rate)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            pygame.display.update()
    sys.exit()

def game():
    WIDTH = 580
    HEIGHT = 640
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
    pygame.display.set_caption("FRUIT  WARRIOR")
    clock = pygame.time.Clock()  # to keep track of time
    image = ''

    # Game graphics
    background = pygame.image.load('wood.png')
    fruit_images = []
    fruit_list = ['apple.png', 'orange.png', 'pineapple.png', 'mango.png', 'watermelon.png', 'pear.png',
                  'banana.png', 'lemon.png', 'pomegranate.png', 'pitaya.png']
    for img in fruit_list:
        fruit_images.append(pygame.image.load(img))

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('war.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH // 2  # attribute
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

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            """

            :rtype: object
            """
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = random.choice(fruit_images)
            self.image = self.image_orig
            img = self.image_orig
            self.rect = self.image.get_rect()
            if WIDTH > self.rect.width:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            else:
                0
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

    class Bomb(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = pygame.image.load('bomb.png')
            self.image = self.image_orig
            img = self.image_orig
            self.rect = self.image.get_rect()
            if WIDTH - self.rect.width < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width,0)
            else:
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
    bombs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()  # class name
    all_sprites.add(player)
    for i in range(8):  ##
        m = Mob()
        n = Bomb()
        all_sprites.add(m)
        all_sprites.add(n)
        mobs.add(m)
        bombs.add(n)

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

    def show_lives(X, Y, lives):
        life = font.render("Lives: " + str(lives), True, (255, 255, 255))
        screen.blit(life, (X, Y))

    # Game loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # keep running at the right/same speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Update
        all_sprites.update()
        # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True,
                                          True)  # 2 to delete both mob and bullet if collision happens
        for hit in hits:  # new mobs generated when bullet hits them
            print(hit)
            score += 1
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            print(score)

        collisions = pygame.sprite.groupcollide(bombs, bullets, True, True)
        for collision in collisions:
            print(collision)
            lives -= 1
            n = Bomb()
            all_sprites.add(n)
            bombs.add(n)
            print(lives)
            print('BOMB!')
            if lives == 0:
                running = False

        # Render/draw
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display (Double buffering)
        show_score(textX, textY)
        show_lives(liveX, liveY, lives)
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


        pygame.display.update()
    sys.exit()#closes the entire game

menu()
levels()
