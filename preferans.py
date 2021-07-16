# import pandas as pd
import numpy as np

from bot import Bot
from card import Card
from turn_manager import TurnManager
from trade_manager import TradeManager
from rule_manager import RuleManager

import consts


class Preferans:
    def __init__(self):
        self.Bot_1 = Bot()
        self.Bot_2 = Bot()
        self.Bot_3 = Bot()

        self.rules = RuleManager()

        self.PointsDf = consts.SCORE_TABLE

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

        # trade.begin_trade(b1, b2, b3)
        # turn.set_game_specifications(trade...)

        # test
        turn.cards_on_board = np.array([Card(8, 2)])
        turn.trump = 3
        valid_moves = self.rules.valid_moves(
                self.Bot_1.hand,
                turn.cards_on_board,
                turn.trump
            )
        self.Bot_1.show_valid_moves(valid_moves)
        # end test

        # The game itself
        for _ in range(10):
            pass

        return turn

    def _update_table(self, turn):
        pass


Preferans.callable()
