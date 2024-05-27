"""
* Description: Define the Minesweeper.
* Author: Zearo-Jiguang
"""

import random
import queue

from enum import Enum


# Flag and Sign should not be in this class, as their will cover the origin state(Mine).
class State(Enum):
    Digit_1 = 1
    Digit_2 = 2
    Digit_3 = 3
    Digit_4 = 4
    Digit_5 = 5
    Digit_6 = 6
    Digit_7 = 7
    Digit_8 = 8
    Mine_Unrevealed = 10
    Mine_Revealed = 11
    EmptySquare_Unrevealed = 12
    EmptySquare_Revealed = 13


def state_can_be_right_click(state):
    if state == State.Mine_Unrevealed or state == State.EmptySquare_Unrevealed:
        return True
    return False


class Minesweeper:
    def __init__(self, row, col, mine_number):
        self.row: int = row
        self.col: int = col
        self.mineNumber: int = mine_number
        self.emptySquareNumber: int = row * col - mine_number
        self.map = []

    # static member
    dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
    dir_y = [1, 0, -1, 0, 1, -1, 1, -1]
    # the dictionary of State
    state_dict = {member.value: member for member in State}

    # generate the map
    def generate_the_map(self):
        self.map = [[State.EmptySquare_Unrevealed for _ in range(self.col)] for _ in range(self.row)]

        # generate mineNumber numbers in range(1, row * col)
        random_mines = random.sample(range(1, self.row * self.col + 1), self.mineNumber)
        for random_mine in random_mines:
            temp: int = random_mine - 1
            self.map[temp // self.col][temp % self.col] = State.Mine_Unrevealed

    def change_the_map(self, new_row, new_col, new_mine_number):
        if new_row < 1 or new_col < 1:
            # TODO: log
            return
        elif new_mine_number <= 0 or new_mine_number >= new_row * new_col:
            # TODO: log
            return
        self.row = new_row
        self.col = new_col
        self.mineNumber = new_mine_number
        self.emptySquareNumber: int = new_row * new_col - new_mine_number
        self.generate_the_map()
        # self._test_print_the_map()

    def left_mouse_click_the_map(self, click_row, click_col):
        if click_row < 0 or click_row >= self.row or click_col < 0 or click_col >= self.col:
            # TODO: error
            return None
        # click the unrevealed mine
        if self.map[click_row][click_col] == State.Mine_Unrevealed:
            self.map[click_row][click_col] = State.Mine_Revealed
            return {"mine": [[click_row, click_col]]}
        # click the unrevealed empty square
        elif self.map[click_row][click_col] == State.EmptySquare_Unrevealed:
            return self._bfs_click_the_map(click_row, click_col)

    # private function dealing the map when click State.EmptySquare_Unrevealed
    def _bfs_click_the_map(self, click_row, click_col):
        vis = [[False for _ in range(self.col)] for _ in range(self.row)]
        q = queue.Queue()
        q.put((click_row, click_col))
        vis[click_row][click_col] = True
        ans = {"near_mine": [], "near_no_mine": []}
        while not q.empty():
            pos = q.get()
            near_mine_number: int = 0
            x: int = pos[0]
            y: int = pos[1]
            for i in range(8):
                tx = x + self.__class__.dir_x[i]
                ty = y + self.__class__.dir_y[i]
                if tx < 0 or tx >= self.row or ty < 0 or ty >= self.col:
                    continue
                # We just think the unrevealed mine as when the mine is revealed, we lost the game.
                near_mine_number += 1 if self.map[tx][ty] == State.Mine_Unrevealed else 0
            self.emptySquareNumber -= 1
            # when near_mine_number > 8 , it will be an error.
            if 0 < near_mine_number <= 8:
                self.map[x][y] = self.__class__.state_dict[near_mine_number]
                ans["near_mine"].append([x, y])
            elif near_mine_number == 0:
                self.map[x][y] = State.EmptySquare_Revealed
                ans["near_no_mine"].append([x, y])
                for i in range(8):
                    tx = x + self.__class__.dir_x[i]
                    ty = y + self.__class__.dir_y[i]
                    if (tx < 0 or tx >= self.row or ty < 0 or ty >= self.col
                            or vis[tx][ty] or self.map[tx][ty] != State.EmptySquare_Unrevealed):
                        continue
                    q.put((tx, ty))
                    vis[tx][ty] = True
        return ans

    ''' The functions below this line are for testing. '''

    def _test_print_the_map(self):
        for row in self.map:
            print([element.value for element in row])
