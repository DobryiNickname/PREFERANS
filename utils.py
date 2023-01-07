import copy
import numpy as np
import time
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

def make_copy(obj: MetaHand):
    copy_metahand = MetaHand(
        metahand=[
            MetaCard(
                cards=i.cards[:],
                suit=i.suit,
                value=i.value,
                capacity=i.capacity
                ) 
            for i in obj.metahand
        ]
    )
    # copy_obj = copy.deepcopy(obj)
    return copy_metahand

def put_card_on_table(bot_id_mapping: Dict[int, Bot],  bot_order: List[int], trump, current_depth, max_depth=5, logger={}):

    if current_depth > max_depth:
        return None

    first_bot_id = bot_order[0]
    first_bot = bot_id_mapping[first_bot_id]

    cards_on_table = {
        "first card": None,
        "second card": None,
        "third card": None,
    }

    for first_card in first_bot.meta_hand.metahand:
        cards_on_table["first card"] = first_card
        # if current_depth == 1:
        #     print(f'first card suit-{first_card.suit} value-{first_card.value}')

        start = time.time()
        copy_first_bot = Bot(first_bot_id, meta_hand=make_copy(first_bot.meta_hand))
        end = time.time()
        duration = end - start
        logger['make_copy'].append(duration)

        start = time.time()
        copy_first_bot.meta_hand.decrease_card_capacity(first_card)
        end = time.time()
        duration = end - start
        logger['decrease'].append(duration)

        second_bot_id = bot_order[1]
        second_bot = bot_id_mapping[second_bot_id]

        start = time.time()
        second_bot_valid_moves = valid_moves(second_bot.meta_hand, cards_on_table, trump=trump)
        end = time.time()
        duration = end - start
        logger['valid_moves'].append(duration)
        
        for second_card in second_bot_valid_moves:
            cards_on_table["second card"] = second_card
            
            start = time.time()
            copy_second_bot = Bot(second_bot_id, meta_hand=make_copy(second_bot.meta_hand))
            end = time.time()
            duration = end - start
            logger['make_copy'].append(duration)
            
            start = time.time()
            copy_second_bot.meta_hand.decrease_card_capacity(second_card)
            end = time.time()
            duration = end - start
            logger['decrease'].append(duration)

            third_bot_id = bot_order[2]
            third_bot = bot_id_mapping[third_bot_id]

            start = time.time()
            third_bot_valid_moves = valid_moves(third_bot.meta_hand, cards_on_table, trump=trump)
            end = time.time()
            duration = end - start
            logger['valid_moves'].append(duration)
            
            for third_card in third_bot_valid_moves:
                cards_on_table["third card"] = third_card

                start = time.time()
                copy_third_bot = Bot(third_bot_id, meta_hand=make_copy(third_bot.meta_hand))
                end = time.time()
                duration = end - start
                logger['make_copy'].append(duration)
                
                start = time.time()
                copy_third_bot.meta_hand.decrease_card_capacity(third_card)
                end = time.time()
                duration = end - start
                logger['decrease'].append(duration)

                bot_id_mapping_next = {
                    copy_first_bot.bot_id: copy_first_bot,
                    copy_second_bot.bot_id: copy_second_bot,
                    copy_third_bot.bot_id: copy_third_bot,
                }

                start = time.time()
                bot_order_next = determine_bot_order(cards_on_table, bot_order, trump)
                end = time.time()
                duration = end - start
                logger['determine_bot_order'].append(duration)

                put_card_on_table(
                    bot_id_mapping_next, 
                    bot_order_next, 
                    trump, 
                    current_depth + 1,
                    max_depth, 
                    logger)
