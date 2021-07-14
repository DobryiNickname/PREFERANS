import operator

import consts


class Bot:
    def __init__(self):
        self.hand = None

    def set_hand(self, hand):
        self.hand = hand

    def show_hand(self) -> None:
        """
        Show sorted hand in terms of card's value and suit.

        :return: None
        """
        unsorted_hand = self.hand
        # Возможно передлать под кастомный запрос человека.
        sorted_hand = sorted(unsorted_hand, key=operator.attrgetter("suit", "value"), reverse=True)
        for card in sorted_hand:
            print(consts.CARD_VALUE_DICT[card.value]
                  + consts.CARD_SUIT_DICT[card.suit])

    def predict_card(self):
        # random choise -> rules?
        pass