import pytest
from src.util.helpers import ValidationHelper
from unittest.mock import MagicMock

@pytest.fixture
def helper_factory():
    # private, only used through parent.
    def _validation_helper_creator(age):
        mock_user = MagicMock()
        mock_user.get = MagicMock(return_value={"age": age})
        validation_helper = ValidationHelper(mock_user)
        return validation_helper
    return _validation_helper_creator


@pytest.fixture
def userid():
    return "42"


@pytest.mark.unit
@pytest.mark.parametrize("test_input,expected", [(-1, "invalid"), (0, "underaged"), (1, "underaged"), (17, "underaged"), (18, "valid"), (19, "valid"), (119, "valid"), (120, "valid"), (121, "invalid")])
def test_validateAge(test_input, expected, userid, helper_factory):
    helper = helper_factory(test_input)
    assert helper.validateAge(userid) == expected
