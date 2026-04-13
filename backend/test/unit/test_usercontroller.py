import pytest
from unittest.mock import MagicMock, patch
from src.controllers.usercontroller import UserController

INVAL_EMAIL_MESS = 'Error: invalid email address'

class Test_user_controller:
    @pytest.fixture
    def user_controller(self, email):
        """Return a user_controller"""
        dao_mock = MagicMock()
        dao_mock.find = MagicMock(return_value=[{"email": email}])
        user_controller = UserController(dao_mock)
        return user_controller
    
    @pytest.fixture
    def user_controller_multiple_users(self, email):
        """Return a user controller with multiple users"""
        dao_mock = MagicMock()
        dao_mock.find = MagicMock(return_value=[{
            "username": "Alice",
            "email": email
            },
            {
            "username": "BOB",
            "email": email
            }])
        user_controller = UserController(dao_mock)
        return user_controller


    @pytest.mark.email
    @pytest.mark.email_invalid
    @pytest.mark.parametrize("email, expected", [
        ("name", INVAL_EMAIL_MESS), 
        ("domain.com", INVAL_EMAIL_MESS),
        ("name@", INVAL_EMAIL_MESS),
        ("@domain.com", INVAL_EMAIL_MESS),
        ("domain.com", INVAL_EMAIL_MESS),
        ("surname..name@domain.com", INVAL_EMAIL_MESS),
        (".com@", INVAL_EMAIL_MESS),
        ("surname.name@domain.com@", INVAL_EMAIL_MESS),
        ("", INVAL_EMAIL_MESS)
        ])
    def test_get_user_by_email_invalid(self, user_controller, email, expected):
        with pytest.raises(ValueError) as execinfo:
            user_controller.get_user_by_email(email)
        assert expected in str(execinfo.value)


    @pytest.mark.email
    @pytest.mark.email_valid
    @pytest.mark.parametrize("email, expected", [
        ("name@domain.com", {"email": "name@domain.com"}),
        ("name.name@domain.com", {"email": "name.name@domain.com"}),
        ("name999@domain.com", {"email": "name999@domain.com"}),
        ("name.\.name@domain.com", {"email": "name.\.name@domain.com"})
        ])
    def test_get_user_by_email_valid(self, user_controller, email, expected):
        result = user_controller.get_user_by_email(email)
        assert expected == result

    @pytest.mark.email
    @pytest.mark.email_valid_multiple_users
    @pytest.mark.parametrize("email, expected", [
        ("name@domain.com", {
            "username": "Alice",
            "email": "name@domain.com"
            })
        ])
    def test_get_user_by_email_valid(self, user_controller_multiple_users, email, expected):
        result = user_controller_multiple_users.get_user_by_email(email)
        assert expected == result



