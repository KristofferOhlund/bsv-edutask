import pytest
from src.util.helpers import hasAttribute

@pytest.fixture
def create_dictionary():
    """
    Return an object with the key "Name", value "Test"
    """
    return {"Name": "Test"}

@pytest.mark.unit
def test_hasAttribute_true():
    """
    Test if hasAttribute returns True when key exists in object
    """
    # Arrange
    test_dicitonary = create_dictionary

    # Act
    result = hasAttribute(test_dicitonary, "Name")

    # Assert
    assert result == True

@pytest.mark.unit
def test_hasAttribute_false():
    """
    Test if hasAttribute returns False when key does not exist in object
    """
    # Arrange
    test_dicitonary = create_dictionary

    # Act
    result = hasAttribute(test_dicitonary, "Bike")
    assert result == False

@pytest.mark.unit
def test_hasAttribute_none():
    """
    Test if hasAttribute returns False when dict key is None
    """
    test_dictionary = None

    result = hasAttribute(test_dictionary, "hello")
    assert result == False