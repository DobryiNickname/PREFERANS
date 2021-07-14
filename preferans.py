from turn import Turn


class Preferans:
    def __init__(self):
        pass

    @classmethod
    def callable(cls) -> None:
        obj = cls()
        obj.run()

    def run(self) -> None:
        self._generate_turn()

    @staticmethod
    def _generate_turn() -> None:
        turn = Turn()
        turn.run_turn()


Preferans.callable()


