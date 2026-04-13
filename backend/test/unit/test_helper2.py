import pytest
from unittest.mock import MagicMock, patch
from src.util.helpers import ValidationHelper2



@pytest.mark.dep
def test_validationHelper2():
    with patch("src.util.helpers.UserController", autospec=True) as patched_controller:
         with patch("src.util.helpers.DAO", autospec=True) as patched_DAO:
              user_controller = patched_controller(patched_DAO)
              user_controller.get = MagicMock(return_value={"age": 5})

              helper = ValidationHelper2()
              assert helper.validateAge("14") == "underaged"



@pytest.mark.dep
@patch("src.util.helpers.UserController", autospec=True)
@patch("src.util.helpers.DAO", autospec=True)
def test_validationHelper2_2(dao_boy, user_boy):
     user_controller = user_boy(dao_boy)
     user_controller.get = MagicMock(return_value={"age": -5})

     helper = ValidationHelper2()

     assert helper.validateAge("100") == "invalid"
