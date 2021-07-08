class Card:
    def __init__(self, **kwargs):
        self.value = kwargs["value"]
        self.suit = kwargs["suit"]
        self.is_trump = None

    # Хуй знает правильно ли так делать
    def _set_trump(self, trump: bool) -> None:
        self.is_trump = trump
