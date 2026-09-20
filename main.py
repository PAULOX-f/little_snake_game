import pygame as pg
import random as rd
import snake as snk
import fruit as frt
import event_controller as evc

size = width, height = 1200, 800
grid = 50
qtd_colunas = width // grid
qtd_linhas = height // grid
centro_x = qtd_colunas // 2
centro_y = qtd_linhas // 2

pg.init()
pg.font.init()
pg.display.set_caption("Snake")
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
running = True

font = pg.font.SysFont("Arial", 30, bold=True)

score = 0
snake = [
    (centro_x, centro_y)
        ]
fruit = None

dt = 0

lastKeyPressed = None
isFruit = False
direction = None

move_timer = 0
move_interval = 0.15

while running:

    lastKeyPressed, direction, should_quit = evc.handle_events(lastKeyPressed, direction)
    if should_quit:
        running = False
    
    fruit, isFruit = frt.generate_fruit(snake, qtd_colunas, qtd_linhas, isFruit, fruit)
    
    ct = clock.tick(60)

    dt = ct / 1000.0  # Delta time in seconds
    move_timer += dt

    if move_timer >= move_interval:
        snake_aux = snake.copy()
        tail = snake_aux[-1]

        snake, direction = snk.move_snake(snake, snake_aux, lastKeyPressed, direction)

        move_timer = 0

        if snake[0] == fruit:
                isFruit = False
                snake.append(tail)
                score += 1

    screen.fill("black")  # Clear the screen with black
    if isFruit:
            pg.draw.rect(screen, (255, 0, 0), (fruit[0] * grid, fruit[1] * grid, grid, grid))
    
    snk.draw_snake(screen, snake, grid)

    font_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(font_surface, (10, 10))

    pg.display.flip() 

    if snk.snake_collision(snake, width, height, grid):
        snake = [(centro_x, centro_y)]
        lastKeyPressed = None
        isFruit = False
        direction = None
        score = 0


pg.quit()