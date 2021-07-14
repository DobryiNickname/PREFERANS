import numpy as np
import consts


class Bot:
    def __init__(self, hand):
        self.hand = hand

    def show_hand(self) -> None:
        """
        Show hand in terms of card's value and suit.

        :param hand: List of cards
        :return: None
        """
        for card in self.hand:
            print(consts.CARD_VALUE_DICT[card.value]
                  + consts.CARD_SUIT_DICT[card.suit])
