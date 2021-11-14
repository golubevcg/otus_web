import pytest
from unittest import mock
from l2_lotto_game.src.lotto_game import LottoGame
from l2_lotto_game.src.players_model import Computer


@pytest.fixture()
def lotto_game_object_fixture():
    comp1 = Computer("comp1")
    comp2 = Computer("comp2")
    return LottoGame([comp1, comp2])


def test_correct_init():
    comp1 = Computer("comp1")
    comp2 = Computer("comp2")
    lotto_game = LottoGame([comp1, comp2])
    assert lotto_game.players_list


def test_wrong_init(lotto_game_object_fixture):
    with pytest.raises(ValueError) as empty_error:
        lotto_game = LottoGame(list())
    assert str(empty_error.value) == "Wrong value, given players list is empty. " \
                                     "To create LottoGame instance, " \
                                     "provide correct list with players."

    comp1 = Computer("comp1")
    with pytest.raises(ValueError) as val_error:
        lotto_game = LottoGame([comp1])
    assert str(val_error.value) == "Game can be played only with 2 players or more."

    with pytest.raises(TypeError) as type_error:
        lotto_game = LottoGame(["tralala"])
    assert str(type_error.value) == "Wrong type, each player in list must be User, Computer or other class" \
                                    " inherited from Player class."


def test_generate_cards(lotto_game_object_fixture):
    lotto_game_object_fixture.generate_cards()
    users = lotto_game_object_fixture.players_list
    assert users[0].card
    assert users[1].card


def test_check_game_started(capfd , lotto_game_object_fixture):
    lotto_game_object_fixture.start_game()
    out, err = capfd.readouterr()
    assert "Starting game! Let's go!" in out
    assert out.count("--------Current keg number") > 1
    assert "Game Over!" in out


@mock.patch.object(LottoGame, "generate_cards")
def test_check_game_started_function_calls(mocker, lotto_game_object_fixture):
    with pytest.raises(ValueError):
        lotto_game_object_fixture.start_game()
    mocker.assert_called_once()