import operator
import consts
from typing import List

from card import Card, MetaCard, MetaHand
from consts import CARD_SUIT_DICT, CARD_VALUE_DICT


class Bot:
    def __init__(self, bot_id, hand=None, meta_hand=None):
        self.hand: List[Card] = hand
        self.meta_hand: MetaHand = meta_hand
        self.bot_id = bot_id

    def set_hand_and_metahand(self, hand: List[Card]):
        sort_hand = sorted(hand, key=operator.attrgetter("suit", "value"), reverse=True)
        self.hand = sort_hand
        meta_hand = MetaHand()
        # Цикл по мастям для создания массива одномастных карт
        for suit in range(4):
            single_suit: List[Card] = []
            for card in sort_hand:
                if card.get_suit() == suit:
                    single_suit.append(card)
            # Помещаем соседние по силе карты в метакарту
            if len(single_suit) != 0:
                meta_card = MetaCard()
                meta_card.add_card(single_suit[0])
                for k in range(1, len(single_suit)):
                    if single_suit[k].get_value() + 1 == single_suit[k - 1].get_value():
                        meta_card.add_card(single_suit[k])
                    else:
                        meta_hand.add_metacard(meta_card)
                        meta_card = MetaCard()
                        meta_card.add_card(single_suit[k])
                if meta_card.get_capacity() != 0:
                    meta_hand.add_metacard(meta_card)

        self.meta_hand = meta_hand

    @staticmethod
    def format_card(card: Card):
        return CARD_VALUE_DICT[card.get_value()] + CARD_SUIT_DICT[card.get_suit()]

    # deprecated
    def show_hand(self) -> None:
        """
        Show sorted hand in terms of card's value and suit.
        :return: None
        """
        unsorted_hand = self.hand
        if len(self.hand) == 0:
            print(f"I'm bot {self.bot_id}. My hand is empty(")
        # Возможно передлать под кастомный запрос человека.
        sorted_hand = sorted(unsorted_hand, key=operator.attrgetter("suit", "value"), reverse=True)
        for card in sorted_hand:
            print(self.format_card(card), end=" ")
        print("\n")

