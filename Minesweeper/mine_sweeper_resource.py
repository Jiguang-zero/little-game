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

restart_actor = Actor("restart")
restart_actor.x = 7 * Constants.SCREEN_WIDTH // 8
restart_actor.y = 3 * Constants.SCREEN_HEIGHT // 4

home_actor = Actor("home")
home_actor.x = 7 * Constants.SCREEN_WIDTH // 8
home_actor.y = 7 * Constants.SCREEN_HEIGHT // 8

option_actor = Actor("option")
option_actor.x = 7 * Constants.SCREEN_WIDTH // 8
option_actor.y = 5 * Constants.SCREEN_HEIGHT // 8

return_actor = Actor("return")
return_actor.x = 1 * Constants.SCREEN_WIDTH // 20
return_actor.y = 1 * Constants.SCREEN_HEIGHT // 10

change_actor = Actor("change")
change_actor.x = 4 * Constants.SCREEN_WIDTH // 5
change_actor.y = 3 * Constants.SCREEN_HEIGHT // 5

change_game_value_actors = []
style_map_key = ["row", "col", "mine"]
option_style = Constants.OPTION_SETTING_STYLE
for i in range(3):
    increase_actor = Actor("increase")
    decrease_actor = Actor("decrease")
    increase_actor.x = option_style[style_map_key[i]]["change_value"][0][0]
    increase_actor.y = option_style[style_map_key[i]]["change_value"][0][1] + Constants.DEVIATION_FROM_P_AND_F
    decrease_actor.x = option_style[style_map_key[i]]["change_value"][1][0]
    decrease_actor.y = option_style[style_map_key[i]]["change_value"][1][1] + Constants.DEVIATION_FROM_P_AND_F
    change_game_value_actors.append([increase_actor, decrease_actor])
