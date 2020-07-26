# kütüphaneler
import pygame
import time
import random

pygame.init()

# renkler
white = (255, 255, 255)
yellow = (255,255,102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0, 0, 255)

# ekran boyutu
display_width = 600
display_height = 400

# ekran boyunu set etme ve isimlerdirme
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 30)

def snake(snake_block,snake_list):
    for i in snake_list:
        pygame.draw.rect(display,black,[i[0],i[1],snake_block,snake_block])

# message fonksiyonu
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 3, display_height / 3])

# oyunun döngüsünün fonksiyonu
def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    # yılanın uzunluğu ve uzunluğunun kontrol edildiği liste değişkeni
    snake_list = []
    len_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(blue)
            message("Game Over! \n Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            len_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
