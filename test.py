from card import Card
from turn_manager import TurnManager
from bot import Bot

import operator
import time
import consts


class Node:
    def __init__(self, parent):
        self.leaves = []
        self.parent = parent
        self.triplet_value = None
        self.triplet = None

    def append_leave(self, node):
        self.leaves.append(node)

    def set_triplet(self, triplet):
        self.triplet = triplet
        if (triplet[0].value > triplet[1].value) and (triplet[0].value > triplet[2].value):
            self.triplet_value = 1
        else:
            self.triplet_value = 0


def build_tree(h1, h2, h3):
    init_tree = Node(None)
    for i in h1:
        for j in h2:
            for k in h3:
                if (k.suit == i.suit) and (j.suit == i.suit):
                    triplet = [i, j, k]
                    leave = Node(init_tree)
                    leave.set_triplet(triplet)
                    init_tree.append_leave(leave)

    return init_tree


def show_tree(tree_prm):
    for i in tree_prm.leaves:
        print("Triplet - "
              f"({consts.CARD_SUIT_DICT[i.triplet[0].suit]+consts.CARD_VALUE_DICT[i.triplet[0].value]},"
              f"{consts.CARD_SUIT_DICT[i.triplet[1].suit]+consts.CARD_VALUE_DICT[i.triplet[1].value]},"
              f"{consts.CARD_SUIT_DICT[i.triplet[2].suit]+consts.CARD_VALUE_DICT[i.triplet[2].value]})"
              f"Value of turn - {i.triplet_value}"
              )


turn = TurnManager()
hands = turn.deal_cards()
# tree = build_tree(hands[0], hands[1], hands[2])

bot1 = Bot()
bot1.set_hand_and_metahand(hands[0])
bot1.show_hand()
bot1.show_metahand()

# bot2 = Bot()
# bot2.set_hand(hands[1])
# bot2.show_hand()
#
# bot3 = Bot()
# bot3.set_hand(hands[2])
# bot3.show_hand()
#
# show_tree(tree)


