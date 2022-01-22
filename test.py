from turn_manager import TurnManager
from rule_manager import RuleManager
from bot import Bot

import consts

import copy
import time


class Node:
    def __init__(self):
        self.leaves = []
        self.bot_0_score = None
        self.bot_1_score = None
        self.bot_2_score = None
        self.triplet = None

        self.bot_game_score = None
        self.bot_whist_score = None

        self.triplet_value = None

    def append_leave(self, node):
        self.leaves.append(node)

    def set_triplet_value(self, triplet):
        self.triplet = triplet
        if (triplet[0].value > triplet[1].value) and (triplet[0].value > triplet[2].value):
            self.triplet_value = 1
        else:
            self.triplet_value = 0


def build_tree(mh_0, mh_1, mh_2, recursion_level, current_order, trump=0, id_bot_game=0):

    if recursion_level == 0:
        return Node()

    ruleman = RuleManager()

    # Терминальная нода, пустая, хранит все возможные ходы данного уровня рекурсии
    init_node = Node()

    # Просто руки ботов в списке
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

                new_order = set_order_after_trick(turn_node.triplet, trump)
                turn_node.bot_0_score = int(new_order[0] == 0)
                turn_node.bot_1_score = int(new_order[0] == 1)
                turn_node.bot_2_score = int(new_order[0] == 2)

                turn_node.append_leave(
                    build_tree(
                        copy_mh_0, copy_mh_1, copy_mh_2, recursion_level - 1, new_order,
                        trump=trump
                    )
                )

                init_node.append_leave(turn_node)


        metacards_on_board = []

    #if current_order[0] == id_bot_game:
    #    init_node.bot_game_score = any([getattr(leave, "bot_"+str(id_bot_game)+"_score") == 1 for leave in init_node.leaves])

    return init_node


def set_order_after_trick(triplet, trump):
    """Return order of bot_id"""
    if not any([card.suit == trump for card in triplet]):
        trump = triplet[0].suit

    check_trump_cards = []
    for index, card in enumerate(triplet):
        if card.suit == trump:
            check_trump_cards.append((index, card))

    sort_check = sorted(check_trump_cards, key=lambda x: x[1].value, reverse=True)

    if sort_check[0][0] == 0:
        return [0, 1, 2]
    elif sort_check[0][0] == 1:
        return [1, 2, 0]
    else:
        return [2, 0, 1]


def show_tree(tree_prm, tab):
    if len(tree_prm.leaves) == 0:
        return

    for leave in tree_prm.leaves:
        print("\t" * tab, end="")
        print("Triplet - "
              f"({consts.CARD_VALUE_DICT[leave.triplet[0].value] + consts.CARD_SUIT_DICT[leave.triplet[0].suit]},"
              f"{consts.CARD_VALUE_DICT[leave.triplet[1].value] + consts.CARD_SUIT_DICT[leave.triplet[1].suit]},"
              f"{consts.CARD_VALUE_DICT[leave.triplet[2].value] + consts.CARD_SUIT_DICT[leave.triplet[2].suit]})"
              )
        show_tree(leave.leaves[0], tab+1)


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

start = time.time()
tree = build_tree(
    bot0.meta_hand, bot1.meta_hand, bot2.meta_hand, 2, [0, 1, 2], trump=0, id_bot_game=1
)
end = time.time()
print(end-start)

#show_tree(tree, 0)


