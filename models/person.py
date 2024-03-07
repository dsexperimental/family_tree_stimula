from datetime import datetime
from typing import Dict

class Person:
    def __init__(self, first_name: str, last_name: str, birthday: datetime, city: str, state: str, gender: str, user_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.city = city
        self.state = state
        self.gender = gender
        self.user_name = user_name

    def to_dict(self) -> Dict[str, str]:
        """Converts the Person object to a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday.strftime("%Y-%m-%d"),
            "city": self.city,
            "state": self.state,
            "gender": self.gender,
            "user_name": self.user_name,
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> "Person":
        """Creates a Person object from a dictionary."""
        return Person(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birthday=datetime.strptime(data["birthday"], "%Y-%m-%d"),
            city=data["city"],
            state=data["state"],
            gender=data["gender"],
            user_name=data["user_name"],
        )