# import pandas as pd

from bot import Bot
from turn_manager import TurnManager
from trade_manager import TradeManager

import consts


class Preferans:
    def __init__(self):
        self.Bot_1 = Bot()
        self.Bot_2 = Bot()
        self.Bot_3 = Bot()

        self.PointsDf = consts.TABLE

    @classmethod
    def callable(cls) -> None:
        obj = cls()
        obj.run()

    def run(self) -> None:
        # while true:
        turn = self._start_turn()
        self._update_table(turn)

    def _start_turn(self) -> TurnManager:
        turn = TurnManager()
        trade = TradeManager()

        hands = turn.deal_cards()
        self.Bot_1.set_hand(hands[0])
        self.Bot_2.set_hand(hands[1])
        self.Bot_3.set_hand(hands[2])

        self.Bot_3.show_hand()

        return turn

    def _update_table(self, turn):
        pass


Preferans.callable()
