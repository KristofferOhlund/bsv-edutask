import pytest
from src.util.helpers import ValidationHelper
from unittest.mock import MagicMock


@pytest.fixture()
def mock_helper(age):
    mock_user = MagicMock() # Mock object / class
    mock_user.get = MagicMock(return_value={"age": age}) # mock function with return value
    validation_helper = ValidationHelper(mock_user)
    print("\nPARAMETER", age, "\n")
    return validation_helper


@pytest.fixture
def userid():
    return "42"


@pytest.mark.param
@pytest.mark.parametrize("age,expected", [(-1, "invalid"), (0, "underaged"), (1, "underaged"), (17, "underaged"), (18, "valid"), (19, "valid"), (119, "valid"), (120, "valid"), (121, "invalid")])
def test_validateAge(expected, mock_helper, userid):
    print("\n\n", type(mock_helper))
    result = mock_helper.validateAge(userid)
    assert result == expected
