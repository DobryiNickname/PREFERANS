from typing import List, Dict

from card import Card
from bot import Bot

import numpy as np


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
    np.random.seed(69)
    shuffled_deck = np.arange(32)
    np.random.shuffle(shuffled_deck)

    generated_cards = {
        "hand_1": [Card(x % 8, x // 8) for x in shuffled_deck[0:10]],
        "hand_2": [Card(x % 8, x // 8) for x in shuffled_deck[10:20]],
        "hand_3": [Card(x % 8, x // 8) for x in shuffled_deck[20:30]],
        "talon": [Card(x % 8, x // 8) for x in shuffled_deck[30:32]]
    }

    return generated_cards


def valid_moves(hand: List[Card], cards_on_board: Dict[str, Card], trump=None) -> List[Card]:
    valid_moves = []

    # Если у бота первый ход
    if cards_on_board["first card"] is None:
        valid_moves = hand
        return valid_moves

    first_card_suit = cards_on_board["first card"].get_suit()

    # Смотрим наличие масти первоположенной карты
    for card in hand:
        if card.get_suit() == first_card_suit:
            valid_moves.append(card)
    if len(valid_moves) != 0:
        return valid_moves

    # Смотрим наличие козыря(если назначен) в отсутствии первоположенной масти
    if trump is not None:
        for card in hand:
            if card.get_suit() == trump:
                valid_moves.append(card)
        if len(valid_moves) != 0:
            return valid_moves

    # Оставшиеся любые карты
    valid_moves = hand
    return valid_moves

def determine_bot_order(cards_on_board: Dict[str, Card], bot_order: List[int], trump=None):

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

def put_card_on_table(bot_id_mapping: Dict[int, Bot],  bot_order: List[int], trump):

    first_bot_id = bot_order[0]
    first_bot = bot_id_mapping[first_bot_id]
    second_bot_id = bot_order[1]
    second_bot = bot_id_mapping[second_bot_id]
    third_bot_id = bot_order[2]
    third_bot = bot_id_mapping[third_bot_id]
    
    cards_on_table = {
        "first card": None,
        "second card": None,
        "third card": None,
    }

    cards_on_table["first card"] = first_bot.make_decision(
        valid_moves(
            first_bot.hand,
            cards_on_table,
            trump),
        trump
        )
    cards_on_table["second card"] = second_bot.make_decision(
        valid_moves(
            second_bot.hand,
            cards_on_table,
            trump),
        trump
        )
    cards_on_table["third card"] = third_bot.make_decision(
        valid_moves(
            third_bot.hand,
            cards_on_table,
            trump),
        trump
        )

    print(
        f"Cards on table - {first_bot.format_card(cards_on_table['first card'])}"
        f" {first_bot.format_card(cards_on_table['second card'])}"
        f" {first_bot.format_card(cards_on_table['third card'])}"
        )
    
    bot_order_next_move = determine_bot_order(cards_on_table, bot_order, trump)

    return bot_order_next_move
