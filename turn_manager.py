from card import Card

import numpy as np


class TurnManager:
    def __init__(self):
        self.talon = None
        self.order = None
        self.trump = None
        self.cards_on_board = None

    def deal_cards(self) -> list:
        """
        Generate random shuffle per turn.

        :return: List of hands
        """
        shuffled_deck = np.arange(32)
        np.random.shuffle(shuffled_deck)

        hands = [
            [Card(x % 8, x // 8) for x in shuffled_deck[0:10]],
            [Card(x % 8, x // 8) for x in shuffled_deck[10:20]],
            [Card(x % 8, x // 8) for x in shuffled_deck[20:30]]
        ]

        self.talon = [Card(x % 8, x // 8) for x in shuffled_deck[30:32]]

        return hands

    def trick_and_order(self):
        pass
