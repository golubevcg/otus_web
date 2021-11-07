from card_model import Card
from players_model import User, Computer
import random
from collections import deque

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

        self.generate_cards()

        numbers_queue = deque(range(90))
        random.shuffle(numbers_queue)

        game_over = False
        while numbers_queue or game_over:
            current_keg = numbers_queue.pop()
            print(f"\n Current keg with number:{current_keg}")
            for player in self._players_list:
                if not player.cross_out_number(current_keg):
                    game_over = True

    def generate_cards(self):
        if not self._players_list:
            raise ValueError("Error, cannot generate cards, players_list is empty")

        for player in self._players_list:
            card = Card.generate_card()

            if card:
                player.card = card
                print(f"Player {player.name} recieved this card:\n{card}")

    def generate_number_queue(self):
        pass