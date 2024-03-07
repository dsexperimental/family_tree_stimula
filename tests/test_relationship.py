import pytest
from models.relationship import Relationship, RelationType

def test_unique_identifier():
    relationship = Relationship("Alice", "Bob", RelationType.PARENT)
    assert relationship.unique_identifier() == "Alice|Bob|parent"

def test_to_dict():
    relationship = Relationship("Alice", "Bob", RelationType.SPOUSE)
    expected_dict = {"person1": "Alice", "person2": "Bob", "relation_type": "spouse"}
    assert relationship.to_dict() == expected_dict

def test_from_dict():
    data = {"person1": "Alice", "person2": "Bob", "relation_type": "spouse"}
    relationship = Relationship.from_dict(data)
    assert relationship.person1 == "Alice"
    assert relationship.person2 == "Bob"
    assert relationship.relation_type == RelationType.SPOUSE
