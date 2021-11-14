import pytest
from l2_lotto_game.src.card_model import Card


@pytest.fixture
def fixture_card_object():
    return Card(list(range(1, 16)))


def test_correct_init():
    card = Card(list(range(1, 16)))
    assert card is not None
    assert type(card) == Card
    assert type(card.numbers) == list
    assert len(card.numbers) == 15
    assert card.numbers == list(range(1, 16))
    assert type(card.id) == str and len(card.id) == 36


def test_wrong_init():
    with pytest.raises(ValueError) as exception_info:
        Card(list())
    assert "Empty numbers list error" == str(exception_info.value)

    with pytest.raises(Exception) as exception_info:
        Card(list(range(0, 19)))
    assert "Error, wrong numbers amount, it must be 15 numbers" == str(exception_info.value)

    with pytest.raises(TypeError) as exception_info:
        Card(str(list(range(1, 16))))
    assert "Given numbers type not a list" == str(exception_info.value)


def test_cross_out_correct(fixture_card_object):
    fixture_card_object.cross_out_number(1)
    assert fixture_card_object.numbers[0] == "-"


def test_cross_out_wrong(fixture_card_object):
    with pytest.raises(ValueError) as exc_info:
        fixture_card_object.cross_out_number(43)
    assert "Error, given number not exist in numbers list." == str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        fixture_card_object.cross_out_number(None)
    assert "Error, given number is empty." == str(exc_info.value)

    with pytest.raises(TypeError) as exc_info:
        fixture_card_object.cross_out_number("123")
    assert "Error, given number wrong type, must be int." == str(exc_info.value)


def test_num_in_card_correct(fixture_card_object):
    assert fixture_card_object.check_number_in_card(10)
    assert not fixture_card_object.check_number_in_card(25)
    assert not fixture_card_object.check_number_in_card(0)


def test_num_in_card_wrong(fixture_card_object):
    with pytest.raises(ValueError) as exc_info:
        fixture_card_object.check_number_in_card(None)
    assert "Error, given number is empty." == str(exc_info.value)

    with pytest.raises(TypeError) as exc_data:
        fixture_card_object.check_number_in_card("0")
    assert "Error, given number wrong type, must be int." == str(exc_data.value)


def test_card_str_repr(fixture_card_object):
    test_str = """--------------------------
 1     2     3     4     5
 6     7     8     9    10
11    12    13    14    15
--------------------------"""
    assert test_str == str(fixture_card_object)


def test_convert_int_to_str_w_spaces_correct():
    assert " 1" == Card.convert_int_to_str_w_spaces_for_one_digit_int(1)
    assert "11" == Card.convert_int_to_str_w_spaces_for_one_digit_int(11)
    assert " -" == Card.convert_int_to_str_w_spaces_for_one_digit_int("-")


def test_convert_int_to_str_w_spaces_wrong():
    with pytest.raises(ValueError) as exc_info:
        Card.convert_int_to_str_w_spaces_for_one_digit_int(None)
    assert "Error, given number is empty." == str(exc_info.value)

    with pytest.raises(TypeError) as exc_data:
        Card.convert_int_to_str_w_spaces_for_one_digit_int([0, 1, 2])
    assert "Error, given number wrong type, must be int or str." == str(exc_data.value)

    with pytest.raises(ValueError) as exc_data:
        Card.convert_int_to_str_w_spaces_for_one_digit_int(123)
    assert "Error, too large input, available only two digit numbers." == str(exc_data.value)


def test_generate_card():
    assert Card == type(Card.generate_card())
    assert None != Card.generate_card().id
    assert None != Card.generate_card().numbers