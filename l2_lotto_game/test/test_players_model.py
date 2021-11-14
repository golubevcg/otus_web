import pytest
from unittest.mock import patch
from l2_lotto_game.src.players_model import Player, User, Computer
from l2_lotto_game.src.card_model import Card


@pytest.fixture
def fixture_player_object():
    return Player("Andrew")


@pytest.fixture
def fixture_user_object():
    return User("Andrew")


@pytest.fixture
def fixture_computer_object():
    return Computer("Computer")


@pytest.fixture
def fixture_card_object():
    return Card(list(range(1, 16)))


def test_correct_init():
    player = Player("Andrew")
    assert player is not None
    assert type(player) == Player
    assert player.name == "Andrew" and type(player.name) == str
    assert type(player.id) == str and len(player.id) == 36


def test_wrong_init():
    with pytest.raises(ValueError) as exc_data:
        Player(None)
    assert str(exc_data.value) == "Empty name value error"

    with pytest.raises(TypeError) as exc_info:
        Player(1234)
    assert str(exc_info.value) == "Wrong type, to set player name, name type must be str"


def test_name_setter(fixture_player_object):
    with pytest.raises(ValueError) as exc_data:
        fixture_player_object.name = None
    assert str(exc_data.value) == "Empty name value error"

    with pytest.raises(TypeError) as exc_info:
        fixture_player_object.name = 123
    assert str(exc_info.value) == "Wrong type, to set player name, name type must be str"


def test_card_setter(fixture_player_object):
    with pytest.raises(ValueError) as exc_data:
        fixture_player_object.card = None
    assert str(exc_data.value) == "Empty card value error"

    with pytest.raises(TypeError) as exc_info:
        fixture_player_object.card = "Tralala"
    assert str(exc_info.value) == "Wrong type, to set player card, card type must be Card"


def test_player_str_repr(fixture_player_object):
    assert str(fixture_player_object).startswith(fixture_player_object.name)


def test_cross_out_exception(fixture_player_object):
    with pytest.raises(NotImplementedError) as exc_data:
        fixture_player_object.cross_out_number(123)
    assert type(exc_data.value) == NotImplementedError

    with pytest.raises(NotImplementedError) as exc_data:
        fixture_player_object.cross_out_number("123")
    assert type(exc_data.value) == NotImplementedError

    with pytest.raises(NotImplementedError) as exc_data:
        fixture_player_object.cross_out_number(None)
    assert type(exc_data.value) == NotImplementedError


def test_user_cross_out_number_wrong_args(fixture_user_object):
    with pytest.raises(ValueError) as exc_data:
        fixture_user_object.cross_out_number(None)
    assert str(exc_data.value) == "Nothing to cross out, given number is empty."

    with pytest.raises(ValueError) as exc_info:
        fixture_user_object.cross_out_number(1)
    assert str(exc_info.value) == "Cannot cross out number - card is not defined."


@patch("players_model.User.validate_input_val")
def test_user_cross_out_number_correct(mock_validate_input_val,
                                       fixture_user_object,
                                       fixture_card_object):

    # MOCK INPUT
    # MOCK VALIDATE INPUT
    pass


def test_user_cross_out_number_wrong_input_value(fixture_user_object):
    # MOCK INPUT
    # MOCK VALIDATE INPUT
    pass


def test_user_validate_input_val(fixture_user_object):
    # user validate input val
    pass


def test_computer_cross_out_number(fixture_user_object):
    # compute cross out number
    pass