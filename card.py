import operator
from typing import List
from consts import CARD_SUIT_DICT, CARD_VALUE_DICT


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class MetaCard:
    def __init__(self):
        self.cards: List[Card] = []
        self.suit = None
        self.value = None
        self.capacity = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        if len(self.cards) == 1:
            self._set_metacard_suit()
            self._set_metacard_value()
        self._increase_capacity()

    def get_cards(self):
        return self.cards

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_capacity(self):
        return self.capacity

    def _set_metacard_suit(self):
        self.suit = self.cards[0].get_suit()

    def _set_metacard_value(self):
        self.value = self.cards[0].get_value()

    def _increase_capacity(self):
        self.capacity += 1
        if self.capacity == 9:
            raise ValueError("Metacard capacity is greater than 8")

    def decrease_capacity(self):
        self.capacity -= 1
        if self.capacity == -1:
            raise ValueError("Metacard capacity is less than 0")


class MetaHand:
    def __init__(self, metahand=None):
        self.metahand: List[MetaCard] = metahand if metahand is not None else []

    def add_metacard(self, metacard: MetaCard):
        self.metahand.append(metacard)

    def decrease_card_capacity(self, metacard: MetaCard):
        for mc in self.metahand:
            if (mc.get_value() == metacard.get_value()
                    and mc.get_suit() == metacard.get_suit()):
                mc.decrease_capacity()
                if mc.get_capacity() == 0:
                    self.metahand.remove(mc)

    @staticmethod
    def format_card(card: Card):
        return CARD_VALUE_DICT[card.get_value()] + CARD_SUIT_DICT[card.get_suit()]

    def show(self):
        print(f"Lenght of metahand: {len(self.metahand)}")
        print("___")
        for metacard in self.metahand:
            print("Cards in metacard: ")
            for j in range(metacard.get_capacity()):
                print(f"{self.format_card(metacard.get_cards()[j])}", end=" ")
            print(f"\n Value of metacard: {metacard.get_value()}")
            print(f" Suit of metacard: {metacard.get_suit()}")
