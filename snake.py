# Arquivo para guardar funções com relação a cobra do jogo
import pygame as pg

# Função para mover a cobra
def move_snake(snake, snake_aux, lastKeyPressed, direction):

    # verifica a tecla pressionada e atualiza a posição da cabeça da cobra
    # Define direção da cobra com base na tecla pressionada, evitando que a cobra se mova na direção oposta
    if lastKeyPressed == pg.K_w:
        x, y = snake[0]
        snake[0] = (x, y - 1)
        if len(snake) > 1:
            direction = "up"

    if lastKeyPressed == pg.K_s:
        x, y = snake[0]
        snake[0] = (x, y + 1)
        if len(snake) > 1:
            direction = "down"

    if lastKeyPressed == pg.K_a:
        x, y = snake[0]
        snake[0] = (x - 1, y)
        if len(snake) > 1:
            direction = "left"

    if lastKeyPressed == pg.K_d:
        x, y = snake[0]
        snake[0] = (x + 1, y)
        if len(snake) > 1:
            direction = "right"
    
    # Atualiza posição do corpo da cobra, movendo cada segmento para a posição do segmento anterior
    for i in range(1, len(snake)):
        snake[i] = snake_aux[i - 1]

    return snake, direction

def snake_collision(snake, width, height, grid):
    # Verifica se a cabeça da cobra colidiu com as bordas da tela ou com seu próprio corpo
    if snake[0][0] < 0 or snake[0][0] >= width // grid or snake[0][1] < 0 or snake[0][1] >= height // grid or snake[0] in snake[1:]:
        return True
    return False

def draw_snake(screen, snake, grid):
    # Desenha cada segmento da cobra na tela
    for segment in snake:
        x, y = segment
        pg.draw.rect(screen, (0, 255, 0), (x * grid, y * grid, grid, grid))