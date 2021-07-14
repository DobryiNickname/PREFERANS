from turn_manager import TurnManager
from bot import Bot


class Preferans:
    def __init__(self):
        self.Bot_1 = Bot()
        self.Bot_2 = Bot()
        self.Bot_3 = Bot()

    @classmethod
    def callable(cls) -> None:
        obj = cls()
        obj.run()

    def run(self) -> None:
        self._generate_turn()

    def _generate_turn(self) -> None:
        turn = TurnManager(self)
        turn.run()


Preferans.callable()
