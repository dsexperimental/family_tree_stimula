# Child tasks: Initial UI Layer

1. [ ] **Design CLI Interface**: Place in the {$project_root}/ui directory.
    - Overview:
        - Define the main menu and commands for interacting with the family tree (e.g., add person, remove person, add relationship, remove relationship, list relations, find relation).
        - Ensure commands are user-friendly and intuitive.
        - Keep the service layer interaction abstracted to ease the future transition to a web service from CLI.
    - Manual Test: instruct user to test the UI functions

2. [ ] **Implement `add_person` Command**: 
    - Functionality:
        - Prompt the user for person details (first name, last name, birthday, city, state, gender, and user name).
        - Validate input data.
        - Call the `create_person` service layer function.
    - Considerations:
        - Provide clear error messages for validation failures or operation errors.
    - Manual Test: instruct user to test the UI functions

3. [ ] **Implement `remove_person` Command**:
    - Functionality:
        - Prompt the user for a person's user name.
        - Call the `remove_person` service layer function.
    - Considerations:
        - Inform the user if the specified person does not exist.
    - Manual Test: instruct user to test the UI functions

4. [ ] **Implement `add_relationship` Command**:
    - Functionality:
        - Prompt the user for the user names of two people and the relationship type.
        - Validate input data.
        - Call the `create_relationship` service layer function.
    - Considerations:
        - Ensure relationship type input is valid.
        - Provide feedback if the operation is successful or if it fails (e.g., one of the users does not exist).
    - Manual Test: instruct user to test the UI functions

5. [ ] **Implement `remove_relationship` Command**:
    - Functionality:
        - Prompt the user for the user names of two people and the relationship type.
        - Call the `remove_relationship` service layer function.
    - Considerations:
        - Inform the user if the specified relationship does not exist.
    - Manual Test: instruct user to test the UI functions

6. [ ] **CLI Unit Tests**: [task_detail_folder](cli_unit_tests)

