from card_model import Card
import random
from collections import deque
import re
from players_model import User, Computer
import time

class LotoGame:

    def __init__(self, players_list: list):
        if len(players_list) != 2:
            raise ValueError("Incorrect data, players list can only contain two players.")

        self._players_list = players_list

    @property
    def players_list(self):
        return self._players_list

    @players_list.setter
    def players_list(self, players_list: list):
        print("Updating players list...")
        self._players_list = players_list

    def start_game(self):

        print("Welcome to Amazing Loto Game!")
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
            for player in self._players_list:
                print(f"\n\nPlayer {player.name} turn! Player card:\n{player.card}")
                if not player.cross_out_number(current_keg):
                    game_over = True
                    curr_player_index = self._players_list.index(player)
                    winner_player = self._players_list[curr_player_index-1]
                    print(f"\nThere is no such number in this card!")
                    print(f"Game over! Player {winner_player.name} is winner!")
                    break

                # case in which all card numbers is crossed
                card_str = str(player.card)
                if not re.search(digits_regex, card_str):
                    game_over = True
                    print(f"Game over! Player {self._players_list[0].name} is winner!")
                    break

    def generate_cards(self):
        if not self._players_list:
            raise ValueError("Error, cannot generate cards, players_list is empty")

        for player in self._players_list:
            card = Card.generate_card()

            if card:
                player.card = card
                print(f"\nPlayer {player.name} received this card:\n{card}")


player1 = User("user1")
player2 = Computer("comp1")
loto_game = LotoGame([player1, player2])
loto_game.start_game()