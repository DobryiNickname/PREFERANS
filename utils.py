from card import Card, MetaCard, MetaHand

import numpy as np
from typing import List, Dict


def generate_hands_and_talon() -> Dict[str, List[Card]]:
    """
    Generate random shuffle per turn.
    :return: List of hands
    """
    shuffled_deck = np.arange(32)
    np.random.shuffle(shuffled_deck)

    generated_cards = {
        "hand_1": [Card(x % 8, x // 8) for x in shuffled_deck[0:10]],
        "hand_2": [Card(x % 8, x // 8) for x in shuffled_deck[10:20]],
        "hand_3": [Card(x % 8, x // 8) for x in shuffled_deck[20:30]],
        "talon": [Card(x % 8, x // 8) for x in shuffled_deck[30:32]]
    }

    return generated_cards


def valid_moves(metahand: MetaHand, metacards_on_board: List[MetaCard], trump=None):
    valid_moves = []

    # Если у бота первый ход
    if len(metacards_on_board) == 0:
        valid_moves = metahand.metahand
        return valid_moves

    first_card_suit = metacards_on_board[0].get_suit()

    # Смотрим наличие масти первоположенной карты
    for metacard in metahand.metahand:
        if metacard.get_suit() == first_card_suit:
            valid_moves.append(metacard)
    if len(valid_moves) != 0:
        return valid_moves

    # Смотрим наличие козыря(если назначен) в отсутствии первоположенной масти
    if trump is not None:
        for metacard in metahand.metahand:
            if metacard.get_suit() == trump:
                valid_moves.append(metacard)
        if len(valid_moves) != 0:
            return valid_moves

    # Оставшиеся любые карты
    valid_moves = metahand.metahand
    return valid_moves
