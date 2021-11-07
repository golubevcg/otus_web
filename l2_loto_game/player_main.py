import uuid
import card_main


class Player:
    def __init__(self, name):
        self._name = name
        self._id = uuid.uuid4()
        self._card = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if type(name) != str:
            raise TypeError("Wrong type, to set player name, name type must be str")

        self._name = name
        print(f"Player name been updated from: {self._name} to: {name}")

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card: card_main.Card):
        """

        :type card: object
        """
        if type(card) != str:
            raise TypeError("Wrong type, to set player card, card type must be Card")

        self._card = card
        print(f"Player card been updated from: {self._card} to: {card}")

    def cross_out_number(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self._name}({str(self._id)})"
