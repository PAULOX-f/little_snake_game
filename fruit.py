# Arquivo para guardar funções com relação a frutas do jogo
import pygame as pg
import random as rd

# Gera uma fruta em uma posição aleatória que não esteja ocupada pela cobra
def generate_fruit(snake, qtd_colunas, qtd_linhas, isFruit, fruit):
    # Enquanto isFruit = False gera uma nova fruta em uma posição aleatória
    while not isFruit:
        x_fruit = rd.randrange(qtd_colunas)
        y_fruit = rd.randrange(qtd_linhas)

        fruit = (x_fruit, y_fruit)

        # Verifica se a fruta gerada não está ocupada pela cobra
        if fruit not in snake:
            isFruit = True
            return fruit, isFruit
    # Se isFruit = True, retorna a fruta existente e o estado de isFruit
    return fruit, isFruit