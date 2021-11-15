from l2_lotto_game.src.card_model import Card
import random
from collections import deque
import re
from l2_lotto_game.src.players_model import User, Computer
import time

class LottoGame:

    """
    Main class for LottoGame.
    """

    def __init__(self, players_list: list):
        if not players_list:
            raise ValueError("Wrong value, given players list is empty. "
                             "To create LottoGame instance, "
                             "provide correct list with players.")

        if type(players_list) != list:
            raise TypeError("Wrong type, to create LottoGame instance, provide list with players.")

        for player in players_list:
            if not isinstance(player, (User, Computer)):
                raise TypeError("Wrong type, each player in list must be User, Computer or other class"
                                " inherited from Player class.")
                break

        if len(players_list) < 2:
            raise ValueError("Game can be played only with 2 players or more.")


        self._players_list = players_list

    @property
    def players_list(self):
        return self._players_list

    @players_list.setter
    def players_list(self, players_list: list):
        print("Updating players list...")
        self._players_list = players_list

    def start_game(self):

        """
        Main game function, which start game cycle.
        """

        print("Welcome to Amazing Lotto Game!")
        print("Generating cards...")
        self.generate_cards()

        print("Mixing values...")
        numbers_queue = deque(range(1, 90))
        random.shuffle(numbers_queue)

        time.sleep(1)
        print("Brewing coffee...")
        time.sleep(1)

        digits_regex = re.compile("[0-9]")
        game_over = False
        print("Starting game! Let's go!")
        while numbers_queue and not game_over:
            current_keg = numbers_queue.pop()
            print(f"\n\n--------Current keg number:{current_keg}")

            for player in self._players_list[:]:
                print(f"\n\nPlayer {player.name} turn! Player card:\n{player.card}")
                if not player.cross_out_number(current_keg):
                    print(f"\nThere is no such number in this card!")
                    print(f"Player {player.name} lost!")
                    self._players_list.remove(player)
                    if len(self._players_list) == 1:
                        game_over = True
                        break

                # case in which all card numbers is crossed
                card_str = str(player.card)
                if not re.search(digits_regex, card_str):
                    game_over = True
                    print(f"Player {self._players_list[0].name} is winner!")
                    break

            if len(self._players_list) == 1:
                game_over = True
                print(f"Player {self._players_list[0].name} is winner!")

        print("Game Over!")

    def generate_cards(self):

        """
        Generates cards for each user
        """

        if not self._players_list:
            raise ValueError("Error, cannot generate cards, players_list is empty")

        for player in self._players_list:
            card = Card.generate_card()

            if card:
                player.card = card
                print(f"\nPlayer {player.name} received this card:\n{card}")


