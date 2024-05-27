# -*- coding:gb18030 -*-
import threading
import time
import pgzrun

from mine_sweeper import State
from mine_sweeper import state_can_be_right_click
from mine_sweeper import Minesweeper
from mine_sweeper_resource import actor_path_dict, level_choice, level_set_row_col_mine
from mine_sweeper_constants import Constants

TITLE = "Minesweeper"
TILE_SIZE = Constants.TILE_SIZE
WIDTH = Constants.SCREEN_WIDTH
HEIGHT = Constants.SCREEN_HEIGHT


class MinesweeperGame:
    def __init__(self):
        # default size, 9 * 9, with 10 mines
        self.MinesweeperGameMap = Minesweeper(9, 9, 10)
        self.MinesweeperGameMap.generate_the_map()
        self.gameStatus = "begin"  # running, win, lose
        self.maps = []
        self.style = "normal_style"
        self.clickTimes = 0
        self.time_clock = 0
        self.stop_clock = False

    def draw(self):
        if self.gameStatus == "begin":
            for level in level_choice:
                level.draw()
        else:
            for item in self.maps:
                item.draw()
            if self.gameStatus == "running":
                screen.draw.text(str(self.time_clock), (100, 100), fontsize=25, color="white")
            elif self.gameStatus == "lose":
                pass
            elif self.gameStatus == "win":
                pass

    def start_clock(self):
        def run_clock():
            while self.gameStatus == "running" and self.stop_clock is False:
                time.sleep(1)
                self.time_clock += 1

        clock_thread = threading.Thread(target=run_clock)
        clock_thread.daemon = True
        clock_thread.start()

    def left_click_square(self, x, y):
        # left mouse click square when the game is running
        if self.gameStatus != "running" or not self._check_whether_in_the_map(x, y):
            return

        self._first_click(x, y)
        self._left_click_square_details(x, y)

    def level_select(self, pos):
        for item in level_choice:
            if item.collidepoint(pos):
                if item.image not in level_set_row_col_mine:
                    continue
                level_setting = level_set_row_col_mine[item.image]
                self.MinesweeperGameMap.change_the_map(level_setting[0], level_setting[1], level_setting[2])
                self._init_game()
                self.gameStatus = "running"
                break

    def right_click_square(self, x, y):
        if self.gameStatus != "running" or not self._check_whether_in_the_map(x, y):
            return

        actor = self.maps[x * self.MinesweeperGameMap.col + y]
        if state_can_be_right_click(self.MinesweeperGameMap.map[x][y]):
            if actor.image == self._get_actor_with_style("flag"):
                actor.image = self._get_actor_with_style("sign")
            elif actor.image == self._get_actor_with_style("sign"):
                actor.image = self._get_actor_with_state(
                    self.MinesweeperGameMap.map[x][y]
                )
            elif actor.image != self._get_actor_with_style("flag"):
                actor.image = self._get_actor_with_style("flag")

    ''' We will define private function below this line. '''
    """
    *Description: Get the full path of actor.
    """

    def _get_actor_with_state(self, minesweeper_state):
        actor_path = actor_path_dict[minesweeper_state]
        return self._get_actor_with_style(actor_path)

    def _get_actor_with_style(self, style):
        return self.style + "//" + style

    def _init_maps(self):
        self.maps = []
        for i in range(self.MinesweeperGameMap.row):
            for j in range(self.MinesweeperGameMap.col):
                mine_square = Actor(self._get_actor_with_state(self.MinesweeperGameMap.map[i][j]))
                mine_square.x = j * TILE_SIZE + Constants.FIRST_SQUARE_START_X
                mine_square.y = i * TILE_SIZE + Constants.FIRST_SQUARE_START_Y
                self.maps.append(mine_square)

    def _init_game(self):
        self.gameStatus = "begin"
        self._init_maps()
        self.clickTimes = 0
        self.time_clock = 0
        self.stop_clock = False

    # change_square: MinesweeperGameMap.left_mouse_click_the_map
    def _click_mine(self, change_square):
        mine = change_square["mine"][0]
        self.maps[mine[0] * self.MinesweeperGameMap.col + mine[1]].image = (
            self._get_actor_with_state(
                self.MinesweeperGameMap.map[mine[0]][mine[1]]
            )
        )
        self.gameStatus = "lose"

    def _click_empty_square(self, change_square):
        for item in change_square:
            for square in change_square[item]:
                self.maps[square[0] * self.MinesweeperGameMap.col + square[1]].image = (
                    self._get_actor_with_state(
                        self.MinesweeperGameMap.map[square[0]][square[1]]))

        # Check whether you win the game.
        if self.MinesweeperGameMap.emptySquareNumber == 0:
            self.gameStatus = "win"

    # first click. And the function will pass if clickTimes != 0
    def _first_click(self, x, y):
        while (self.clickTimes == 0
               and self.MinesweeperGameMap.map[x][y] == State.Mine_Unrevealed):
            self.MinesweeperGameMap.generate_the_map()

        if self.clickTimes == 0:
            self.start_clock()

    # The details when click square.
    def _left_click_square_details(self, x, y):
        change_square = self.MinesweeperGameMap.left_mouse_click_the_map(x, y)
        if change_square is None:
            return

        self.clickTimes += 1

        if "mine" in change_square:
            self._click_mine(change_square)
            return

        self._click_empty_square(change_square)

    def _check_whether_in_the_map(self, x, y):
        return 0 <= x < self.MinesweeperGameMap.row and 0 <= y < self.MinesweeperGameMap.col


game = MinesweeperGame()
flag = False


# We must generate update() function, or we can not draw the time each time it updates.
def update():
    pass


def draw():
    # screen.fill((255, 255, 255))
    screen.clear()
    game.draw()


def on_mouse_down(pos, button):
    click_j = (pos[0] - Constants.FIRST_SQUARE_START_X + TILE_SIZE // 2) // TILE_SIZE
    click_i = (pos[1] - Constants.FIRST_SQUARE_START_Y + TILE_SIZE // 2) // TILE_SIZE

    if button == mouse.LEFT:
        if game.gameStatus == "begin":
            game.level_select(pos)
        else:
            game.left_click_square(click_i, click_j)
    elif button == mouse.RIGHT:
        game.right_click_square(click_i, click_j)


pgzrun.go()
