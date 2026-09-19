import pygame as pg
import random as rd

size = width, height = 1200, 800
grid = 50
qtd_colunas = width // grid
qtd_linhas = height // grid

pg.init()
pg.display.set_caption("Snake")
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
running = True

snake = [
    (12, 8)
        ]

dt = 0

lastKeyPressed = None
isFruit = False

move_timer = 0
move_interval = 0.1

while running:

    while isFruit == False:
        x_fruit = rd.randrange(qtd_colunas)
        y_fruit = rd.randrange(qtd_linhas)

        fruit = (x_fruit, y_fruit)

        if fruit not in snake:
            isFruit = True
    
    ct = clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                lastKeyPressed = pg.K_w
            if event.key == pg.K_s: 
                lastKeyPressed = pg.K_s
            if event.key == pg.K_a:
                lastKeyPressed = pg.K_a
            if event.key == pg.K_d:
                lastKeyPressed = pg.K_d

    dt = ct / 1000.0  # Delta time in seconds
    move_timer += dt

    if move_timer >= move_interval:
        snake_aux = snake.copy()
        tail = snake_aux[-1]

        if lastKeyPressed == pg.K_w:
            x, y = snake[0]
            snake[0] = (x, y - 1)

        if lastKeyPressed == pg.K_s:
            x, y = snake[0]
            snake[0] = (x, y + 1)

        if lastKeyPressed == pg.K_a:
            x, y = snake[0]
            snake[0] = (x - 1, y)
            
        if lastKeyPressed == pg.K_d:
            x, y = snake[0]
            snake[0] = (x + 1, y)


        for i in range(1, len(snake)):
            snake[i] = snake_aux[i - 1]

        move_timer = 0

        if snake[0] == fruit:
                isFruit = False
                snake.append(tail)

    screen.fill("black")  # Clear the screen with black
    if isFruit == True:
            pg.draw.rect(screen, (255, 0, 0), (fruit[0] * grid, fruit[1] * grid, grid, grid))
    for segment in snake:
        x, y = segment
        pg.draw.rect(screen,(0, 255, 0),(x * grid, y * grid, grid, grid))

    pg.display.flip() 

    if snake[0][0] < 0 or snake[0][0] >= width // grid or snake[0][1] < 0 or snake[0][1] >= height // grid or snake[0] in snake[1:]:
        snake = [
        (width // grid // 2, height // grid // 2),
        ]
        lastKeyPressed = None
        isFruit = False


pg.quit()