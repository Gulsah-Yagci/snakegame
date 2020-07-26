#Kütüphane
import pygame


#Screen yaratma

pygame.init()
display = pygame.display.set_mode((400,300)) # screen size 400x300
pygame.display.update() # animasyonlarda hareketi sağlamak için sürekli frame update edilir
pygame.display.set_caption('Snake')
game_over = False # oyunun bitip bitmediğinin kontrolu

# Oyundan çıkılana kadar devam et
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

pygame.quit()
quit()