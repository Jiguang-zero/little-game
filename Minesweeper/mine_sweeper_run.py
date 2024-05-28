# -*- coding:gb18030 -*-
import threading
import time
import pgzrun

from mine_sweeper import State
from mine_sweeper import state_can_be_right_click
from mine_sweeper import Minesweeper
from mine_sweeper_resource import (actor_path_dict, level_choice,
                                   level_set_row_col_mine, restart_actor,
                                   home_actor, option_actor, return_actor, change_actor,
                                   change_game_value_actors)
from mine_sweeper_constants import Constants

TITLE = "Minesweeper"
TILE_SIZE = Constants.TILE_SIZE
WIDTH = Constants.SCREEN_WIDTH
HEIGHT = Constants.SCREEN_HEIGHT


def draw_in_game_button():
    restart_actor.draw()
    home_actor.draw()
    option_actor.draw()


def _check_values_can_be_change(row, col, mine):
    # check positive_number
    if row < 1 or col < 1 or mine <= 1:
        return False
    if mine >= row * col:
        return False
    # for better gaming.
    if row > 27 or col > 37:
        return False
    if mine / (row * col) >= 0.92 or mine / (row * col) <= 0.08:
        return False
    return True


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
        self.last_click_time = 0
        self.last_click_square = []
        self.flag_mine = 0
        self.row: int = 0
        self.col: int = 0
        self.mine: int = 0

    def draw(self):
        if self.gameStatus == "begin":
            for level in level_choice:
                level.draw()
        elif self.gameStatus == "option":
            self._draw_option()
        else:
            for item in self.maps:
                item.draw()
            self._draw_data_values()
            draw_in_game_button()

    def start_clock(self):
        def run_clock():
            while self.stop_clock is False:
                self.time_clock += 1
                time.sleep(1)
                if self.time_clock >= 999:
                    self.time_clock = 999
                    self.stop_clock = True

        clock_thread = threading.Thread(target=run_clock)
        clock_thread.daemon = True
        clock_thread.start()

    def left_click_square(self, x, y):
        # left mouse click square when the game is running
        if self.gameStatus != "running" or not self._check_whether_in_the_map(x, y):
            return

        if self._check_whether_can_be_double_click(x, y):
            current_time = time.time()
            current_square = [x, y]
            if (current_time - self.last_click_time < Constants.DOUBLE_CLICK_INTERVAL
                    and current_square == self.last_click_square):
                self.double_click_square(x, y)
            self.last_click_time = current_time
            self.last_click_square = current_square
        else:
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

    def double_click_square(self, x, y):
        if self._check_whether_can_be_double_click(x, y):
            current_square_num = int(
                self._get_maps_with_x_y(x, y).image.split("//")[-1][len("digit"):])
            flag_numbers: int = 0
            square_to_be_click = []
            for i in range(8):
                new_x = x + Minesweeper.dir_x[i]
                new_y = y + Minesweeper.dir_y[i]
                if not self._check_whether_in_the_map(new_x, new_y):
                    continue
                if (self._get_maps_with_x_y(new_x, new_y).image
                        == self._get_actor_with_style("flag")):
                    flag_numbers += 1
                else:
                    square_to_be_click.append([new_x, new_y])
            if current_square_num == flag_numbers:
                for square in square_to_be_click:
                    self.left_click_square(square[0], square[1])

    def right_click_square(self, x, y):
        if self.gameStatus != "running" or not self._check_whether_in_the_map(x, y):
            return

        actor = self.maps[x * self.MinesweeperGameMap.col + y]
        if state_can_be_right_click(self.MinesweeperGameMap.map[x][y]):
            if actor.image == self._get_actor_with_style("flag"):
                self.flag_mine -= 1
                actor.image = self._get_actor_with_style("sign")
            elif actor.image == self._get_actor_with_style("sign"):
                actor.image = self._get_actor_with_state(
                    self.MinesweeperGameMap.map[x][y]
                )
            elif actor.image != self._get_actor_with_style("flag"):
                self.flag_mine += 1
                actor.image = self._get_actor_with_style("flag")

    def click_in_game_button(self, pos):
        if restart_actor.collidepoint(pos):
            self._click_restart()
        if home_actor.collidepoint(pos):
            self._click_home()
        if option_actor.collidepoint(pos):
            self._click_option()

    def click_button_in_option(self, pos):
        if return_actor.collidepoint(pos):
            self.gameStatus = "running"
        self._click_change_value_setting(pos)
        if change_actor.collidepoint(pos):
            self.MinesweeperGameMap.change_the_map(self.row, self.col, self.mine)
            self._init_game()
            self.gameStatus = "running"

    ''' We will define private function below this line. '''
    """
    *Description: Get the full path of actor.
    """

    def _get_actor_with_state(self, minesweeper_state):
        actor_path = actor_path_dict[minesweeper_state]
        return self._get_actor_with_style(actor_path)

    def _get_actor_with_style(self, style):
        return self.style + "//" + style

    # draw the data: like, time: 43
    def _draw_data_values(self):
        time_style = Constants.TIME_SHOWING_STYLE
        mine_style = Constants.MINE_NUMBER_SHOWING_STYLE
        state_style = Constants.STATES_SHOWING_STYLE
        screen.draw.text("time: " + str(self.time_clock), time_style["pos"],
                         fontsize=time_style["size"], color="white", fontname="mono")
        screen.draw.text("left: " + str(self.flag_mine) + "/" + str(self.MinesweeperGameMap.mineNumber),
                         mine_style["pos"], fontsize=mine_style["size"], color="white", fontname="mono")
        screen.draw.text("states: " + self.gameStatus, state_style["pos"],
                         color="white", fontname="mono", fontsize=state_style["size"])

    def _click_restart(self):
        self.MinesweeperGameMap.generate_the_map()
        self._init_game()
        self.gameStatus = "running"
        self.stop_clock = True
        self.time_clock = 0

    def _click_home(self):
        self.gameStatus = "begin"
        self.stop_clock = True
        self.time_clock = 0

    def _init_maps(self):
        self.maps = []
        for i in range(self.MinesweeperGameMap.row):
            for j in range(self.MinesweeperGameMap.col):
                mine_square = Actor(self._get_actor_with_state(self.MinesweeperGameMap.map[i][j]))
                mine_square.x = j * TILE_SIZE + Constants.FIRST_SQUARE_START_X
                mine_square.y = i * TILE_SIZE + Constants.FIRST_SQUARE_START_Y
                self.maps.append(mine_square)

    def _init_game(self):
        self._init_maps()
        self.clickTimes = 0
        self.time_clock = 0
        self.flag_mine = 0
        self.stop_clock = False

    # change_square: MinesweeperGameMap.left_mouse_click_the_map
    def _click_mine(self, change_square):
        mine = change_square["mine"][0]
        self._get_maps_with_x_y(mine[0], mine[1]).image = (
            self._get_actor_with_state(
                self.MinesweeperGameMap.map[mine[0]][mine[1]]
            )
        )
        self.gameStatus = "lose"
        self.stop_clock = True
        sounds.explosion.play()

    def _click_empty_square(self, change_square):
        for item in change_square:
            for square in change_square[item]:
                self._get_maps_with_x_y(square[0], square[1]).image = (
                    self._get_actor_with_state(
                        self.MinesweeperGameMap.map[square[0]][square[1]]))

        # Check whether you win the game.
        if self.MinesweeperGameMap.emptySquareNumber == 0:
            self.gameStatus = "win"
            self.stop_clock = True
            sounds.win.play()

    # first click. And the function will pass if clickTimes != 0
    def _first_click(self, x, y):
        while (self.clickTimes == 0
               and self.MinesweeperGameMap.map[x][y] == State.Mine_Unrevealed):
            self.MinesweeperGameMap.generate_the_map()

        if self.clickTimes == 0:
            self.stop_clock = False
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
        return (0 <= x < self.MinesweeperGameMap.row and
                0 <= y < self.MinesweeperGameMap.col)

    # array -> 2D. x, y must be right input.
    def _get_maps_with_x_y(self, x, y):
        return self.maps[x * self.MinesweeperGameMap.col + y]

    def _check_whether_can_be_double_click(self, x, y):
        if not self._check_whether_in_the_map(x, y):
            return False
        for i in range(1, 9):
            if (self._get_maps_with_x_y(x, y).image ==
                    self._get_actor_with_style("digit" + str(i))):
                return True
        return False

    def _draw_option(self):
        return_actor.draw()
        change_actor.draw()
        self._draw_value_setting()

    def _draw_value_setting(self):
        option_style = Constants.OPTION_SETTING_STYLE
        screen.draw.text("当前行数: " + str(self.row), option_style["row"]["pos"],
                         fontsize=option_style["size"], color="white", fontname="simple_kai")
        screen.draw.text("当前列数: " + str(self.col), option_style["col"]["pos"],
                         fontsize=option_style["size"], color="white", fontname="simple_kai")
        screen.draw.text("当前雷数: " + str(self.mine), option_style["mine"]["pos"],
                         fontsize=option_style["size"], color="white", fontname="simple_kai")

        for item in change_game_value_actors:
            item[0].draw()
            item[1].draw()

    def _click_option(self):
        self.gameStatus = "option"
        self.row = self.MinesweeperGameMap.row
        self.col = self.MinesweeperGameMap.col
        self.mine = self.MinesweeperGameMap.mineNumber

    def _click_change_value_setting(self, pos):
        temp_values = [self.row, self.col, self.mine]
        index = 0
        for button in change_game_value_actors:
            if button[0].collidepoint(pos):
                temp_values[index] += 1
            if button[1].collidepoint(pos):
                temp_values[index] -= 1
            index += 1
        if _check_values_can_be_change(temp_values[0], temp_values[1], temp_values[2]):
            self.row = temp_values[0]
            self.col = temp_values[1]
            self.mine = temp_values[2]


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
        elif game.gameStatus == "option":
            game.click_button_in_option(pos)
        else:
            game.click_in_game_button(pos)
            if game.gameStatus == "running":
                game.left_click_square(click_i, click_j)

    elif button == mouse.RIGHT:
        game.right_click_square(click_i, click_j)
    elif button == mouse.MIDDLE:
        game.double_click_square(click_i, click_j)


pgzrun.go()
