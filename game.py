#Kütüphaneler
import pygame
import time


#Screen yaratma
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600



display = pygame.display.set_mode((display_width,display_height)) # screen size
pygame.display.set_caption('Snake')

x1 = display_width/2
y1 = display_height/2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30


font_style = pygame.font.SysFont(None,50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/2, display_height/2])



game_over = False # oyunun bitip bitmediğinin kontrolu
# Oyundan çıkılana kadar devam et
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 >= display_width or x1< 0 or y1 >= display_height:
        game_over=True

    x1 += x1_change
    y1 += y1_change

    display.fill(white)
    pygame.draw.rect(display,black,[x1,y1,snake_block,snake_block])

    pygame.display.update()
    clock.tick(snake_speed)


message('Game Over',red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()