import uuid
import random
import re

class Card:

    """
    Base class for each LottoGame card data.
    """

    def __init__(self, numbers: list):
        if len(numbers) != 15:
            raise Exception("Error, wrong numbers amount, it must be 15 numbers")
        self._id = uuid.uuid4()
        self.numbers = numbers

    @property
    def id(self):
        return self._id

    def cross_out_number(self, num: int):

        """
        Crosses out given number in card. If given num not in card numbers exception will be thrown.
        :param num: number to cross in card
        """
        if not num:
            raise Exception("Error, given number is empty.")

        if not self.check_number_in_card(num):
            raise Exception("Error, given number not exist in numbers list.")

        num_index = self.numbers.index(num)
        self.numbers[num_index] = "-"
        print("Number successfully was crossed!")

    def check_number_in_card(self, num) -> bool:

        """
        Checks if given number in numbers list
        :param num: number to check value
        :return: bool True if num in self.numbers, False otherwise
        """

        if not num:
            raise Exception("Error, given number is empty.")

        if num in self.numbers:
            return True
        else:
            return False

    def __str__(self):
        if not self.numbers or len(self.numbers) != 15:
            return

        separator = "--------------------------"

        final_string = f"{separator}\n"
        for i in range(3):
            start = 5 * i
            end = start + 5
            current_numbers_line = "    ".join(map(self.convert_int_to_str_w_spaces_for_one_digit_int,
                                                   self.numbers[start:end]))
            final_string += f"{current_numbers_line}\n"

        final_string += separator

        return final_string

    @classmethod
    def convert_int_to_str_w_spaces_for_one_digit_int(cls, val: int):

        """
        Converts given int to str, if int have only one digit,
        additional space will be added in returned string before number.
        :param val:
        :return: str updated value
        """

        regex = "[0-9]"
        if not re.search(regex, str(val)):
            return f" {str(val)}"
        elif int(val) >= 10:
            return str(val)
        else:
            return f" {str(val)}"

    @classmethod
    def generate_card(cls):

        """
        Static fabric method, which generate class instance with random numbers.
        """

        numbers_range = list(range(1, 90))
        card_numbers = random.choices(numbers_range, k=15)

        try:
            card = cls(card_numbers)
            return card
        except Exception as e:
            print(e)
            return None
