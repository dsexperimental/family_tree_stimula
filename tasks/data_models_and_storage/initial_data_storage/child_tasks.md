# Child Tasks: Initial Data Storage

1. [ ] **Implement Storage Mechanism**
    - Utilize Python dictionaries to simulate in-memory data storage.
    - Structure:
        - Person Storage: Use the unique user name as the dictionary key and person details as a dictionary for the value.
        - Relationship Storage: Use the unique identifier key for the relationship as the key and all relationship fields as a dictionary for the value.

2. [ ] **Create `add_person` Function**
    - Functionality:
        - Adds a new person to the storage using a `Person` instance.
        - Checks for uniqueness of the user name before adding.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `add_person` functionality.

3. [ ] **Create `add_relationship` Function**
    - Functionality:
        - Adds a new relationship between two people.
        - Validates the existence of both people in the storage.
        - Ensures there is no existing relationship of the same type between the individuals.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `add_relationship` functionality.

4. [ ] **Create `remove_relationship` Function**
    - Functionality:
        - Removes a specific relationship between two people.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `remove_relationship` functionality.

5. [ ] **Create `remove_person` Function**
    - Functionality:
        - Removes a person and all their relationships from the storage.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `remove_person` functionality.

6. [ ] **Create `get_person` Query Function**
    - Functionality:
        - Retrieves the details of a person by their user name.
        - Returns a `Person` object.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `get_person` functionality.

7. [ ] **Create `list_relationships` Query Function**
    - Functionality:
        - Lists all relationships for a given person.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `list_relationships` functionality.

8. [ ] **Create `search_people` Query Function**
    - Functionality:
        - Searches for people matching a passed dictionary of attributes.
        - Returns a list of `Person` objects that match the criteria.
    - Location: Place in the {$project_root}/storage directory.
    - Create unit testing for the `search_people` functionality.
