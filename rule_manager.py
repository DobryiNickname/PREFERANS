import numpy as np


class RuleManager:
    def __init__(self):
        pass

    @staticmethod
    def valid_moves(metahand, metacards_on_board, trump=None):
        valid_moves = []

        # Если у бота первый ход
        if len(metacards_on_board) == 0:
            valid_moves = metahand.metahand
            return valid_moves

        first_card_suit = metacards_on_board[0].suit

        # Смотрим наличие масти первоположенной карты
        for metacard in metahand.metahand:
            if metacard.suit == first_card_suit:
                valid_moves.append(metacard)
        if len(valid_moves) != 0:
            return valid_moves

        # Смотрим наличие козыря(если назначен) в отсутствии первоположенной масти
        if trump is not None:
            for metacard in metahand.metahand:
                if metacard.suit == trump:
                    valid_moves.append(metacard)
            if len(valid_moves) != 0:
                return valid_moves

        # Оставшиеся любые карты
        valid_moves = metahand.metahand
        return valid_moves
