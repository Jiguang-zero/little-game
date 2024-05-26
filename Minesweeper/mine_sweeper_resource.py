"""
*Description: This file will store the resource of minesweeper.
"""

from mine_sweeper import State

actor_path_dict = {
    State.EmptySquare_Unrevealed: "unrevealed",
    State.Mine_Unrevealed: "unrevealed",
    State.EmptySquare_Revealed: "empty",
    State.Mine_Revealed: "mine",
}

state_dict = {member.value: member for member in State}
for i in range(1, 9):
    actor_path_dict[state_dict[i]] = "digit" + str(i)
