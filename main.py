# pyright: reportMissingImports=false
import pygame as pg

pg.init()
pg.display.set_caption("Snake")
size = width, height = 1200, 800
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
snake = [
    pg.Vector2(600, 400),
    pg.Vector2(550, 400),
    pg.Vector2(500, 400)
]
dt = 0
lastKeyPressed = None
running = True

while running:
    ct = clock.tick(60)  # Limit to 60 FPS
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

    if lastKeyPressed == pg.K_w:
        snake[0].y -= 300 * dt
    if lastKeyPressed == pg.K_s:
        snake[0].y += 300 * dt
    if lastKeyPressed == pg.K_a:
        snake[0].x -= 300 * dt
    if lastKeyPressed == pg.K_d:
        snake[0].x += 300 * dt

    screen.fill("black")  # Clear the screen with black
    for segment in snake:
        pg.draw.rect(screen,(255, 0, 0),(segment.x, segment.y, 50, 50))

    pg.display.flip() 

    if snake[0].x + 5 < 0 or snake[0].x + 45 > width or snake[0].y + 5 < 0 or snake[0].y + 45 > height:
        snake[0] = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        lastKeyPressed = None


pg.quit()