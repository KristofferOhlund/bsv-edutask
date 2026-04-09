import pytest
from src.util.helpers import ValidationHelper
from unittest.mock import MagicMock


@pytest.fixture(params=["age"])
def mock_factory(request):
    mock_user = MagicMock() # Mock object / class
    mock_user.get = MagicMock(return_value={"age": request.param}) # mock function with return value
    validation_helper = ValidationHelper(mock_user)
    print("PARAMETER", request.params, "\n\n")
    return validation_helper


# @pytest.fixture
# def helper_factory():
#     # private, only used through parent.
#     def _validation_helper_creator(3):
#         mock_user = MagicMock()
#         mock_user.get = MagicMock(return_value={"age": age})
#         validation_helper = ValidationHelper(mock_user)
#         return validation_helper
#     return _validation_helper_creator


@pytest.fixture
def userid():
    return "42"


@pytest.mark.param
@pytest.mark.parametrize("age,expected", [(-1, "invalid"), (0, "underaged"), (1, "underaged"), (17, "underaged"), (18, "valid"), (19, "valid"), (119, "valid"), (120, "valid"), (121, "invalid")])
def test_validateAge(age, expected, userid, mock_factory):
    # helper = mock_factory(age)
    assert mock_factory.validateAge(userid) == expected
