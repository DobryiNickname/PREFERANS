import operator
import consts
from typing import List

from card import Card, MetaCard, MetaHand


class Bot:
    def __init__(self):
        self.hand = None
        self.meta_hand = None

    def set_hand_and_metahand(self, hand: List[Card]):
        self.hand = hand

        sort_hand = sorted(hand, key=operator.attrgetter("suit", "value"), reverse=True)
        meta_hand = MetaHand()
        # Цикл по мастям для создания массива одномастных карт
        for i in range(4):
            single_suit = []
            for j in sort_hand:
                if j.suit == i:
                    single_suit.append(j)
            # Помещаем соседние по силе карты в метакарту
            if len(single_suit) != 0:
                meta_card = MetaCard()
                meta_card.add_card(single_suit[0])
                for k in range(1, len(single_suit)):
                    if single_suit[k].value + 1 == single_suit[k - 1].value:
                        meta_card.add_card(single_suit[k])
                    else:
                        meta_hand.add_metacard(meta_card)
                        meta_card = MetaCard()
                        meta_card.add_card(single_suit[k])
                if meta_card.capacity != 0:
                    meta_hand.add_metacard(meta_card)

        self.meta_hand = meta_hand

    @staticmethod
    def format_card(card_in: Card):
        return consts.CARD_VALUE_DICT[card_in.value] + consts.CARD_SUIT_DICT[card_in.suit]

    def show_hand(self) -> None:
        """
        Show sorted hand in terms of card's value and suit.
        :return: None
        """
        unsorted_hand = self.hand
        # Возможно передлать под кастомный запрос человека.
        sorted_hand = sorted(unsorted_hand, key=operator.attrgetter("suit", "value"), reverse=True)
        for card in sorted_hand:
            print(self.format_card(card), end=" ")
        print("\n")

    def show_metahand(self):
        print(f"Lenght of metahand: {len(self.meta_hand.metahand)}")
        print("___")
        for metacard in self.meta_hand.metahand:
            print("Cards in metacard: ")
            for j in range(metacard.capacity):
                print(f"{self.format_card(metacard.cards[j])}", end=" ")
            print(f"\n Value of metacard: {metacard.value}")
            print(f"Suit of metacard: {metacard.suit}")

    # Это старый рандомный код, мб удалить нах
    @staticmethod
    def show_valid_moves(valid_moves):
        unsorted_hand = valid_moves
        # Возможно передлать под кастомный запрос человека.
        sorted_hand = sorted(unsorted_hand, key=operator.attrgetter("suit", "value"), reverse=True)
        for card in sorted_hand:
            print(consts.CARD_VALUE_DICT[card.value]
                  + consts.CARD_SUIT_DICT[card.suit])
