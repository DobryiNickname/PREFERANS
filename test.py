import pandas as pd
from typing import List


from utils import generate_hands_and_talon, put_card_on_table
from bot import Bot

class RoundPlay():
    def __init__(self):
        hands = generate_hands_and_talon()

        self.bot0 = Bot(0, "MAXIMISE", hand=hands["hand_1"])
        self.bot0.show_hand()

        self.bot1 = Bot(1,"RANDOM", hand=hands["hand_2"])
        self.bot1.show_hand()

        self.bot2 = Bot(2, "RANDOM", hand=hands["hand_3"])
        self.bot2.show_hand()

        self.bot_id_mapping = {
            0: self.bot0,
            1: self.bot1,
            2: self.bot2,
        }

        self.bot_order_mapping = {
            "first bot turn": [0, 1, 2],
            "second bot turn": [1, 2, 0],
            "third bot turn": [2, 0, 1],
        }

        self.result_table = {
            "Bot_0_trick_score": 0,
            "Bot_1_trick_score": 0,
            "Bot_2_trick_score": 0,
        }

    def run(self):
        initial_bot_order = self.bot_order_mapping["first bot turn"] # нужен итератор по кругу

        for _ in range(10):
            initial_bot_order = put_card_on_table(self.bot_id_mapping, initial_bot_order, 1) # нужен baseline для определения козыря
            self.add_trick_to_table(initial_bot_order)

        self.show_round_result()

    def add_trick_to_table(self, bot_order_after_trick: List[int]):
        self.result_table[f"Bot_{bot_order_after_trick[0]}_trick_score"] += 1

    def show_round_result(self):
        res_df = pd.DataFrame(self.result_table, index=[0])
        print(res_df)

round = RoundPlay()
round.run()