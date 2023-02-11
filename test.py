from utils import generate_hands_and_talon, put_card_on_table
from bot import Bot

hands = generate_hands_and_talon()

bot0 = Bot(0, "MAXIMISE", hand=hands["hand_1"])
bot0.show_hand()

bot1 = Bot(1,"RANDOM", hand=hands["hand_2"])
bot1.show_hand()

bot2 = Bot(2, "RANDOM", hand=hands["hand_3"])
bot2.show_hand()

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

initial_bot_order = bot_order_mapping["first bot turn"]
for _ in range(10):
    print(f"Ходы до взятки -    {initial_bot_order:}")
    initial_bot_order = put_card_on_table(bot_id_mapping, initial_bot_order, 1)
    print(f"Ходы после взятки - {initial_bot_order:}")