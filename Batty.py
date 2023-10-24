import pygame


def create_blocks():
    blocks = []
    y_block = 75
    for j in range(3):
        x_block = 225
        for i in range(5):
            blocks.append((x_block, y_block))
            x_block += 125
        y_block += 75
    return blocks


def show_blocks():
    for x, y in blocks:
        screen.blit(block_img, block_img.get_rect(topleft=(x, y)))

def collision(x_block, y_block):
    d = dist(x_block, y_block, x_circle, y_circle)
    if d <= radius_circle:
        return 1, 1    
    d = dist(x_block + block_img.get_width(), y_block, x_circle, y_circle)
    if d <= radius_circle:    
        return 1, 1
    d = dist(x_block, y_block + block_img.get_height(), x_circle, y_circle)
    if d <= radius_circle: 
        return 1, 1
    d = dist(x_block + block_img.get_width(), y_block + block_img.get_height(), x_circle, y_circle)
    if d <= radius_circle: 
        return 1, 1
    # левая стенка
    if 0 < x_block - x_circle <= radius_circle and y_block <= y_circle <= y_block + block_img.get_height():
        return 1, 0
    # правая стенка
    # верхняя стенка
    # нижняя стенка


def dist(X1, Y1, X2, Y2):
    x = X2 - X1
    y = Y2 - Y1
    c = (x**2 + y**2)**0.5
    return c

FPS = 60
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

platform_img = pygame.image.load('images\\platform.png').convert()
platform_img = pygame.transform.scale(platform_img, (200, 40))

block_img = pygame.image.load('images\\block.png').convert()
block_img = pygame.transform.scale(block_img, (100, 50))
blocks = create_blocks()
radius_circle = 15

x_platform = SCREEN_WIDTH // 2
y_platform = SCREEN_HEIGHT // 4 * 3

speed_platform = 0

x_circle = 200
y_circle = 500

v_x = -5
v_y = -5

while True:
    clock.tick(FPS)
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_platform -= 6
            if event.key == pygame.K_RIGHT:
                speed_platform += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_platform += 6
            if event.key == pygame.K_RIGHT:
                speed_platform -= 6

    # шарик
    x_circle += v_x
    y_circle += v_y
    if x_circle >= SCREEN_WIDTH - radius_circle:
        x_circle = SCREEN_WIDTH - radius_circle
        v_x = -v_x
    if x_circle <= radius_circle:
        x_circle = radius_circle
        v_x = -v_x
    if y_circle <= radius_circle:
        y_circle = radius_circle
        v_y = -v_y
    if y_circle > SCREEN_HEIGHT - radius_circle:
        y_circle = SCREEN_HEIGHT - radius_circle
        x_circle = SCREEN_WIDTH // 2
    
    # платформа
    x_platform += speed_platform
    if x_platform >= SCREEN_WIDTH - platform_img.get_width() // 2:
        x_platform = SCREEN_WIDTH - platform_img.get_width() // 2
    if x_platform <= platform_img.get_width() // 2:
        x_platform = platform_img.get_width() // 2

    # шарик и платформа (столкновение)
    # TODO Дописать условие сталкновения с платформой (бока + не проваливаться + разные углы)
    higher_than_platform = x_platform - platform_img.get_width() // 2 <= x_circle <= x_platform + platform_img.get_width() // 2
    if 0 <= y_platform - y_circle <= radius_circle and higher_than_platform:
        v_y = - v_y
        y_circle += v_y

    # шарик и блоки (столкновение)
    

    screen.fill(BLACK)
    screen.blit(platform_img, platform_img.get_rect(center=(x_platform, y_platform)))
    
    show_blocks()
    pygame.draw.circle(screen, RED, (x_circle,y_circle), radius = radius_circle)
    pygame.display.update()
