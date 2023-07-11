import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (173, 216, 255)
BG_COLOR = (60, 70, 197)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("김예서 20200365")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



def newItem():
    i = Item()
    all_sprites.add(i)
    items.add(i)

def newObstacle():
    o = Obstacle()
    all_sprites.add(o)
    obstacles.add(o)


def draw_life_bar(surf, x, y, lifeLeft):
    if lifeLeft < 0:
        lifeLeft = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (lifeLeft / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        player_img = player_images[0]
        self.image = pygame.transform.scale(player_img, (120, 120))
        self.image_orig = self.image
        # self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.top = 60
        self.speedx = 0
        self.shield = 100
        self.life = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

        self.rot = 0
        # self.rot_speed = random.randrange(-2, 70)
        self.rot_speed = 10
        self.last_update = pygame.time.get_ticks()

    def rotate(self):

        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center



    def update(self):
        if player.life >= 80:
            player_img = player_images[0]
            self.image = pygame.transform.scale(player_img, (120, 120))
            self.image_orig = self.image
            self.image.set_colorkey(BLACK)
            # player_img = pygame.image.load(path.join(img_dir, player_list[0])).convert()
            # player_img.set_colorkey(BLACK)
        elif 80 > player.life >= 60:
            player_img = player_images[1]
            self.image = pygame.transform.scale(player_img, (120, 120))
            self.image_orig = self.image
            self.image.set_colorkey(BLACK)
        elif 60 > player.life >= 40:
            player_img = player_images[2]
            self.image = pygame.transform.scale(player_img, (120, 120))
            self.image_orig = self.image
            self.image.set_colorkey(BLACK)
        elif 40 > player.life >= 20:
            player_img = player_images[3]
            self.image = pygame.transform.scale(player_img, (120, 120))
            self.image_orig = self.image
            self.image.set_colorkey(BLACK)

        elif 20 > player.life >= 0:
            player_img = player_images[4]
            self.image = pygame.transform.scale(player_img, (120, 120))
            self.image_orig = self.image
            self.image.set_colorkey(BLACK)
        else:
            print('생명력 0 이하')
        

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH + 20:
            self.rect.right = WIDTH + 20
        if self.rect.left < 0:
            self.rect.left = 0

        # self.rotate()




class Item(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['fertilizer'])
        # self.image_orig.set_colorkey(BLACK)
        self.image = item_images[self.type]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(BLACK)
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = HEIGHT
        self.speedy = random.randrange(10, 12)
        self.speedy *= -1
    def update(self):

        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -100 or self.rect.right > WIDTH + 100:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['bird', 'trash01', 'trash02', 'trash03'])
        # self.image_orig.set_colorkey(BLACK)
        self.image = obstacle_images[self.type]
        self.rect = self.image.get_rect()

        self.image.set_colorkey(BLACK)
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = HEIGHT
        self.speedy = random.randrange(5, 10)
        self.speedy *= -1
    def update(self):

        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -100 or self.rect.right > WIDTH + 100:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class hitFX(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.image = hit_image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.image.set_colorkey(BLACK)



    def update(self):
        if tick % 15 == 0:
            self.kill()

#
def show_go_screen():
    screen.blit(start_background, start_background_rect)
    draw_text(screen, "Fly Flowerpot", 64, WIDTH / 2,75)
    draw_text(screen, "Help the flowerpot to land safely!", 22,
              WIDTH / 2, HEIGHT * 3 / 4 - 20)
    draw_text(screen, "Press arrow keys move", 18,
              WIDTH / 2, HEIGHT * 3 / 4 + 10)
    draw_text(screen, "Press a key to begin", 20, WIDTH / 2, HEIGHT * 3 / 4 + 50)
    pygame.display.flip()
    main_waiting = True

    while main_waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                game_start = True
                main_waiting = False
                return game_start
#
def show_end_screen():
    screen.fill(BLACK)
    draw_text(screen, "Game Over", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Press SPACEBAR to return to main menu", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    fail_waiting = True

    while fail_waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_go_screen()
#
def show_clear_screen():
    screen.blit(success_background, success_background_rect)
    draw_text(screen, "Game Clear!", 64, WIDTH / 2, 75 )
    draw_text(screen, "Press SPACEBAR to return to main menu", 18, WIDTH / 2, HEIGHT * 3 / 4+5)
    pygame.display.flip()
    clear_waiting = True

    print(running)
    while clear_waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_go_screen()



### 게임 그래픽 로드 ###

# 배경 이미지 로드
background = pygame.image.load(path.join(img_dir, "BG.png")).convert()
background_rect = background.get_rect()
start_background = pygame.image.load(path.join(img_dir, "start_BG.png")).convert()
start_background_rect = start_background.get_rect()
success_background = pygame.image.load(path.join(img_dir, "success_BG.png")).convert()
success_background_rect = success_background.get_rect()

# 플레이어(화분) 이미지 로드
player_images = []
player_list = ['FlowerPot01.png', 'FlowerPot02.png', 'FlowerPot03.png',
                 'FlowerPot04.png', 'FlowerPot05.png']
for img in player_list:
    player_images.append(pygame.image.load(path.join(img_dir, img)).convert())

# 이펙트 로드
hit_image = pygame.image.load(path.join(img_dir, 'hit.png')).convert()
hit_image = pygame.transform.scale(hit_image, (70, 70))

# 아이템 이미지 로드
item_images = {}
item_images['fertilizer'] = pygame.image.load(path.join(img_dir, 'fert.png')).convert()
item_images['fertilizer'] = pygame.transform.scale(item_images['fertilizer'], (50, 50))

# 장애물 이미지 로드
obstacle_images = {}
obstacle_images['trash01'] = pygame.image.load(path.join(img_dir, 'trash01.png')).convert()
obstacle_images['trash01'] = pygame.transform.scale(obstacle_images['trash01'], (30, 30))
obstacle_images['trash02'] = pygame.image.load(path.join(img_dir, 'trash02.png')).convert()
obstacle_images['trash02'] = pygame.transform.scale(obstacle_images['trash02'], (50, 50))
obstacle_images['trash03'] = pygame.image.load(path.join(img_dir, 'trash03.png')).convert()
obstacle_images['trash03'] = pygame.transform.scale(obstacle_images['trash03'], (40, 40))
obstacle_images['bird'] = pygame.image.load(path.join(img_dir, 'bird.png')).convert()
obstacle_images['bird'] = pygame.transform.scale(obstacle_images['bird'], (100, 100))




### 사운드 로드 ###
gameFail_sound = pygame.mixer.Sound(path.join(snd_dir, 'gameFail.wav'))
gameClear_sound = pygame.mixer.Sound(path.join(snd_dir, 'gameClear.wav'))
item_sound = pygame.mixer.Sound(path.join(snd_dir, 'item.wav'))
bird_sound = pygame.mixer.Sound(path.join(snd_dir, 'bird.wav'))
trash_sound = pygame.mixer.Sound(path.join(snd_dir, 'trash.mp3'))
bomb_sound = pygame.mixer.Sound(path.join(snd_dir, 'bomb.mp3'))
pygame.mixer.music.load(path.join(snd_dir, 'bgm.mp3'))
pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(loops=-1)





# Game loop
game_start = True
game_over = False
game_clear = False
running = True
clock = pygame.time.Clock()
tick = 0
metersLeft = 100

### While loop ###
while running:
    tick += 1
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    # 게임시작/게임오버
    if game_start:
        print('돌아오나')
        game_start = False
        pygame.mixer.music.play(loops=-1)
        show_go_screen()
        metersLeft = 100
        all_sprites = pygame.sprite.Group()
        obstacles = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        items = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)

    if game_over:
        gameFail_sound.play()
        pygame.mixer.music.stop()
        show_end_screen()
        game_over = False
    
    if game_clear:
        gameClear_sound.play()
        pygame.mixer.music.stop()
        show_clear_screen()
        game_clear = False


    # 게임 오버 조건
    if player.life <= 0:
        game_over = True
    
    # 미터 조절
    if tick % 60 == 0:
        metersLeft -= 1
    # 게임 클리어조건
    if metersLeft <= 0:
        metersLeft = 0
        game_clear = True


    # Update
    all_sprites.update()

    # 장애물 / 아이템 스폰 (레벨)
    if tick % 50 == 0 and metersLeft >= 70:
        newObstacle()
    elif tick % 30 == 0 and 70 > metersLeft >= 30:
        newObstacle()
    elif tick % 15 == 0 and 30 > metersLeft >= 0:
        newObstacle()
    if tick % (60*3) == 0:
        newItem()


    #### 아이템 ####
    item_col = pygame.sprite.spritecollide(player, items, True, pygame.sprite.collide_circle)
    for i_col in item_col:
        if i_col.type == 'fertilizer':
            player.life += 20
            item_sound.play()
        newItem()
        if player.life >= 100:
            player.life = 100

    #### 장애물 ####
    ob_hits = pygame.sprite.spritecollide(player, obstacles, True, pygame.sprite.collide_circle)
    for ob_hit in ob_hits:
        if ob_hit.type == 'bird':
            player.life -= 30 # 30
            bird_sound.play()
            hit = hitFX(ob_hit.rect.center, 'player')
            all_sprites.add(hit)
        elif ob_hit.type == 'trash01' or 'trash02' or 'trash03':
            player.life -= 10 # 10
            trash_sound.play()
            hit = hitFX(ob_hit.rect.center, 'player')
            all_sprites.add(hit)

        newObstacle()
        if player.life <= 0: # 죽었을 때
            player.life = 0
        

    # Draw / render
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(metersLeft) + ' m', 20, WIDTH - 60, 10)
    draw_life_bar(screen, 15, 15, player.life)
    pygame.display.flip() # *after* drawing everything, flip the display

pygame.quit()
