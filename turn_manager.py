from card import Card

import numpy as np


class TurnManager:
    def __init__(self, pref):
        self.talon = None
        # Узнать у шарящих людей можно ли так делать?
        self.pref = pref

    def run(self):
        self._deal_cards()
        self.pref.Bot_1.show_hand()

    def _deal_cards(self) -> None:
        """
        Generate random shuffle per turn.

        :return: None
        """
        shuffled_deck = np.arange(32)
        np.random.shuffle(shuffled_deck)

        self.pref.Bot_1.set_hand([Card(x % 8, x // 8) for x in shuffled_deck[0:10]])
        self.pref.Bot_2.set_hand([Card(x % 8, x // 8) for x in shuffled_deck[10:20]])
        self.pref.Bot_3.set_hand([Card(x % 8, x // 8) for x in shuffled_deck[20:30]])

        self.talon = [Card(x % 8, x // 8) for x in shuffled_deck[20:30]]
