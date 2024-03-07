# /app/stimula_working/family_tree/models/storage.py

# Dictionary to simulate in-memory storage for Person details.
# Key: user_name (unique identifier for each person)
# Value: Dictionary of person details
person_storage = {}

# Dictionary to simulate in-memory storage for Relationships.
# Key: unique identifier for the relationship (combination of person1, person2, and relation_type)
# Value: Dictionary of relationship details
relationship_storage = {}

from .person import Person
from .relationship import Relationship, RelationType

def add_person(new_person: Person) -> bool:
    """Adds a new person to the storage if the username is unique.

    Args:
        new_person (Person): The person instance to add.

    Returns:
        bool: True if the person was added, False if the username already exists.
    """
    if new_person.user_name in person_storage:
        return False
    person_storage[new_person.user_name] = new_person.to_dict()
    return True

def add_relationship(new_relationship: Relationship) -> bool:
    """Adds a new relationship to the storage if the unique identifier is not already present.

    Args:
        new_relationship (Relationship): The relationship instance to add.

    Returns:
        bool: True if the relationship was added, False if the unique identifier already exists.
    """
    unique_id = new_relationship.unique_identifier()
    if unique_id in relationship_storage:
        return False
    relationship_storage[unique_id] = new_relationship.to_dict()
    return True

def remove_relationship(person1: str, person2: str, relation_type: RelationType) -> bool:
    """Removes a relationship from the storage if it exists.

    Args:
        person1 (str): The user_name of the first person in the relationship.
        person2 (str): The user_name of the second person in the relationship.
        relation_type (RelationType): The type of the relationship.

    Returns:
        bool: True if the relationship was removed, False if the relationship does not exist.
    """
    unique_id = f"{person1}|{person2}|{relation_type.value}"
    if unique_id in relationship_storage:
        del relationship_storage[unique_id]
        return True
    return False

def remove_person(user_name: str) -> bool:
    """Removes a person from the storage if they exist.

    Args:
        user_name (str): The user_name of the person to remove.

    Returns:
        bool: True if the person was removed, False if the person does not exist.
    """
    if user_name in person_storage:
        del person_storage[user_name]
        return True
    return False

def get_person(user_name: str) -> Person:
    """Retrieves a person from the storage by their username.

    Args:
        user_name (str): The username of the person to retrieve.

    Returns:
        Person: The person object if found, otherwise None.
    """
    person_dict = person_storage.get(user_name)
    if person_dict:
        return Person.from_dict(person_dict)
    return None

def list_relationships(user_name: str) -> list:
    """Lists all relationships for a given person.

    Args:
        user_name (str): The user_name of the person whose relationships are to be listed.

    Returns:
        list: A list of dictionaries, each representing a relationship involving the given person.
    """
    relationships = []
    for relationship in relationship_storage.values():
        if user_name in [relationship['person1'], relationship['person2']]:
            relationships.append(relationship)
    return relationships

def clear_all() -> None:
    """Clears all stored persons and relationships."""
    person_storage.clear()
    relationship_storage.clear()
