import pytest
from unittest.mock import MagicMock, patch
from src.controllers.usercontroller import UserController

INVAL_EMAIL_MSG = 'Error: invalid email address'

class Test_user_controller:
    # Define a mock which return a user object {email: email}
    @pytest.fixture
    def user_controller(self, email):
        """Return a user_controller"""
        dao_mock = MagicMock()
        dao_mock.find = MagicMock(return_value=[{"email": email}])
        user_controller = UserController(dao_mock)
        return user_controller
    

    # Define a mock which return-value is an array of users
    # assosciated with the same adress
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

    # Test invalid emails using user_controller fixture
    @pytest.mark.email
    @pytest.mark.email_invalid
    @pytest.mark.parametrize("email, expected", [
        ("name", INVAL_EMAIL_MSG), 
        ("domain.com", INVAL_EMAIL_MSG),
        ("name@", INVAL_EMAIL_MSG),
        ("@domain.com", INVAL_EMAIL_MSG),
        ("domain.com", INVAL_EMAIL_MSG),
        ("surname..name@domain.com", INVAL_EMAIL_MSG),
        (".com@", INVAL_EMAIL_MSG),
        ("surname.name@domain.com@", INVAL_EMAIL_MSG),
        ("", INVAL_EMAIL_MSG)
        ])
    def test_get_user_by_email_invalid(self, user_controller, email, expected):
        """Test validation with malformatted email addresses"""
        with pytest.raises(ValueError) as execinfo:
            user_controller.get_user_by_email(email)
        assert expected in str(execinfo.value)

    # Test valid emails using user_controller fixture
    @pytest.mark.email
    @pytest.mark.email_valid
    @pytest.mark.parametrize("email, expected", [
        ("name@domain.com", {"email": "name@domain.com"}),
        ("name.name@domain.com", {"email": "name.name@domain.com"}),
        ("name999@domain.com", {"email": "name999@domain.com"}),
        ("name.\.name@domain.com", {"email": "name.\.name@domain.com"})
        ])
    def test_get_user_by_email_valid(self, user_controller, email, expected):
        """Test the return of correct addresses"""
        result = user_controller.get_user_by_email(email)
        assert expected == result

    # Test valid emails using user_controller_multiple_users fixture
    @pytest.mark.email
    @pytest.mark.email_valid_multiple_users
    @pytest.mark.parametrize("email, expected", [
        ("name@domain.com", {
            "username": "Alice",
            "email": "name@domain.com"
            })
        ])
    def test_get_user_by_email_valid_multiple(self, user_controller_multiple_users, email, expected):
        """Test return of first address in case of multiple users with same email address"""
        result = user_controller_multiple_users.get_user_by_email(email)
        assert expected == result

    # Test valid email but user does not exist in database
    @pytest.mark.email
    @pytest.mark.email_none
    def test_email_is_none(self):
        """
        Test if get_user_by_email returns None when provided email is not found in the database
        """
        dao_mock = MagicMock()
        dao_mock.find = MagicMock(return_value=[])
        user_controller = UserController(dao_mock)
        result = user_controller.get_user_by_email("mail@host.com")
        assert result == None



