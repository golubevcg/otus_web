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


def test_user_cross_out_number_wrong_args(fixture_user_object, fixture_card_object):
    with pytest.raises(ValueError) as exc_data:
        fixture_user_object.cross_out_number(None)
    assert str(exc_data.value) == "Nothing to cross out, given number is empty."

    with pytest.raises(ValueError) as exc_info:
        fixture_user_object.cross_out_number(1)
    assert str(exc_info.value) == "Cannot cross out number - card is not defined."

    fixture_user_object.card = fixture_card_object
    with pytest.raises(TypeError) as exc_inf:
        fixture_user_object.cross_out_number("1")
    assert str(exc_inf.value) == "Error, number to cross must be int"


@patch("l2_lotto_game.src.players_model.User.validate_input_val", return_value="y")
@patch("builtins.input", return_value="y")
def test_user_cross_out_number_correct_y(validate_input_val_mock, input_val_mock,
                                         fixture_user_object, fixture_card_object):
    fixture_user_object.card = fixture_card_object
    assert fixture_user_object.cross_out_number(1)
    validate_input_val_mock.assert_called_once()
    input_val_mock.assert_called_once()


@patch("l2_lotto_game.src.players_model.User.validate_input_val", return_value="n")
@patch("builtins.input", return_value="n")
def test_user_cross_out_number_correct_n(validate_input_val_mock, input_val_mock,
                                         fixture_user_object, fixture_card_object):
    fixture_user_object.card = fixture_card_object
    assert fixture_user_object.cross_out_number(25)
    validate_input_val_mock.assert_called_once()
    input_val_mock.assert_called_once()


@patch("builtins.input", return_value="y")
def test_user_validate_input_val_correct(input_mock, fixture_user_object):
    assert "y" == fixture_user_object.validate_input_val("y")
    assert "n" == fixture_user_object.validate_input_val("n")

    input_mock.return_value = "n"
    fixture_user_object.validate_input_val("test")
    input_mock.assert_called_once()


def test_user_validate_input_val_wrong(fixture_user_object):
    with pytest.raises(ValueError) as val_err:
        fixture_user_object.validate_input_val(None)
    assert str(val_err.value) == "There was an error, nothing to validate, given string es empty."


def test_computer_cross_out_number_correct(fixture_computer_object, fixture_card_object):
    fixture_computer_object.card = fixture_card_object
    assert fixture_computer_object.cross_out_number(1)


def test_computer_cross_out_number_wrong(fixture_computer_object, fixture_card_object):
    with pytest.raises(ValueError) as val_error:
        fixture_computer_object.cross_out_number(1)
    assert str(val_error.value) == "Card is empty, cannot cross out number."

    fixture_computer_object.card = fixture_card_object
    with pytest.raises(ValueError) as val_err:
        fixture_computer_object.cross_out_number(None)
    assert str(val_err.value) == "Nothing to cross out, given number is empty."