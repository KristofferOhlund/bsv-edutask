import pytest
from unittest.mock import MagicMock, patch
from src.util.dao import DAO
import json
from pymongo.errors import WriteError


@pytest.fixture
def validator_file(filename):
    with open(f'./src/static/validators/{filename}.json', 'r') as f:
        return json.load(f)
    

# @pytest.mark.dao
# @pytest.mark.parametrize("config, expected", [("task", dict), ("todo", dict), ("user", dict), ("video", dict),])
# def test_dao_create(get_validator_config, config, expected):
#     dao = DAO()

# ----- BAD DATA -----
@pytest.mark.dao
@pytest.mark.parametrize("filename, in_data, expected", [
                         ("task", {"title": 1, "description": "my_description"}, 'type did not match')
                        ])
def test_dao_create_bad_data(validator_file, filename, in_data, expected): 
    with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
        patched_validator.return_value = validator_file
        dao = DAO("filename")
        with pytest.raises(WriteError) as execinfo:
            result = dao.create(in_data)
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