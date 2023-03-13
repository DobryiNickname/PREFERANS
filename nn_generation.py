import numpy as np
# import pytorch
# import tensorflow


from consts import CARD_SUIT_DICT
from typing import List
from card import Card
# [Suit: int Value:int isTrump:bool isMine:bool isInBita:bool isOnBoard:bool CardBelongsToBotId:int isValidCardForMove:bool] x32

def initialise_input_vector(trump: int, bot_id: int, bot_hand: List[Card], cards_in_bita: List[Card], cards_on_table, valid_moves: List[Card]):
    
    # suits
    spades_params = [0] * 8
    clubs_params = [1] * 8
    diamonds_params = [2] * 8
    hearts_params = [3] * 8
    suit_params = spades_params + clubs_params + diamonds_params + hearts_params
    
    # values
    value_params = [i for i in range(8)]
    all_cards_value_params = value_params + value_params + value_params + value_params
    
    # trumps
    isTrump_params = [True if param==trump else False for param in suit_params]
    
    # player's hand
    isMine_params = [False] * 32
    for card in bot_hand:
        idx = card.get_suit() * 8 + card.get_value()
        isMine_params[idx] = True
    
    # bita (no longer in game)
    isInBita_params = [False] * 32
    for card in cards_in_bita:
        idx = card.get_suit() * 8 + card.get_value()
        isInBita_params[idx] = True

    # cards on table
    isOnBoard_params = [False] * 32
    for card in cards_on_table.values():
        idx = card.get_suit() * 8 + card.get_value()
        isOnBoard_params[idx] = True

    # card belongs to what bot
    CardBelongsToBotId_params = [] # TODO должен быть 32-мерным с заполением bot_id.mask(isMine_params) + заполнять при наличии cards_on_table

    # valid moves
    isValidCardForMove_params = [False] * 32
    for card in valid_moves:
        idx = card.get_suit() * 8 + card.get_value()
        isValidCardForMove_params[idx] = True

    input_params = suit_params \
                + all_cards_value_params \
                + isTrump_params \
                + isMine_params \
                + isInBita_params \
                + isOnBoard_params \
                + CardBelongsToBotId_params \
                + isValidCardForMove_params
    
    return input_params

from rlcard.agents import RandomAgent

