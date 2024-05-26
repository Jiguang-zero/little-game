"""
*Description: This file will store the resource of minesweeper.
"""

from mine_sweeper import State

actor_path_dict = {

}

for item in State:
    actor_path_dict[item] = "unrevealed"

actor_path_dict[State.Mine_Revealed] = "revealed"
actor_path_dict[State.EmptySquare_Revealed] = "revealed"

state_dict = {member.value: member for member in State}
for i in range(1, 9):
    actor_path_dict[state_dict[i]] = "revealed"

