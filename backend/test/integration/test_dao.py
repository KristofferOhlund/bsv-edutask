import pytest
from unittest.mock import MagicMock, patch
from src.util.dao import DAO
import json
from pymongo.errors import WriteError
from validation_data import OK_VALIDATION_DATA, INVALID_VALIDATION_DATA

@pytest.fixture
def validator_file(filename):
    with open(f'./src/static/validators/{filename}.json', 'r') as f:
        return json.load(f)

# ----- OK_VALIDATION_DATA -----
@pytest.mark.valid
@pytest.mark.parametrize("filename, in_data, expected", OK_VALIDATION_DATA)
def test_dao_create_objects(validator_file, filename, in_data, expected):
    with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
        patched_validator.return_value = validator_file
        dao = DAO(filename)
        result = dao.create(in_data)
        assert isinstance(result, expected)
        assert "$oid" in result["_id"]
        dao.drop()


# ----- INVALID_VALIDATION_DATA -----
@pytest.mark.dao
@pytest.mark.parametrize("filename, in_data, expected", INVALID_VALIDATION_DATA)
def test_dao_create_bad_data(validator_file, filename, in_data, expected):
    with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
        patched_validator.return_value = validator_file
        dao = DAO(filename)
        with pytest.raises(WriteError) as execinfo:
            dao.create(in_data)
        assert expected in str(execinfo.value)



# ----- WORKING DATA -----
# @pytest.mark.dao
# def test_dao_create(get_validator_config):
#     with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
#         patched_validator.return_value = get_validator_config
        
#         dao = DAO("task")
        
#         inserted_obj = dao.create({"title": "my_title", "description": "my_description"})
#         # print("#" * 30)
#         # print(dao.find())
#         print(inserted_obj)

#         assert  '_id' in inserted_obj
#         # dao.delete(inserted_obj["_id"])
#         # dao.drop()
#         # print(dao.find())