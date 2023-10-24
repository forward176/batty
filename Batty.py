import pygame

# TODO git + github 

FPS = 60
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

# def blocks():
#     block_img = pygame.image.load('images\\block.png').convert()
#     block_img = pygame.transform.scale(block_img, (100, 50))
    
#     x1_block = SCREEN_WIDTH // 4
#     y1_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    
#     x2_block = SCREEN_WIDTH // 3
#     y2_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    
#     x2_block = SCREEN_WIDTH // 2
#     y2_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    
#     x2_block = SCREEN_WIDTH // 1
#     y2_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)


def func():
    x_block = 225
    y_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    x1_block = x_block + 125
    y1_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)  
    x2_block = x1_block + 125
    y2_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)  
    x3_block = x2_block + 125
    y3_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    x4_block = x3_block + 125
    y4_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 150)
    
    x5_block = 225
    y5_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 225)
    x6_block = x_block + 125
    y6_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 225)  
    x7_block = x1_block + 125
    y7_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 225)  
    x8_block = x2_block + 125
    y8_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 225)
    x9_block = x3_block + 125
    y9_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 225)
    
    x10_block = 225
    y10_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 75)
    x11_block = x_block + 125
    y11_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 75)  
    x12_block = x1_block + 125
    y12_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 75)  
    x13_block = x2_block + 125
    y13_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 75)
    x14_block = x3_block + 125
    y14_block = SCREEN_HEIGHT - (SCREEN_HEIGHT - 75)

    screen.blit(block_img, block_img.get_rect(center=(x_block, y_block)))
    screen.blit(block_img, block_img.get_rect(center=(x1_block, y1_block)))
    screen.blit(block_img, block_img.get_rect(center=(x2_block, y2_block)))
    screen.blit(block_img, block_img.get_rect(center=(x3_block, y3_block)))
    screen.blit(block_img, block_img.get_rect(center=(x4_block, y4_block)))
    
    screen.blit(block_img, block_img.get_rect(center=(x5_block, y5_block)))
    screen.blit(block_img, block_img.get_rect(center=(x6_block, y6_block)))
    screen.blit(block_img, block_img.get_rect(center=(x7_block, y7_block)))
    screen.blit(block_img, block_img.get_rect(center=(x8_block, y8_block)))
    screen.blit(block_img, block_img.get_rect(center=(x9_block, y9_block)))

    screen.blit(block_img, block_img.get_rect(center=(x10_block, y10_block)))
    screen.blit(block_img, block_img.get_rect(center=(x11_block, y11_block)))
    screen.blit(block_img, block_img.get_rect(center=(x13_block, y13_block)))
    screen.blit(block_img, block_img.get_rect(center=(x14_block, y14_block)))
    screen.blit(block_img, block_img.get_rect(center=(x12_block, y12_block)))


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

platform_img = pygame.image.load('images\\platform.png').convert()
platform_img = pygame.transform.scale(platform_img, (200, 40))


block_img = pygame.image.load('images\\block.png').convert()
block_img = pygame.transform.scale(block_img, (100, 50))



# font=pygame.freetype.SysFont(None, 30)
# font.origin=True

# main_font = pygame.font.SysFont('serif', 24)

# start_text = main_font.render("Новая игра", True, WHITE)

# start_ticks = pygame.time.get_ticks()
# ticks=pygame.time.get_ticks() - start_ticks


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
    higher_than_platform = x_platform - platform_img.get_width() // 2 <= x_circle <= x_platform + platform_img.get_width() // 2
    if 0 <= y_platform - y_circle <= radius_circle and higher_than_platform:
        v_y = - v_y
        y_circle += v_y



    screen.fill(BLACK)
    screen.blit(platform_img, platform_img.get_rect(center=(x_platform, y_platform)))
    # screen.blit(block_img, block_img.get_rect(center=(x_block, y_block)))
    func()
    pygame.draw.circle(screen, RED, (x_circle,y_circle), radius = radius_circle)
    pygame.display.update()
