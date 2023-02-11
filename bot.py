import operator
from typing import List
import logging
import random

from card import Card
from consts import CARD_SUIT_DICT, CARD_VALUE_DICT


class Bot:
    def __init__(self, bot_id: int, decision_mode, hand: List[int]=None):
        self.hand = sorted(hand, key=operator.attrgetter("suit", "value"), reverse=True) if hand is not None else hand
        self.bot_id = bot_id

        self.decision_functions = {
            "MAXIMISE": self.baseline_choose_max_value_card,
            "RANDOM": self.baseline_choose_random_value_card
        }

        self.decision_mode = decision_mode

        self.logger = logging.getLogger()

    @staticmethod
    def format_card(card: Card):
        return CARD_VALUE_DICT[card.get_value()] + CARD_SUIT_DICT[card.get_suit()]

    def show_hand(self) -> None:
        """
        Show sorted hand in terms of card's value and suit.
        """
        if self.hand is None:
            self.logger.error(f"I'm bot {self.bot_id}. My hand is empty")
            raise ValueError("self.hand is None")
        
        for card in self.hand:
            print(self.format_card(card), end=" ")
        print("\n")

    def _remove_card_from_hand(self, card: Card):
        self.hand.remove(card)

    def make_decision(self, valid_moves, trump):
        return(self.decision_functions[self.decision_mode](valid_moves, trump))

    def baseline_choose_max_value_card(self, valid_moves: List[Card], trump):
        if trump is not None and trump in [card.get_suit() for card in valid_moves]:
            possible_cards = [card for card in valid_moves if card.get_suit() == trump]
        else:
            possible_cards = sorted(valid_moves, key=operator.attrgetter("value"), reverse=True)

        max_choice = 0
        self._remove_card_from_hand(possible_cards[max_choice])
        return possible_cards[max_choice]

    def baseline_choose_random_value_card(self, valid_moves: List[Card], trump):
        rnd_choice = random.choice(valid_moves)
        self._remove_card_from_hand(rnd_choice)
        return rnd_choice