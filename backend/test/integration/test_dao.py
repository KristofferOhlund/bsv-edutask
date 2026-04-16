import pytest
from unittest.mock import MagicMock, patch
from src.util.dao import DAO
import json
from pymongo.errors import WriteError
from validation_data import OK_VALIDATION_DATA, INVALID_VALIDATION_DATA, DUPLICATE_DATA

@pytest.fixture
def validator_file(filename):
    with open(f'./src/static/validators/{filename}.json', 'r') as f:
        return json.load(f)

@pytest.fixture
def mock_dao(validator_file):
    with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
        patched_validator.return_value = validator_file
        dao = DAO("test")
        yield dao
        dao.drop()

# ----- OK_VALIDATION_DATA -----
@pytest.mark.valid
@pytest.mark.dao
@pytest.mark.parametrize("filename, in_data, expected", OK_VALIDATION_DATA)
def test_dao_create_objects(mock_dao, in_data, expected):
        dao = mock_dao
        result = dao.create(in_data)
        assert expected in result["_id"]
        print("\nOK VALIDATION POST LENGTH: ", len(dao.find()))


# ----- INVALID_VALIDATION_DATA -----
@pytest.mark.invalid_data
@pytest.mark.dao
@pytest.mark.parametrize("filename, in_data, expected", INVALID_VALIDATION_DATA)
def test_dao_create_bad_data(mock_dao, in_data, expected):
    dao = mock_dao
    with pytest.raises(WriteError) as execinfo:
        dao.create(in_data)
        print("\nPRINT: ", dao.find())
    assert expected in str(execinfo.value)



# ----- DUPLICATE_DATA -----
@pytest.mark.dao
@pytest.mark.parametrize("filename, in_data, expected", DUPLICATE_DATA)
def test_dao_create_duplicate_data(mock_dao, in_data, expected):
    dao = mock_dao
    with pytest.raises(WriteError) as execinfo:
        dao.create(in_data)
        dao.create(in_data)
        print("\nDUBBLA::: ", dao.find())
        print("LENGTH: ", len(dao.find()), "\n")
    assert expected in str(execinfo.value)
