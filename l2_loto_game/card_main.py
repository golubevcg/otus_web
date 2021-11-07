import uuid
import player_main


class Card:

    def __init__(self, numbers: list, player: player_main.Player):
        self._player = player
        if len(numbers) != 15:
            raise Exception("Error, wrong numbers amount, it must be 15 numbers")
        self._id = uuid.uuid4()
        self.numbers = numbers

    @property
    def id(self):
        return self._id

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player: player.Player):
        if type(player) != player.Player:
            raise TypeError("Wrong type, to set player, type must be Player")

        self._player = player
        print(f"In card ({str(self._id)}), player been updated from: {self._player} to: {player}")

    def cross_out_number(self, num: int):
        if not num:
            raise Exception("Error, given number is empty.")

        if not self.check_number_in_card(num):
            raise Exception("Error, given number not exist in numbers list.")

        num_index = self.numbers.index(num)
        self.numbers[num_index] = "-"
        print("Number successfully was crossed!")

    def check_number_in_card(self, num) -> bool:

        if not num:
            raise Exception("Error, given number is empty.")

        if num in self.numbers:
            return True
        else:
            return False

    def __str__(self):
        if not self.numbers or len(self.numbers) != 15:
            return

        separator = "--------------------------\n"

        final_string = separator
        for i in range(3):
            start = 5 * i
            end = start + 5
            current_numbers_line = "    ".join(map(self.convert_int_to_str_w_spaces_for_one_digit_int, self.numbers[start:end]))
            final_string += f"{current_numbers_line}\n"

        final_string += separator

        return final_string

    @classmethod
    def convert_int_to_str_w_spaces_for_one_digit_int(cls, val: int):
        if val >= 10:
            return str(val)
        else:
            return f" {str(val)}"


test_player = player_main.Player("Vasya")
test_card = Card(list(range(15)), test_player)
print(test_card)
print(test_card.player)
test_player1 = player_main.Player("Alina")
test_card.player = test_player1
print(test_card)
