import pytest
from src.util.helpers import ValidationHelper
from unittest.mock import MagicMock

"""
Arrange:
We inject a factory function.
We can access child-function (that takes an argument, age).
The child-function gets the name of the parent-function.
A bit DRY:er than previous version. But hard to read for noobs like us!
https://docs.pytest.org/en/stable/explanation/fixtures.html
https://docs.python.org/3/library/unittest.mock.html
For clarifications and explanations: gemini.google.com
"""
@pytest.fixture
def helper_factory():
    # private, only used through parent.
    def _validation_helper_creator(age):
        mock_user = MagicMock()
        mock_user.get = MagicMock(return_value={"age": age})
        # def returner(id="id"):
        #     print(id)
        #     return {"age": age}
        # mock_user.get = returner
        validation_helper = ValidationHelper(mock_user)
        return validation_helper
    return _validation_helper_creator

@pytest.fixture
def userid():
    return "42"

@pytest.mark.unit
def test_validateAge_age_negative(userid, helper_factory):
    validation_helper = helper_factory(-1)

    result = validation_helper.validateAge(userid)
    
    assert result == "invalid"

@pytest.mark.unit
def test_validateAge_age_zero(userid, helper_factory):
    validation_helper = helper_factory(0)

    result = validation_helper.validateAge(userid)
    
    assert result == "underaged"

@pytest.mark.unit
def test_validateAge_age_1(userid, helper_factory):
    validation_helper = helper_factory(1)

    result = validation_helper.validateAge(userid)
    
    assert result == "underaged"

@pytest.mark.unit
def test_validateAge_age_17(userid, helper_factory):
    validation_helper = helper_factory(17)

    result = validation_helper.validateAge(userid)
    
    assert result == "underaged"

@pytest.mark.unit
def test_validateAge_age_18(userid, helper_factory):
    validation_helper = helper_factory(18)

    result = validation_helper.validateAge(userid)
    
    assert result == "valid"

@pytest.mark.unit
def test_validateAge_age_19(userid, helper_factory):
    validation_helper = helper_factory(19)

    result = validation_helper.validateAge(userid)
    
    assert result == "valid"

@pytest.mark.unit
def test_validateAge_age_119(userid, helper_factory):
    validation_helper = helper_factory(119)

    result = validation_helper.validateAge(userid)
    
    assert result == "valid"

@pytest.mark.unit
def test_validateAge_age_120(userid, helper_factory):
    validation_helper = helper_factory(120)

    result = validation_helper.validateAge(userid)
    
    assert result == "valid"

@pytest.mark.unit
def test_validateAge_age_121(userid, helper_factory):
    validation_helper = helper_factory(121)

    result = validation_helper.validateAge(userid)
    
    assert result == "invalid"
