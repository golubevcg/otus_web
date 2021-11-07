


# add top class to inherit from, where you will set all base functions
# this must be implemented like in lecture been said with 100% implemented
# from him we will inherit user class and computer class
class User(Player):
    def __init__(self, username):
        self.username = username
        self.card = None

    # replace with correct setter with proper type
    def set_card(self, card: Card):
        self.card = card


class LotoGame:

    def __init__(self, players_list: list):
        self.players_list = players_list
        self.player_card_mapping = dict()
        self.card_free_numbers = set(range(90))

    def generate_cards(self):
        for player in self.players_list:
            selected_numbers = self.generate_new_card_numbers()
            new_card = Card(selected_numbers, player)
            player.set_card(new_card)
            self.player_card_mapping[player] = new_card

    def generate_new_card_numbers(self) -> list:
        if not self.card_free_numbers:
            print("Error, there is no free numbers available!")

        card_numbers = random.choices(list(self.card_free_numbers), k=15)
        self.card_free_numbers = self.card_free_numbers.difference(set(card_numbers))

        return card_numbers


test_player = Player("Vasya")
test_card = Card(list(range(15)), test_player)
print(test_card)
print(test_card.player)
test_player1 = Player("Alina")
test_card.player = test_player1
print(test_card)
