import numpy as np

from typing import List

import consts


class Preferans:
    def __init__(self):
        self.card_value_dict = consts.CARD_VALUE_DICT
        self.card_suit_dict = consts.CARD_SUIT_DICT
        self.deck_of_cards = np.arange(32)

        self.first_hand = None
        self.second_hand = None
        self.third_hand = None
        self.talon = None

    @classmethod
    def callable(cls) -> None:
        obj = cls()
        obj.run()

    def run(self) -> None:
        self._generate_turn()
        self._show_hand(self.first_hand)

    def _generate_turn(self) -> None:
        """
        Generate random shuffle per turn.

        :return: None
        """
        shuffled_deck = self.deck_of_cards
        np.random.shuffle(shuffled_deck)

        self.first_hand = shuffled_deck[0:10]
        self.second_hand = shuffled_deck[10:20]
        self.third_hand = shuffled_deck[20:30]
        self.talon = shuffled_deck[30:32]

    def _show_hand(self, hand: List) -> None:
        """
        Show hand in terms of card's value and suit.

        :param hand: List of distinct numbers
        :return: None
        """
        if np.unique(hand).size != len(hand):
            raise Exception("Invalid hand - contains duplicates.")

        for card in hand:
            print(self.card_value_dict[card % 8] +
                  self.card_suit_dict[card // 8])


Preferans.callable()


