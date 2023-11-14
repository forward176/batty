import pygame


def create_blocks():
    global block_img, space_between_blocks
    blocks = []
    rows = 2 + level
    while FIELD_HEIGHT - 2 * space_between_blocks < rows * (block_img.get_height() + space_between_blocks):
        block_img = pygame.transform.scale(block_img, (block_img.get_width() * 0.9, block_img.get_height() * 0.9))
        space_between_blocks *= 0.9
    space_between_blocks = int(space_between_blocks)
    colums = (SCREEN_WIDTH - space_between_blocks) // (block_img.get_width() + space_between_blocks)
    border_space = (SCREEN_WIDTH - (colums * (block_img.get_width() + space_between_blocks) - space_between_blocks)) // 2
    
    y_block = border_space
    for j in range(rows):
        x_block = border_space
        for i in range(colums):
            blocks.append((x_block, y_block))
            x_block += (block_img.get_width() + space_between_blocks)
        y_block += (block_img.get_height() + space_between_blocks)
    return blocks


def show_blocks():
    for x, y in blocks:
        screen.blit(block_img, block_img.get_rect(topleft=(x, y)))

def collision(LEFT, TOP, RIGHT, BOTTOM): # -1 -- левая, верхняя
    d = dist(LEFT, TOP, x_circle, y_circle)
    if d <= radius_circle:
        return -1, -1    
    d = dist(RIGHT, TOP, x_circle, y_circle)
    if d <= radius_circle:    
        return 1, -1
    d = dist(LEFT, BOTTOM, x_circle, y_circle)
    if d <= radius_circle: 
        return -1, 1
    d = dist(RIGHT, BOTTOM, x_circle, y_circle)
    if d <= radius_circle: 
        return 1, 1
    # левая стенка
    if 0 < LEFT - x_circle <= radius_circle and TOP <= y_circle <= BOTTOM:
        return -1, 0
    # правая стенка
    if 0 < x_circle - RIGHT <= radius_circle and TOP <= y_circle <= BOTTOM:
        return 1, 0
    # верхняя стенка
    if 0 < TOP - y_circle <= radius_circle and LEFT <= x_circle <= RIGHT:
        return 0, -1
    # нижняя стенка
    if 0 < y_circle - BOTTOM <= radius_circle and LEFT <= x_circle <= RIGHT:
        return 0, 1
    return 0, 0
 
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

level = 1

platform_img = pygame.image.load('images\\platform.png').convert()
platform_img = pygame.transform.scale(platform_img, (200, 28))

block_img = pygame.image.load('images\\block.png').convert()
block_img = pygame.transform.scale(block_img, (100, 50))
radius_circle = 12
space_between_blocks = 25
FIELD_HEIGHT = SCREEN_HEIGHT // 4 * 3

speed_platform = 0


def set_start():
    global x_circle, y_circle, v_x, v_y, x_platform, y_platform, blocks, freeze_flag  
    x_platform = SCREEN_WIDTH // 2
    y_platform = FIELD_HEIGHT + 100
    x_circle = x_platform
    y_circle = y_platform - radius_circle - platform_img.get_height() // 2
    v_x = -3
    v_y = -3
    blocks = create_blocks()
    screen.fill(BLACK)
    show_blocks()
    freeze_flag = False


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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_platform += 6
            if event.key == pygame.K_RIGHT:
                speed_platform -= 6
            
    pygame.draw.circle(screen, BLACK, (x_circle,y_circle), radius = radius_circle)
    pygame.draw.rect(screen,BLACK, platform_img.get_rect(center=(x_platform, y_platform)))

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
        # x_circle = SCREEN_WIDTH // 2
        v_y = 0
        v_x = 0
    
    # платформа
    x_platform += speed_platform
    if x_platform >= SCREEN_WIDTH - platform_img.get_width() // 2:
        x_platform = SCREEN_WIDTH - platform_img.get_width() // 2
    if x_platform <= platform_img.get_width() // 2:
        x_platform = platform_img.get_width() // 2

    # шарик и платформа (столкновение)
    qx, qy = collision(
            x_platform - platform_img.get_width() // 2, 
            y_platform - platform_img.get_height() // 2, 
            x_platform + platform_img.get_width() // 2, 
            y_platform + platform_img.get_height() // 2
        )
    # -1 -- левая, верхняя

    rebound_coefficient = 1
    if qx == 1 and v_x < 0:
        v_x = -v_x  
        x_circle += v_x * rebound_coefficient
    elif qx == 1 and v_x > 0:
        x_circle += v_x * rebound_coefficient
    elif qx == -1 and v_x > 0:
        v_x = -v_x
        x_circle += v_x * rebound_coefficient
    elif qx == -1 and v_x < 0:
        x_circle += v_x * rebound_coefficient

    if qy == 1 and v_y < 0:
        v_y = -v_y  
        y_circle += v_y * rebound_coefficient
    elif qy == 1 and v_y > 0:
        y_circle += v_y * rebound_coefficient
    elif qy == -1 and v_y > 0:
        v_y = -v_y
        y_circle += v_y * rebound_coefficient
    elif qy == -1 and v_y < 0:
        y_circle += v_y * rebound_coefficient

    # шарик и блоки (столкновение)
    # TODO изменить логику столкновений с блоками, чтобы без цикла искать столкновение
    for x_block, y_block in blocks:
        qx, qy = collision(x_block, y_block, x_block + block_img.get_width(), y_block + block_img.get_height())
        if qx == qy == 0:
            continue
        if qx != 0:
            v_x = -v_x
        if qy != 0:
            v_y = -v_y
        blocks.remove((x_block, y_block))
        pygame.draw.rect(screen, BLACK, (x_block, y_block, block_img.get_width(), block_img.get_height()))
        break
    if not blocks:
        level += 1
        set_start()
        freeze_flag = True
    
    screen.blit(platform_img, platform_img.get_rect(center=(x_platform, y_platform)))
    pygame.draw.circle(screen, RED, (x_circle,y_circle), radius = radius_circle)
    pygame.display.update()

    if freeze_flag:
        pygame.time.delay(3000)
        freeze_flag = False
