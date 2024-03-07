import pytest
from datetime import datetime
from models.person import Person
from models.storage import add_person, person_storage, add_relationship, remove_relationship, relationship_storage, remove_person, list_relationships, clear_all, get_person
from models.relationship import Relationship, RelationType

@pytest.fixture(autouse=True)
def clear_storage_before_tests():
    """Fixture to clear storage before each test case."""
    clear_all()


def test_add_person_unique_username():
    """Test adding a person with a unique username."""
    person = Person("John", "Doe", datetime(1990, 1, 1), "New York", "NY", "male", "johndoe")
    result = add_person(person)
    assert result is True
    assert "johndoe" in person_storage

def test_add_person_duplicate_username():
    """Test adding a person with a duplicate username."""
    person1 = Person("Jane", "Doe", datetime(1990, 1, 1), "New York", "NY", "female", "janedoe")
    person2 = Person("Jane", "Smith", datetime(1990, 1, 1), "Los Angeles", "CA", "female", "janedoe")
    add_person(person1)
    result = add_person(person2)
    assert result is False
    assert person_storage["janedoe"]["last_name"] == "Doe"  # Ensures the first entry wasn't overwritten

def test_add_relationship_unique():
    """Test adding a relationship with a unique identifier."""
    relationship = Relationship("user1", "user2", RelationType.PARENT)
    result = add_relationship(relationship)
    assert result is True
    assert relationship.unique_identifier() in relationship_storage

def test_add_relationship_duplicate():
    """Test adding a relationship with a duplicate identifier."""
    relationship1 = Relationship("user1", "user3", RelationType.SPOUSE)
    relationship2 = Relationship("user1", "user3", RelationType.SPOUSE)  # Same as relationship1
    add_relationship(relationship1)  # Add the first relationship
    result = add_relationship(relationship2)  # Attempt to add the duplicate
    assert result is False
    # Ensure only one entry exists for this relationship in the storage
    assert len([key for key, value in relationship_storage.items() if value['person1'] == 'user1' and value['person2'] == 'user3']) == 1

def test_remove_existing_relationship():
    """Test removing an existing relationship."""
    # Setup: Add persons and a relationship before attempting to remove
    person1 = Person("User", "One", datetime(1990, 1, 1), "City", "State", "male", "user1")
    person2 = Person("User", "Two", datetime(1990, 1, 1), "City", "State", "female", "user2")
    add_person(person1)
    add_person(person2)
    relationship = Relationship("user1", "user2", RelationType.PARENT)
    add_relationship(relationship)
    
    # Test: Attempt to remove the added relationship
    result = remove_relationship("user1", "user2", RelationType.PARENT)
    assert result is True
    assert "user1|user2|parent" not in relationship_storage

def test_remove_nonexistent_relationship():
    """Test attempting to remove a relationship that does not exist."""
    result = remove_relationship("nonexistent_user1", "nonexistent_user2", RelationType.SPOUSE)
    assert result is False

def test_remove_existing_person():
    """Test removing an existing person."""
    person = Person("Test", "User", datetime(1990, 1, 1), "Test City", "Test State", "male", "testuser")
    add_person(person)  # Add the person before attempting to remove
    result = remove_person("testuser")
    assert result is True
    assert "testuser" not in person_storage

def test_remove_nonexistent_person():
    """Test attempting to remove a person that does not exist."""
    result = remove_person("nonexistent_user")
    assert result is False

def test_get_existing_person():
    """Test retrieving an existing person by username."""
    # Setup: Add a person to the storage
    person = Person("Alice", "Smith", datetime(1990, 5, 20), "Springfield", "IL", "female", "alicesmith")
    add_person(person)
    # Test: Retrieve the person
    retrieved_person = get_person("alicesmith")
    assert retrieved_person is not None
    assert retrieved_person.user_name == "alicesmith"
    assert retrieved_person.first_name == "Alice"

def test_get_nonexistent_person():
    """Test attempting to retrieve a person by a username that does not exist."""
    # Test: Attempt to retrieve a nonexistent person
    retrieved_person = get_person("nonexistent_user")
    assert retrieved_person is None

def test_list_relationships_for_existing_person():
    """Test listing relationships for a person with existing relationships."""
    # Setup: Add persons and relationships
    person1 = Person("User", "One", datetime(1990, 1, 1), "City", "State", "male", "user1")
    person2 = Person("User", "Two", datetime(1990, 1, 1), "City", "State", "female", "user2")
    add_person(person1)
    add_person(person2)
    relationship = Relationship("user1", "user2", RelationType.SPOUSE)
    add_relationship(relationship)
    # Test: List relationships for user1
    relationships = list_relationships("user1")
    assert len(relationships) == 1
    assert relationships[0]['person1'] == "user1"
    assert relationships[0]['person2'] == "user2"
    assert relationships[0]['relation_type'] == "spouse"

def test_list_relationships_for_person_with_no_relationships():
    """Test listing relationships for a person with no relationships."""
    # Setup: Add a person without adding any relationships
    person = Person("Lonely", "User", datetime(1990, 1, 1), "City", "State", "male", "lonelyuser")
    add_person(person)
    # Test: List relationships for lonelyuser
    relationships = list_relationships("lonelyuser")
    assert len(relationships) == 0

def test_clear_all():
    """Test clearing all stored persons and relationships."""
    # Setup: Add some persons and relationships
    person1 = Person("Temp", "User1", datetime(1990, 1, 1), "City1", "State1", "male", "tempuser1")
    person2 = Person("Temp", "User2", datetime(1990, 1, 2), "City2", "State2", "female", "tempuser2")
    add_person(person1)
    add_person(person2)
    relationship = Relationship("tempuser1", "tempuser2", RelationType.SPOUSE)
    add_relationship(relationship)
    
    # Ensure setup was successful
    assert len(person_storage) > 0
    assert len(relationship_storage) > 0
    
    # Test: Clear all
    clear_all()
    
    # Verify clearing was successful
    assert len(person_storage) == 0
    assert len(relationship_storage) == 0
