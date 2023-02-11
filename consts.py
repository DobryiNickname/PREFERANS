from colorama import Fore

CARD_VALUE_DICT = {
    0: "7",
    1: "8",
    2: "9",
    3: "10",
    4: "J",
    5: "Q",
    6: "K",
    7: "A"
}

CARD_SUIT_DICT = {
    0: "♠",
    1: "♣",
    2: "♦",
    3: "♥"
}

SCORE_TABLE = {
    "POOL_1": 0,
    "POOL_2": 0,
    "POOL_3": 0,
    "MOUNTAIN_1": 0,
    "MOUNTAIN_2": 0,
    "MOUNTAIN_3": 0,
    "WHIST_12": 0,
    "WHIST_13": 0,
    "WHIST_21": 0,
    "WHIST_23": 0,
    "WHIST_31": 0,
    "WHIST_32": 0,
    "BID": 1,
    "END": 2
}

TRADE_TABLE = {
    0: "6S",
    1: "6C",
    2: "6D",
    3: "6H",
    4: "6NT",
    5: "7S",
    6: "7C",
    7: "7D",
    8: "7H",
    9: "7NT",
    10: "8S",
    11: "8C",
    12: "8D",
    13: "8H",
    14: "8NT",
    15: "9S",
    16: "9C",
    17: "9D",
    18: "9H",
    19: "9NT",
    20: "10S",
    21: "10C",
    22: "10D",
    23: "10H",
    24: "10NT",
    25: "MISERE"
}

TRADE_OPTIONS = {
    0: "PASS",
    1: "RAISE",
    2: "STAY"
}

GAME_MODE = {
    0: "ALL PASS",
    1: "TRICKS"
}

GAME_OPTIONS = {
    0: "ACCEPT GAME",
    1: "DECLINE GAME"
}

WHIST_OPTIONS = {
    0: "PASS",
    1: "WHIST",
    2: "HALF WHIST"
}

WHIST_MODE = {
    0: "DARK",
    1: "LIGHT"
}
