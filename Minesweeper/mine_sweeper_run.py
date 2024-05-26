# -*- coding:gb18030 -*-

import pgzrun
# from pgzero.constants import mouse

from mine_sweeper import Minesweeper
from mine_sweeper_resource import actor_path_dict

TITLE = "Minesweeper"
# The pixel size of a square is 20 * 20.
TILE_SIZE = 20
WIDTH = 16 * TILE_SIZE
HEIGHT = 16 * TILE_SIZE


class MinesweeperGame:
    def __init__(self):
        # default size, 9 * 9, with 10 mines
        self.MinesweeperGameMap = Minesweeper(9, 9, 10)
        self.MinesweeperGameMap.generate_the_map()
        self.gameStatus = "begin"  # running, win, lose
        self.maps = []
        self.style = "normal_style"

    def draw(self):
        if self.gameStatus == "begin":
            self._init_maps()
            self.gameStatus = "running"

        for item in self.maps:
            item.draw()

    def click(self, x, y):
        change_square = self.MinesweeperGameMap.left_mouse_click_the_map(x, y)
        if change_square is None:
            return
        if "mine" in change_square:
            print(change_square["mine"])
            # game over
            return

        for item in change_square:
            for square in change_square[item]:
                self.maps[square[0] * self.MinesweeperGameMap.col + square[1]].image = (
                    self._get_actor_with_style(
                        self.MinesweeperGameMap.map[square[0]][square[1]]))

    ''' We will define private function below this line. '''
    """
    *Description: Get the full path of actor.
    """

    def _get_actor_with_style(self, minesweeper_state):
        actor_path = actor_path_dict[minesweeper_state]
        return self.style + "//" + actor_path

    def _init_maps(self):
        for i in range(self.MinesweeperGameMap.row):
            for j in range(self.MinesweeperGameMap.col):
                mine_square = Actor(self._get_actor_with_style(self.MinesweeperGameMap.map[i][j]))
                mine_square.x = i * TILE_SIZE + 30
                mine_square.y = j * TILE_SIZE + 40
                self.maps.append(mine_square)


game = MinesweeperGame()


def draw():
    screen.fill((255, 255, 255))
    game.draw()


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        click_i = (pos[0] - 30 + 10) // TILE_SIZE
        click_j = (pos[1] - 40 + 10) // TILE_SIZE
        print(pos)
        game.click(click_i, click_j)


pgzrun.go()
