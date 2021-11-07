import uuid
from card_model import Card
import random

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
        print(f"Player name been updated")

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card: Card):
        """

        :type card: object
        """
        if type(card) != Card:
            raise TypeError("Wrong type, to set player card, card type must be Card")

        self._card = card
        print(f"\nPlayer card been updated")

    def cross_out_number(self, number):
        raise NotImplementedError

    def __str__(self):
        return f"{self._name}({str(self._id)})"


class User(Player):
    def cross_out_number(self, number):
        if not number:
            print("Nothing to cross out, given number is empty.")
            return

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
        if not val:
            print("There was an error, nothing to validate, given string es empty.")

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
    def cross_out_number(self, number):
        if not number:
            print("Nothing to cross out, given number is empty.")
            return

        if number in self.card.numbers:
            self.card.cross_out_number(number)

        return True