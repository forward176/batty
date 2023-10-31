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

def collision(LEFT, TOP, RIGHT, BOTTOM):
    d = dist(LEFT, TOP, x_circle, y_circle)
    if d <= radius_circle:
        return 1, 1    
    d = dist(RIGHT, TOP, x_circle, y_circle)
    if d <= radius_circle:    
        return 1, 1
    d = dist(LEFT, BOTTOM, x_circle, y_circle)
    if d <= radius_circle: 
        return 1, 1
    d = dist(RIGHT, BOTTOM, x_circle, y_circle)
    if d <= radius_circle: 
        return 1, 1
    # левая стенка
    if 0 < LEFT - x_circle <= radius_circle and TOP <= y_circle <= BOTTOM:
        return 1, 0
    # правая стенка
    if 0 < x_circle - RIGHT <= radius_circle and TOP <= y_circle <= BOTTOM:
        return 1, 0
    # верхняя стенка
    if 0 < TOP - y_circle <= radius_circle and LEFT <= x_circle <= RIGHT:
        return 0, 1
    # нижняя стенка
    if 0 < y_circle - BOTTOM <= radius_circle and LEFT <= x_circle <= RIGHT:
        return 0, 1
    return 0, 0
 
def dist(X1, Y1, X2, Y2):
    x = X2 - X1
    y = Y2 - Y1
    c = (x**2 + y**2)**0.5
    return c

FPS = 120
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


def set_start():
    global x_circle, y_circle, v_x, v_y
    x_circle = 200
    y_circle = 500
    v_x = -3
    v_y = -3


set_start()

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
            if event.key == pygame.K_TAB:
                set_start()
                blocks = create_blocks()
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
        v_y = 0
        v_x = 0
    
    # платформа
    x_platform += speed_platform
    if x_platform >= SCREEN_WIDTH - platform_img.get_width() // 2:
        x_platform = SCREEN_WIDTH - platform_img.get_width() // 2
    if x_platform <= platform_img.get_width() // 2:
        x_platform = platform_img.get_width() // 2

    # шарик и платформа (столкновение)
    # TODO Дописать условие сталкновения с платформой (бока + не проваливаться + разные углы)
    higher_than_platform = x_platform - platform_img.get_width() // 2 <= x_circle <= x_platform + platform_img.get_width() // 2
    if 0 <= y_platform - platform_img.get_height() - y_circle <= radius_circle and higher_than_platform:
        v_y = - v_y
        y_circle += v_y
    # qx, qy = collision(
    #         x_platform - platform_img.get_width() // 2, 
    #         y_platform - platform_img.get_height() // 2, 
    #         x_platform + platform_img.get_width() // 2, 
    #         y_platform + platform_img.get_height() // 2
    #     )
    # if qx == 1:
    #     v_x = -v_x        
    # if qy == 1:
    #     v_y = -v_y
    # шарик и блоки (столкновение)
    for x_block, y_block in blocks:
        qx, qy = collision(x_block, y_block, x_block + block_img.get_width(), y_block + block_img.get_height())
        if qx == qy == 0:
            continue
        if qx == 1:
            v_x = -v_x
        if qy == 1:
            v_y = -v_y
        blocks.remove((x_block, y_block))
        break

    screen.fill(BLACK)
    screen.blit(platform_img, platform_img.get_rect(center=(x_platform, y_platform)))
    
    show_blocks()
    pygame.draw.circle(screen, RED, (x_circle,y_circle), radius = radius_circle)
    pygame.display.update()
