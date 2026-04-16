# import pytest
# from unittest.mock import MagicMock, patch
# from src.util.dao import DAO
# import json
# from pymongo.errors import WriteError
# from validation_data import OK_VALIDATION_DATA, INVALID_VALIDATION_DATA, DUPLICATE_DATA

# @pytest.fixture
# def validator_file(filename):
#     with open(f'./src/static/validators/{filename}.json', 'r') as f:
#         return json.load(f)

# # ----- OK_VALIDATION_DATA -----
# @pytest.mark.valid
# @pytest.mark.dao1
# @pytest.mark.parametrize("filename, in_data, expected", OK_VALIDATION_DATA)
# def test_dao_create_objects(validator_file, filename, in_data, expected):
#     with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
#         patched_validator.return_value = validator_file
#         dao = DAO(filename)
#         result = dao.create(in_data)
#         dao.drop()
#         assert isinstance(result, expected)
#         assert "$oid" in result["_id"]
#         print("\nOK VALIDATION POST LENGTH: ", len(dao.find()))


# # ----- INVALID_VALIDATION_DATA -----
# @pytest.mark.dao1
# @pytest.mark.parametrize("filename, in_data, expected", INVALID_VALIDATION_DATA)
# def test_dao_create_bad_data(validator_file, filename, in_data, expected):
#     with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
#         patched_validator.return_value = validator_file
#         dao = DAO(filename)
#         with pytest.raises(WriteError) as execinfo:
#             dao.create(in_data)
#         assert expected in str(execinfo.value)

#         # cleanup
#         dao.drop()


# # ----- DUPLICATE_DATA -----
# @pytest.mark.dao1
# @pytest.mark.parametrize("filename, in_data, expected", DUPLICATE_DATA)
# def test_dao_create_duplicate_data(validator_file, filename, in_data, expected):
#     with patch("src.util.dao.getValidator", autospec=True) as patched_validator:
#         patched_validator.return_value = validator_file
#         dao = DAO(filename)
#         with pytest.raises(WriteError) as execinfo:
#             # dao.drop()
#             dao.create(in_data)
#             dao.create(in_data)
#             print("\nDUBBLA::: ", dao.find())
#             print("\nLENGTH: ", len(dao.find()))
#             dao.drop()
#         assert expected in str(execinfo.value)
