import operator


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class MetaCard:
    def __init__(self):
        self.cards = []
        self.suit = None
        self.value = None
        self.capacity = None

    def add_card(self, card: Card):
        self.cards.append(card)
        self.update_metacard_capacity()
        self.update_metacard_suit()
        self.update_metacard_value()

    def update_metacard_suit(self):
        self.suit = self.cards[0].suit

    def update_metacard_value(self):
        sorted_hand = sorted(self.cards, key=operator.attrgetter("suit", "value"), reverse=True)
        self.value = sorted_hand[0].value

    def update_metacard_capacity(self):
        self.capacity = len(self.cards)

    def decrease_capacity(self):
        self.capacity -= 1


class MetaHand:
    def __init__(self):
        self.metahand = []

    def add_metacard(self, metacard: MetaCard):
        self.metahand.append(metacard)

    def update_metahand(self):
        for metacard in self.metahand:
            if metacard.capacity == 0:
                self.metahand.remove(metacard)
