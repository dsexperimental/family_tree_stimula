from datetime import datetime
from models.person import Person

def test_person_to_dict():
    person = Person(
        first_name="John",
        last_name="Doe",
        birthday=datetime(1990, 1, 1),
        city="New York",
        state="NY",
        gender="Male",
        user_name="john_doe"
    )
    expected_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "birthday": "1990-01-01",
        "city": "New York",
        "state": "NY",
        "gender": "Male",
        "user_name": "john_doe",
    }
    assert person.to_dict() == expected_dict

def test_person_from_dict():
    person_dict = {
        "first_name": "Jane",
        "last_name": "Doe",
        "birthday": "1995-02-02",
        "city": "Los Angeles",
        "state": "CA",
        "gender": "Female",
        "user_name": "jane_doe",
    }
    person = Person.from_dict(person_dict)
    assert person.first_name == "Jane"
    assert person.last_name == "Doe"
    assert person.birthday == datetime(1995, 2, 2)
    assert person.city == "Los Angeles"
    assert person.state == "CA"
    assert person.gender == "Female"
    assert person.user_name == "jane_doe"