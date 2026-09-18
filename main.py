import pygame as pg

pg.init()
pg.display.set_caption("Snake")
size = width, height = 1200, 800
grid = 50
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
snake = [
    (12, 8),
    (11, 8),
    (10, 8)
        ]
dt = 0
lastKeyPressed = None
running = True

move_timer = 0
move_interval = 0.1

while running:
    ct = clock.tick(60)
    snake_aux = snake.copy()
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

    move_timer += dt
    print(move_timer)
    dt = ct / 1000.0  # Delta time in seconds

    if move_timer >= move_interval:
        move_timer = 0

        if lastKeyPressed == pg.K_w:
            x, y = snake[0]
            snake[0] = (x, y - 1)

            snake[1] = snake_aux[0]
            snake[2] = snake_aux[1]

        if lastKeyPressed == pg.K_s:
            x, y = snake[0]
            snake[0] = (x, y + 1)
            snake[1] = snake_aux[0]
            snake[2] = snake_aux[1]

        if lastKeyPressed == pg.K_a:
            x, y = snake[0]
            snake[0] = (x - 1, y)
            snake[1] = snake_aux[0]
            snake[2] = snake_aux[1]
            
        if lastKeyPressed == pg.K_d:
            x, y = snake[0]
            snake[0] = (x + 1, y)

            snake[1] = snake_aux[0]
            snake[2] = snake_aux[1]

    screen.fill("black")  # Clear the screen with black
    for segment in snake:
        x, y = segment
        pg.draw.rect(screen,(255, 0, 0),(x * grid, y * grid, grid, grid))

    pg.display.flip() 

    if snake[0][0] < 0 or snake[0][0] >= width // grid or snake[0][1] < 0 or snake[0][1] >= height // grid:
        snake = [
        (width // grid // 2, height // grid // 2),
        (width // grid // 2 - 1, height // grid // 2),
        (width // grid // 2 - 2, height // grid // 2)
        ]
        lastKeyPressed = None


pg.quit()