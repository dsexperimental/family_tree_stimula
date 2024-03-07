# Child tasks: Initial Service Layer

1. [ ] **Implement `create_person` function**: Place in the {$project_root}/services directory.
    - Functionality:
        - Accepts details for a new person (first name, last name, birthday, city, state, gender, and user name).
        - Validates the input data.
        - Calls the data access layer to store the new person.
    - Considerations:
        - Ensure the user name is unique before proceeding with creation.
        - Include error handling for data validation and storage operations.
    - Create unit testing for `create_person` functionality. (Do _not_ mock underlying layers)

2. [ ] **Implement `remove_person` function**: Place in the {$project_root}/services directory.
    - Functionality:
        - Accepts a person's user name.
        - Validates the existence of the person.
        - Calls the data access layer to remove the specified person.
    - Considerations:
        - Include error handling for cases where the person does not exist.
    - Create unit testing for `remove_person` functionality. (Do _not_ mock underlying layers)

3. [ ] **Implement `create_relationship` function**: Place in the {$project_root}/services directory.
    - Functionality:
        - Accepts user names of two people and a relationship type.
        - Validates the existence of both people and the relationship type.
        - Calls the data access layer to store the new relationship.
    - Considerations:
        - Ensure that the relationship does not already exist.
        - Include error handling for data validation and storage operations.
    - Create unit testing for `create_relationship` functionality. (Do _not_ mock underlying layers)

4. [ ] **Implement `remove_relationship` function**: Place in the {$project_root}/services directory.
    - Functionality:
        - Accepts user names of two people and a relationship type.
        - Validates the existence of the specified relationship.
        - Calls the data access layer to remove the relationship.
    - Considerations:
        - Include error handling for cases where the relationship does not exist.
    - Create unit testing for `remove_relationship` functionality. (Do _not_ mock underlying layers)

