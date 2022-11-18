from utils import generate_hands_and_talon, put_card_on_table
from bot import Bot
from card import MetaHand
import consts

import copy
import time


hands = generate_hands_and_talon()

bot0 = Bot(0)
bot0.set_hand_and_metahand(hands["hand_1"])
bot0.show_hand()

bot1 = Bot(1)
bot1.set_hand_and_metahand(hands["hand_2"])
#bot1.show_hand()

bot2 = Bot(2)
bot2.set_hand_and_metahand(hands["hand_3"])
#bot2.show_hand()

bot_id_mapping = {
    0: bot0,
    1: bot1,
    2: bot2,
}

bot_order_mapping = {
    "first bot turn": [0, 1, 2],
    "second bot turn": [1, 2, 0],
    "third bot turn": [2, 0, 1],
}

start = time.time()
put_card_on_table(bot_id_mapping, bot_order_mapping["first bot turn"])
end = time.time()
print(end - start)
