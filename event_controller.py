# Arquivo para guardar funçaõ de controle de eventos do jogo
import pygame as pg

def handle_events(lastKeyPressed, direction):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return None, None, True  # Indica que o jogo deve ser encerrado

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and direction != "down":
                lastKeyPressed = pg.K_w
            if event.key == pg.K_s and direction != "up":
                lastKeyPressed = pg.K_s
            if event.key == pg.K_a and direction != "right":
                lastKeyPressed = pg.K_a
            if event.key == pg.K_d and direction != "left":
                lastKeyPressed = pg.K_d

    return lastKeyPressed, direction, False  # Retorna os valores atualizados e indica que o jogo continua