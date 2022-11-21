import copy
import numpy as np
from typing import List, Dict

from card import Card, MetaCard, MetaHand
from bot import Bot


bot_order_mapping = {
    "first bot turn": [0, 1, 2],
    "second bot turn": [1, 2, 0],
    "third bot turn": [2, 0, 1],
}


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


def valid_moves(metahand: MetaHand, metacards_on_board: Dict[str, MetaCard], trump=None) -> List[MetaCard]:
    valid_moves = []

    # Если у бота первый ход
    if metacards_on_board["first card"] is None:
        valid_moves = metahand.metahand
        return valid_moves

    first_card_suit = metacards_on_board["first card"].get_suit()

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


def determine_bot_order(cards_on_board: Dict[str, MetaCard], bot_order: List[int], trump=None):

    mapping = {
        cards_on_board['first card']: bot_order[0],
        cards_on_board['second card']: bot_order[1],
        cards_on_board['third card']: bot_order[2]
    }

    if not any([card.get_suit() == trump for card in cards_on_board.values()]):
        trump = cards_on_board["first card"].get_suit()

    trump_cards = [card for card in cards_on_board.values() if card.get_suit() == trump]
    sort_by_value_trump_cards = sorted(trump_cards, key=lambda x: x.get_value(), reverse=True)

    winner_id = mapping[sort_by_value_trump_cards[0]]
    if winner_id == 0:
        return bot_order_mapping["first bot turn"]
    elif winner_id == 1:
        return bot_order_mapping["second bot turn"]
    else:
        return bot_order_mapping["third bot turn"]


def put_card_on_table(bot_id_mapping: Dict[int, Bot],  bot_order: List[int]):
    first_bot_id = bot_order[0]
    first_bot = bot_id_mapping[first_bot_id]

    cards_on_table = {
        "first card": None,
        "second card": None,
        "third card": None,
    }

    for first_card in first_bot.meta_hand.metahand:
        cards_on_table["first card"] = first_card
        print(cards_on_table["first card"])

        copy_first_bot = copy.deepcopy(first_bot)
        copy_first_bot.meta_hand.decrease_card_capacity(first_card)

        second_bot_id = bot_order[1]
        second_bot = bot_id_mapping[second_bot_id]
        second_bot_valid_moves = valid_moves(second_bot.meta_hand, cards_on_table)
        for second_card in second_bot_valid_moves:
            cards_on_table["second card"] = second_card

            copy_second_bot = copy.deepcopy(second_bot)
            copy_second_bot.meta_hand.decrease_card_capacity(second_card)

            third_bot_id = bot_order[2]
            third_bot = bot_id_mapping[third_bot_id]
            third_bot_valid_moves = valid_moves(second_bot.meta_hand, cards_on_table)
            for third_card in third_bot_valid_moves:
                cards_on_table["third card"] = third_card

                copy_third_bot = copy.deepcopy(third_bot)
                copy_third_bot.meta_hand.decrease_card_capacity(third_card)

                bot_id_mapping = {
                    copy_first_bot.bot_id: copy_first_bot,
                    copy_second_bot.bot_id: copy_second_bot,
                    copy_third_bot.bot_id: copy_third_bot,
                }
                # bot_order = determine_bot_order(cards_on_table, trump)
                # put_cards_on_table(bot_id_mapping, bot_order)


