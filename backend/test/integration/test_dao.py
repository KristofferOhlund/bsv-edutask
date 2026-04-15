import pytest
from unittest.mock import MagicMock, patch
from src.util.dao import DAO
import json


@pytest.fixture
def get_validator_config():
    param = "task"
    with open(f'./src/static/validators/{param}.json', 'r') as f:
        return json.load(f)
    

# @pytest.mark.dao
# @pytest.mark.parametrize("config, expected", [("task", dict), ("todo", dict), ("user", dict), ("video", dict),])
# def test_dao_create(get_validator_config, config, expected):
#     dao = DAO()

@pytest.mark.dao
def test_dao_create(get_validator_config):
    with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
        patched_validator.return_value = get_validator_config
        
        dao = DAO("task")
        
        # inserted_id = dao.create({"title": "my_title", "description": "my_description"})
        # print("#" * 30)
        print(dao.find())
        # print("#" * 30)

        # assert type(dao.findOne(inserted_id)) == object
