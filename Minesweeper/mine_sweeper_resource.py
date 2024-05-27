"""
*Description: This file will store the resource of minesweeper.
"""
from pgzero.actor import Actor

from mine_sweeper import State
from mine_sweeper_constants import Constants

actor_path_dict = {
    State.EmptySquare_Unrevealed: "unrevealed",
    State.Mine_Unrevealed: "unrevealed",
    State.EmptySquare_Revealed: "empty",
    State.Mine_Revealed: "mine",
}

state_dict = {member.value: member for member in State}
for i in range(1, 9):
    actor_path_dict[state_dict[i]] = "digit" + str(i)

level_choice = []
for i in range(1, 4):
    level_actor = Actor("level" + str(i))
    level_actor.x = Constants.SCREEN_WIDTH // 2
    level_actor.y = Constants.LEVEL_CHOICE_Y_BEGIN + Constants.LEVEL_CHOICE_Y_INTERVAL * i
    level_choice.append(level_actor)

level_set_row_col_mine = {
    "level1": [9, 9, 10],
    "level2": [16, 16, 40],
    "level3": [16, 30, 99]
}
