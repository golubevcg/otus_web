import uuid
from l2_lotto_game.src.card_model import Card


class Player:

    """
    Base class, from which all players will be inherited.
    In child classes must be implemented cross_out_number or NotImplementedError will rise.
    """

    def __init__(self, name):
        if not name:
            raise ValueError("Empty name value error")

        if type(name) != str:
            raise TypeError("Wrong type, to set player name, name type must be str")

        self._name = name
        self._id = str(uuid.uuid4())
        self._card = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Empty name value error")

        if type(name) != str:
            raise TypeError("Wrong type, to set player name, name type must be str")

        self._name = name
        print(f"Player name been updated")

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card: Card):
        if not card:
            raise ValueError("Empty card value error")

        if type(card) != Card:
            raise TypeError("Wrong type, to set player card, card type must be Card")

        self._card = card
        print(f"\nPlayer card been updated")

    def cross_out_number(self, number):
        raise NotImplementedError

    def __str__(self):
        return f"{self._name}({self._id})"


class User(Player):

    """
    User player class
    """

    def cross_out_number(self, number):

        """
        Based on player decision input, crosses number in user's card or skips.
        If number in card, then it must be crossed,
        if it is not in card - then it must be skipped, this two conditions will give both True,
        False otherwise.
        :param number: number to cross in card
        :return: bool.
        """

        if not number:
            raise ValueError("Nothing to cross out, given number is empty.")

        if not self.card:
            raise ValueError("Cannot cross out number - card is not defined.")

        if type(number) != int:
            raise TypeError("Error, number to cross must be int")

        correct_num = False
        if number in self.card.numbers:
            correct_num = True

        val = input("Cross out number in card? (y/n to answer): ")
        val = self.validate_input_val(val)

        if val == "y":
            if correct_num:
                self.card.cross_out_number(number)
                return True
            else:
                return False
        elif val == "n":
            if correct_num:
                return False
            else:
                return True

    def validate_input_val(self, val: str):

        """
        Validates input given by user in infinite cycle, until proper input will be given.
        """

        if not val:
            raise ValueError("There was an error, nothing to validate, given string es empty.")

        possible_values = ["y", "n"]
        if val in possible_values:
            return val

        while True:
            val = input("Wrong input, enter 'y' to yes and cross out number in card or 'n' to continue:")
            if val not in possible_values:
                continue

            break

        return val


class Computer(Player):

    """
    Computer player class
    """

    def cross_out_number(self, number):
        if not number:
            raise ValueError("Nothing to cross out, given number is empty.")

        if not self.card:
            raise ValueError("Card is empty, cannot cross out number.")

        if number in self.card.numbers:
            self.card.cross_out_number(number)

        return True
