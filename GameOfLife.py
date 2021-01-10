# Импорты
import time
import random
import pygame as p
from pygame.locals import *

# RGB const
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# System list
SYSTEM = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


class GameOfLife:

    def __init__(self, window_width, window_height):
        self.root = p.display.set_mode((window_width, window_height))
        self.cells = [[random.choice((0, 1)) for j in range(self.root.get_width() // 20)] for i in range(self.root.get_height() // 20)]

    def near(self, pos: list, system=SYSTEM):
        """
        This method returns number of neighbours
        """
        count = 0
        for i in system:
            if self.cells[(pos[0] + i[0]) % len(self.cells)][(pos[1] + i[1]) % len(self.cells[0])]:
                count += 1
        return count

    def run(self):
        while True:
            # Заполняем экран белым цветом
            self.root.fill(WHITE)

            # Рисуем сетку
            for i in range(0, self.root.get_height() // 20):
                p.draw.line(self.root, BLACK, (0, i * 20), (self.root.get_width(), i * 20))
            for j in range(0, self.root.get_width() // 20):
                p.draw.line(self.root, BLACK, (j * 20, 0), (j * 20, self.root.get_height()))
           # Нужно чтобы виндовс не думал что программа "не отвечает"
            for i in p.event.get():
                if i.type == QUIT:
                    quit()
            # Проходимся по всем клеткам

            for i in range(0, len(self.cells)):
                for j in range(0, len(self.cells[i])):
                    p.draw.rect(self.root, (255 * self.cells[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])
            # Обновляем экран
            p.display.update()
            self.cells2 = [[0 for j in range(len(self.cells[0]))] for i in range(len(self.cells))]
            for i in range(len(self.cells)):
                for j in range(len(self.cells[0])):
                    if self.cells[i][j]:
                        if self.near([i, j]) not in (2, 3):
                            self.cells2[i][j] = 0
                            continue
                        self.cells2[i][j] = 1
                        continue
                    if self.near([i, j]) == 3:
                        self.cells2[i][j] = 1
                        continue
                    self.cells2[i][j] = 0
            self.cells = self.cells2