import pytest
from src.util.helpers import ValidationHelper
from unittest.mock import MagicMock

def user_controller(age):
    mock = MagicMock()
    mock.get = MagicMock(return_value={"age": age})
    return mock

def validation_helper_creator(user_controller):
    validation_helper = ValidationHelper(user_controller)
    return validation_helper

@pytest.mark.unit
def test_validateAge_valid():
    userid = "10"
    mock_user = user_controller(30)
    validation_helper = validation_helper_creator(mock_user)

    result = validation_helper.validateAge(userid)
    
    assert result == "valid"

@pytest.mark.unit
def test_validateAge_invalid():
    userid = "10"
    mock_user = user_controller(-1)

    validation_helper = validation_helper_creator(mock_user)

    result = validation_helper.validateAge(userid)
    
    assert result == "invalid"
