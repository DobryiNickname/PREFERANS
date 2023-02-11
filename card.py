class Card:
    def __init__(self, value: int, suit: int):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit
