import numpy as np


class RuleManager:
    def __init__(self):
        pass

    @staticmethod
    def valid_moves(hand, cards_on_board, trump=None):
        valid_moves = np.array([])

        # Если у бота первый ход
        if len(cards_on_board) == 0:
            valid_moves = hand
            return valid_moves

        first_card_suit = cards_on_board[0].suit

        # Смотрим наличие масти первоположенной карты
        for card in hand:
            if card.suit == first_card_suit:
                valid_moves = np.append(valid_moves, card)
        if len(valid_moves) != 0:
            return valid_moves

        # Смотрим наличие козыря(если назначен) в отсутствии первоположенной масти
        if trump is not None:
            for card in hand:
                if card.suit == trump:
                    valid_moves = np.append(valid_moves, card)
            if len(valid_moves) != 0:
                return valid_moves

        # Оставшиеся любые карты
        valid_moves = hand
        return valid_moves
