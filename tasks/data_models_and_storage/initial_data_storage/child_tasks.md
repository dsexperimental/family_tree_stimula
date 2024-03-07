

7. [x] **Create `clear_all` Function** Add it to the file {$project_root}/models/storage.py.
    - Functionality:
        - Clear all stored persons and relationships.
    - Create unit testing for the `clear_all` functionality, updating the file {$project_root}/tests/test_storage.py.
	
8. [x] **Add test init** In the test file {$project_root}/tests/test_storage.py
	- add an initialization step to the testing	that includes the function "clear_all", to set a clean starting point for the tests.
	- Rerun the tests

9. [ ] **Create `list_relationships` Query Function** Add it to the file {$project_root}/models/storage.py.
    - Functionality:
        - Lists all relationships for a given person.
    - Create unit testing for the `list_relationships` functionality, updating the file {$project_root}/tests/test_storage.py.

10. [ ] **Create `search_people` Query Function** Add it to the file {$project_root}/models/storage.py.
    - Functionality:
        - Searches for people matching a passed dictionary of attributes.
        - Returns a list of `Person` objects that match the criteria.
    - Create unit testing for the `search_people` functionality, updating the file {$project_root}/tests/test_storage.py.
