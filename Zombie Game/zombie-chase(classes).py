import pygame
import os
import sys


ALPHA = (0, 255, 0)

class Window:
    def __init__(self):
        self.width = 512
        self.height = 512

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speedmult = 1.0
        self.health = 100
        self.damagemult = 1 - self.speedmult
        self.speed = 10
        self.posx = 0
        self.posy = 0
        self.frame = 0
        self.ani = 10
        self.kidleimages = []
        for i in range(19):
            img = pygame.image.load(os.path.join('images','survivor','knife','idle','survivor-idle_knife_' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.kidleimages.append(img)
            self.kidleimages[0]
            self.rect = self.image.get_rect()

    def control(self,x,y):
        self.posx += x
        self.posy += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        if self.posx < 0:    
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.kidleimages[self.frame // self.ani], True, False)
            print(self.posx)
        if self.posx > 0:    
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = self.kidleimages[self.frame // self.ani]
            print(self.posy)

    def __init__(settings):
        settings.turnrate = 15

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


WindowMain = Window()
player = Player()
player.posx = 150
player.posy = 150
player.speed = 10

player_list = pygame.sprite.Group()
player_list.add(player)

pygame.init()
window = pygame.display.set_mode((WindowMain.width, WindowMain.height))
pygame.display.set_caption("Zombie Chase")

colours = {
    "White" : (255,255,255),
    "Red" : (255,0,0),
    "Blue" : (0,0,255),
    "Green" : (0,255,0),
    "Black" : (0,0,0)
}


clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
fps = 30
pygame.init()

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WindowMain.width/3, WindowMain.height/3])


def maingame():
    exit_game = False
    game_over = False
    while exit_game == False:
        while game_over == True:
            window.fill(colours["White"])
            message("You Lost! Press Q-Quit or C-Play Again", colours["Red"])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        exit_game = False
                    elif event.key == pygame.K_c:
                        maingame()
                    elif event.key == pygame.K_ESCAPE:
                        exit_game = True
                if event.type == pygame.QUIT:
                    exit_game = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.control(player.speed,0)
                if event.key == pygame.K_RIGHT:
                    player.control(-player.speed,0)
                if event.key == pygame.K_UP:
                    player.control(0,player.speed)
                if event.key == pygame.K_DOWN:
                    player.control(0,-player.speed)
            if event.type == pygame.QUIT:
                exit_game = True
        
        clock.tick(fps)
        player.update()
        player_list.draw(world)
    
    
    pygame.quit()
    quit()

maingame()

