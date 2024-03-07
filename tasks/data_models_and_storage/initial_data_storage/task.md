# Task File: Initial Data Storage

Implement an initial in-memory data storage system for the family tree application as a placeholder.

- Utilize Python dictionaries as the primary data structure for storing person and relationship information.

### Person Storage

- Key: Use the unique user name of each person as the dictionary key.
- Value: Store person details as a dictionary.

### Relationship Storage

- Key: Use the unique id for the relationship as the key.
- Value: Store all the relationship fields as a dictionary.

### Interface Functions

#### Adding Data

- `add_person(person)`: Adds a new person to the storage.
    - The `person` argument should be a `Person` instance.
    - Verify the unique ID is not present in the DB.
- `add_relationship(user_name_1, user_name_2, relationship_type)`: Adds a new relationship between two people.
    - Validates the existence of both people in the storage before adding.
    - Validates there is no existing relationship in the db

#### Removing Data

- `remove_person(user_name)`: Removes a person and all their relationships from the storage.
- `remove_relationship(user_name_1, user_name_2, relationship_type)`: Removes a specific relationship between two people.

#### Querying Data

- `get_person(user_name)`: Retrieves the details of a person by their user name. Returns a person object.
- `search_people(props)`: Search for people who have attributes matching the passed dictionary. Returns a list of person objects. 
- `list_relationships(user_name)`: Lists all relationships for the given person.