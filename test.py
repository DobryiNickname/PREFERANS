from turn_manager import TurnManager
from rule_manager import RuleManager
from bot import Bot

import consts


class Node:
    def __init__(self):
        self.leaves = []
        self.parent = None
        self.bot_0_score = None
        self.bot_1_score = None
        self.bot_2_score = None
        self.triplet = None

        self.triplet_value = None

    def append_leave(self, node):
        self.leaves.append(node)

    def set_parent(self, parent):
        self.parent = parent

    def set_triplet_value(self, triplet):
        self.triplet = triplet
        if (triplet[0].value > triplet[1].value) and (triplet[0].value > triplet[2].value):
            self.triplet_value = 1
        else:
            self.triplet_value = 0


def build_tree(bot_0, bot_1, bot_2,
               parent, recursion_level, current_order, trump=0):

    if recursion_level == 9:
        return None

    ruleman = RuleManager()

    init_node = Node()
    init_node.set_parent(parent)

    # Просто боты в списке
    bot_list = [bot_0, bot_1, bot_2]
    # Тут будут боты в правильной последовательности
    bot_order = []
    for id in current_order:
        for bot in bot_list:
            if bot.bot_id == id:
                bot_order.append(bot)

    metacards_on_board = []
    zero_hand = ruleman.valid_moves(bot_order[0].meta_hand, metacards_on_board, trump=trump)
    for mc_0 in zero_hand:
        metacards_on_board.append(mc_0)
        first_hand = ruleman.valid_moves(bot_order[1].meta_hand, metacards_on_board, trump=trump)
        for mc_1 in first_hand:
            second_hand = ruleman.valid_moves(bot_order[2].meta_hand, metacards_on_board, trump=trump)
            for mc_2 in second_hand:
                init_node.triplet = [mc_0, mc_1, mc_2]

                # Присвоение очков за ход
                if mc_0.suit == trump: # Проверям, положен ли козырь
                    pass
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


