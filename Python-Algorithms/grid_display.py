import pygame
def main(maze, window_w, window_h, grid_r, grid_c):


    pygame.init()
    window = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption("A* Path Finding Algorithm")

    class grid:
        w = 20
        h = 20
        m = 5
        column = len(maze[1])
        row = len(maze)

    class block:
        w = 20
        h = 20
        m = 5

    exit_window = False

    colours = {
        "White" : (255,255,255),
        "Red" : (255,0,0),
        "Blue" : (0,0,255),
        "Green" : (0,255,0),
        "Black" : (0,0,0)
    }

    block.x = block.m
    block.y = block.m
    for i in range(grid.row):
        for j in range(grid.column):
            if maze[i][j] == 1:
                colour = colours["White"]
            else:
                colour = colours["Black"]
            pygame.draw.rect(window, colour, [block.x, block.y, block.w, block.h])
            block.x += block.w + block.m
        block.y += block.h + block.m
        block.x = block.m
        pygame.display.update()

    while exit_window == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_window = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_window = True
