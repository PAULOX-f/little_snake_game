# pyright: reportMissingImports=false
import pygame as pg

pg.init()
pg.display.set_caption("Snake")
size = width, height = 1200, 800
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
lastKeyPressed = None
running = True

while running:
    clock.tick(60)  # Limit to 60 FPS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0  # Delta time in seconds

    if lastKeyPressed == pg.K_w:
        player_pos.y -= 300 * dt
    if lastKeyPressed == pg.K_s:
        player_pos.y += 300 * dt
    if lastKeyPressed == pg.K_a:
        player_pos.x -= 300 * dt
    if lastKeyPressed == pg.K_d:
        player_pos.x += 300 * dt

    screen.fill("black")  # Clear the screen with black
    pg.draw.rect(screen, (255, 0, 0), (player_pos.x, player_pos.y, 50, 50))

    pg.display.flip() 

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        lastKeyPressed = pg.K_w
    if keys[pg.K_s]:
        lastKeyPressed = pg.K_s 
    if keys[pg.K_a]:
        lastKeyPressed = pg.K_a
    if keys[pg.K_d]:
        lastKeyPressed = pg.K_d


pg.quit()