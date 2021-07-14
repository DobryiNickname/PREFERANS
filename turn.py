from bot import Bot
from card import Card

import numpy as np


class Turn:
    def __init__(self):
        self.first_hand = None
        self.second_hand = None
        self.third_hand = None
        self.talon = None

    def run_turn(self):
        self._deal_cards()

        bot1 = Bot(self.first_hand)
        bot2 = Bot(self.second_hand)
        bot3 = Bot(self.third_hand)

        bot1.show_hand()

    def _deal_cards(self) -> None:
        """
        Generate random shuffle per turn.

        :return: None
        """
        shuffled_deck = np.arange(32)
        np.random.shuffle(shuffled_deck)

        self.first_hand = [Card(x % 8, x // 8) for x in shuffled_deck[0:10]]
        self.second_hand = [Card(x % 8, x // 8) for x in shuffled_deck[10:20]]
        self.third_hand = [Card(x % 8, x // 8) for x in shuffled_deck[20:30]]
        self.talon = [Card(x % 8, x // 8) for x in shuffled_deck[20:30]]
