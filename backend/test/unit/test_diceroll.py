import pytest
from src.util.helpers import diceroll
from unittest.mock import patch

# Eftersom vi importerar diceroll som i sin tur importerar modulen random
# så kan vi accessa random.randint som en modul
# Vi skapar en mock funktion på random.randint och anger return value
# Sedan kör vi diceroll funktionen som vanligt men då med den ersatta mock funktionen

@pytest.mark.patch
@pytest.mark.parametrize("roll,expected", [(1, False), (2, False), (3, False), (4, True), (5, True), (6, True)])
def test_all(roll, expected):
    with patch("src.util.helpers.random.randint") as randint_mock:
        randint_mock.return_value = roll
        assert diceroll() == expected

# If we dont use with statement to create context
# we access the patch object by injecting a object as a function param
# the patched function must be the first param
@pytest.mark.patch
@patch("src.util.helpers.random.randint")
@pytest.mark.parametrize("roll,expected", [(1, False), (2, False), (3, False), (4, True), (5, True), (6, True)])
def test_all(mocker_boy, roll, expected):
    mocker_boy.return_value = roll
    assert diceroll() == expected

