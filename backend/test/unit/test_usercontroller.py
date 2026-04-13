import pytest
from unittest.mock import MagicMock, patch
from src.controllers.usercontroller import UserController


@pytest.fixture
def user_controller(email):
    """Return a user_controller"""
    dao_mock = MagicMock()
    dao_mock.find = MagicMock(return_value=[{"email": email}])
    user_controller = UserController(dao_mock)
    return user_controller

@pytest.mark.email
@pytest.mark.parametrize("email, expected", [("name", 'Error: invalid email address'), ("domain.com", 'Error: invalid email address')])
def test_get_user_by_email(user_controller, email, expected):
    print("HELLO TEST PRINT HELLO!!!!")
    result = user_controller.get_user_by_email(email)
    print("#" * 30)
    print("RESULT: ", result)
    print("#" * 30)
    assert result == expected
