from turn_manager import TurnManager
from rule_manager import RuleManager
from bot import Bot

import consts

import copy


class Node:
    def __init__(self):
        self.leaves = []
        self.bot_0_score = None
        self.bot_1_score = None
        self.bot_2_score = None
        self.triplet = None

        self.triplet_value = None

    def append_leave(self, node):
        self.leaves.append(node)

    def set_triplet_value(self, triplet):
        self.triplet = triplet
        if (triplet[0].value > triplet[1].value) and (triplet[0].value > triplet[2].value):
            self.triplet_value = 1
        else:
            self.triplet_value = 0


def build_tree(mh_0, mh_1, mh_2, recursion_level, current_order, trump=0):

    if recursion_level == 0:
        return Node()

    ruleman = RuleManager()

    init_node = Node()

    # Просто боты в списке
    mh_list = [mh_0, mh_1, mh_2]
    # Тут будут боты в правильной последовательности
    mh_order = []
    for id in current_order:
        mh_order.append(mh_list[id])

    metacards_on_board = []

    zero_hand = ruleman.valid_moves(mh_order[0], metacards_on_board, trump)
    for mc_0 in zero_hand:
        metacards_on_board.append(mc_0)
        first_hand = ruleman.valid_moves(mh_order[1], metacards_on_board, trump)
        for mc_1 in first_hand:
            second_hand = ruleman.valid_moves(mh_order[2], metacards_on_board, trump)
            for mc_2 in second_hand:
                turn_node = Node()
                turn_node.triplet = [mc_0, mc_1, mc_2]

                copy_mh_0 = copy.deepcopy(mh_0)
                copy_mh_0.decrease_capacity(turn_node.triplet[current_order.index(0)])
                copy_mh_0.update_metahand()
                copy_mh_1 = copy.deepcopy(mh_1)
                copy_mh_1.decrease_capacity(turn_node.triplet[current_order.index(1)])
                copy_mh_1.update_metahand()
                copy_mh_2 = copy.deepcopy(mh_2)
                copy_mh_2.decrease_capacity(turn_node.triplet[current_order.index(2)])
                copy_mh_2.update_metahand()

                turn_node.append_leave(
                    build_tree(
                        copy_mh_0, copy_mh_1, copy_mh_2, recursion_level - 1, current_order,
                        trump=trump
                    )
                )

                init_node.append_leave(turn_node)

        metacards_on_board = []

    return init_node


def set_order_after_trick(metacard_1, metacard_2, metacard_3):
    """Return order of bot_id"""
    if (metacard_1.value > metacard_2.value) and (metacard_1.value > metacard_3.value):
        return [0, 1, 2]
    elif (metacard_2.value > metacard_1.value) and (metacard_2.value > metacard_3.value):
        return [2, 0, 1]
    else:
        return [1, 2, 0]


def show_tree(tree_prm):
    for i in tree_prm.leaves:
        print("Triplet - "
              f"({consts.CARD_VALUE_DICT[i.triplet[0].value]+consts.CARD_SUIT_DICT[i.triplet[0].suit]},"
              f"{consts.CARD_VALUE_DICT[i.triplet[1].value]+consts.CARD_SUIT_DICT[i.triplet[1].suit]},"
              f"{consts.CARD_VALUE_DICT[i.triplet[2].value]+consts.CARD_SUIT_DICT[i.triplet[2].suit]})"
              # f"Value of turn - {i.triplet_value}"
              )


turn = TurnManager()
hands = turn.deal_cards()


bot0 = Bot(0)
bot0.set_hand_and_metahand(hands[0])
bot0.show_hand()

bot1 = Bot(1)
bot1.set_hand_and_metahand(hands[1])
bot1.show_hand()

bot2 = Bot(2)
bot2.set_hand_and_metahand(hands[2])
bot2.show_hand()

tree = build_tree(
    bot0.meta_hand, bot1.meta_hand, bot2.meta_hand, 1, [0, 1, 2], trump=0
)

show_tree(tree)


