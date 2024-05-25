# -*- coding:gb18030 -*-

import pgzrun
from pgzero.actor import Actor

from mine_sweeper import Minesweeper

TITLE = "Minesweeper"
# The pixel size of a square is 20 * 20.
TILE_SIZE = 20
WIDTH = 30 * TILE_SIZE
HEIGHT = 30 * TILE_SIZE


class MinesweeperGame:
    def __init__(self):
        # default size, 9 * 9, with 10 mines
        self.MinesweeperGameMap = Minesweeper(9, 9, 10)
        self.MinesweeperGameMap.generate_the_map()


game = MinesweeperGame()
game.MinesweeperGameMap._test_print_the_map()
a = game.MinesweeperGameMap.left_mouse_click_the_map(3, 4)
print("\n")
game.MinesweeperGameMap._test_print_the_map()


maps = []


def init_draw():
    for i in range(game.MinesweeperGameMap.row):
        for j in range(game.MinesweeperGameMap.col):
            mine_square = Actor('unrevealed')
            mine_square.x = i * TILE_SIZE
            mine_square.y = j * TILE_SIZE
            maps.append(mine_square)


def draw():
    init_draw()
    for item in maps:
        item.draw()

print(a)
pgzrun.go()
