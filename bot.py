from card import Card


class Bot:
    def __init__(self):
        self.hand = None

    def _deal_card(self) -> Card:
        """
        Deal card from hand

        :return: Card from hand
        """