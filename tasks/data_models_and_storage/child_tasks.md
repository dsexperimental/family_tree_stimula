# Child tasks: Data Models and Storage

1. [ ] **Implement `Person` Data Model**: Place in the {$project_root}/models directory.
    - Attributes:
        - First name
        - Last name
        - Birthday
        - City
        - State
        - Gender
        - User name (unique identifier)
    - Include functions to convert to and from a dictionary
    - Create unit testing as appropriate

2. [ ] **Define the `Relationship` model**: Place in the {$project_root}/models directory.
    - Attributes:
        - Person 1 (user name)
        - Person 2 (user name)
        - Relation type (Options: [parent, spouse] - define this enumeration somehow)
    - For unique identifier: person 1 + person 2 + relationship_type:
        - Include a function to make the unique identifier string. Choose a format such as appending the strings with appropriate separator, like "|"
    - Include functions to convert to and from a dictionary 
    - Create unit testing as appropriate

3. [ ] **Initial Data Storage**: [task_details_folder](initial_data_storage)

