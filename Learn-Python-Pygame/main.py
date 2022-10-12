import time
import pygame
import random

pygame.init()
dis_w,dis_h = 800,600
dis=pygame.display.set_mode((dis_w,dis_h))
pygame.display.set_caption("Test Snake Game")

colours = {
    "White" : (255,255,255),
    "Red" : (255,0,0),
    "Blue" : (0,0,255),
    "Green" : (0,255,0),
    "Black" : (0,0,0)
}

g_size = 20

s_colour = (0,0,255)
s_size = 18
s_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

def snake(s_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colours["Green"], [x[0], x[1], s_block, s_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_w/3, dis_h/3])

def gameLoop():
    game_over = False
    game_close = False

    x_snake = dis_w/2
    y_snake = dis_h/2

    x_snake_change = 0
    y_snake_change = 0

    x_food = round(random.randrange(0, dis_w - g_size) / g_size) * g_size
    y_food = round(random.randrange(0, dis_h - g_size) / g_size) * g_size

    snake_List = []
    s_length = 1

    while not game_over:
    
        while game_close == True:
            dis.fill(colours["White"])
            message("You Lost! Press Q-Quit or C-Play Again", colours["Red"])
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()
                    elif event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_snake_change = -g_size
                    y_snake_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_snake_change = g_size
                    y_snake_change = 0
                elif event.key == pygame.K_UP:
                    x_snake_change = 0
                    y_snake_change = -g_size
                elif event.key == pygame.K_DOWN:
                    x_snake_change = 0
                    y_snake_change = g_size
                elif event.key == pygame.K_ESCAPE:
                    game_over = False
                    game_close = True


        if x_snake >= dis_w or x_snake < 0 or y_snake >= dis_h or y_snake < 0:
            game_close = True

        x_snake += x_snake_change
        y_snake += y_snake_change
        dis.fill(colours["Black"])

        pygame.draw.rect(dis,colours["Red"],[x_food,y_food,s_size,s_size])
        snake_Head = []
        snake_Head.append(x_snake)
        snake_Head.append(y_snake)
        snake_List.append(snake_Head)
        if len(snake_List) > s_length:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(s_size, snake_List)

        pygame.display.update()

        if x_snake == x_food and y_snake == y_food:
            x_food = round(random.randrange(0, dis_w - g_size) / g_size) * g_size
            y_food = round(random.randrange(0, dis_h - g_size) / g_size) * g_size
            s_length += 1

        clock.tick(s_speed)

    pygame.quit()
    quit()

gameLoop()