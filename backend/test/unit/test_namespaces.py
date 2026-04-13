import pytest
from src.util.daos import getDao
from src.util.dao import DAO
from src.util.helpers import UserController
from unittest.mock import MagicMock, patch
from src.util.helpers import diceroll


class TestNamespaces:
    @pytest.mark.ns
    def test_1(self):
        with patch('src.util.daos.DAO') as mockedDAO:
            mock = MagicMock()
            mockedDAO.return_value = mock
            assert getDao(collection_name='test') == mock

    @pytest.mark.ns
    def test_2(self):
        with patch('src.util.helpers.random.randint') as mockrandint:
            mockrandint.return_value = 6
            assert diceroll() == True

    @pytest.mark.ns
    def test_3(self):
        """Assume you want to test the get_user_by_email method in the UserController class, 
        but you want to temporarily "disarm" the email validation which is implemented using 
        a regular expression. Combine mocking via dependency injection (to mock the find() 
        method of the DAO) with patching (to mock the fullmatch() method of the regex library).
        """

        user = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe'}
        # TODO: mock the DAO such that it returns this simulated user

        mockedDAO = MagicMock()
        mockedDAO.find = MagicMock(return_value=[user])
        uc = UserController(dao=mockedDAO)

        # TODO: patch the fullmatch method of the regex library
        with patch('src.controllers.usercontroller.re.fullmatch') as mockfullmatch:
            mockfullmatch.return_value = True

            assert uc.get_user_by_email(email='jane.doe') == user
