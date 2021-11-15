from l2_lotto_game.src.lotto_game import LottoGame
from l2_lotto_game.src.players_model import Computer

if __name__ == "__main__":
    player1 = Computer("comp1")
    player2 = Computer("comp2")

    lotto_game = LottoGame([player1, player2])
    lotto_game.start_game()