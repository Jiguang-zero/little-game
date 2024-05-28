class Constants:
    TILE_SIZE = 20  # The size of the square.

    SCREEN_WIDTH = 50 * TILE_SIZE
    SCREEN_HEIGHT = 30 * TILE_SIZE

    LEVEL_CHOICE_X = SCREEN_WIDTH // 2
    LEVEL_CHOICE_Y_BEGIN = 50
    LEVEL_CHOICE_Y_INTERVAL = 120

    FIRST_SQUARE_START_X = 30
    FIRST_SQUARE_START_Y = 40

    DOUBLE_CLICK_INTERVAL = 0.4

    DEVIATION_FROM_P_AND_F = 15  # DEVIATION_FROM_PHOTO_AND_FONTS

    TIME_SHOWING_STYLE = {
        "pos": (9 * SCREEN_WIDTH // 11, 2 * SCREEN_HEIGHT // 24),
        "size": 16
    }

    MINE_NUMBER_SHOWING_STYLE = {
        "pos": (9 * SCREEN_WIDTH // 11, 3 * SCREEN_HEIGHT // 24),
        "size": 16
    }

    STATES_SHOWING_STYLE = {
        "pos": (9 * SCREEN_WIDTH // 11, 4 * SCREEN_HEIGHT // 24),
        "size": 16
    }

    OPTION_SETTING_STYLE = {
        "row": {
            "pos": (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 3),
            "change_value": [
                [4 * SCREEN_WIDTH // 10, SCREEN_HEIGHT // 3],
                [5 * SCREEN_WIDTH // 10, SCREEN_HEIGHT // 3]
            ]
        },
        "col": {
            "pos": (SCREEN_WIDTH // 10, 2 * SCREEN_HEIGHT // 5),
            "change_value": [
                [4 * SCREEN_WIDTH // 10, 2 * SCREEN_HEIGHT // 5],
                [5 * SCREEN_WIDTH // 10, 2 * SCREEN_HEIGHT // 5]
            ]
        },
        "mine": {
            "pos": (SCREEN_WIDTH // 10, 7 * SCREEN_HEIGHT // 15),
            "change_value": [
                [4 * SCREEN_WIDTH // 10, 7 * SCREEN_HEIGHT // 15],
                [5 * SCREEN_WIDTH // 10, 7 * SCREEN_HEIGHT // 15]
            ]
        },
        "size": 32
    }
