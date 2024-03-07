from enum import Enum
from typing import Dict

class RelationType(Enum):
    PARENT = "parent"
    SPOUSE = "spouse"

class Relationship:
    def __init__(self, person1: str, person2: str, relation_type: RelationType):
        self.person1 = person1
        self.person2 = person2
        self.relation_type = relation_type

    def unique_identifier(self) -> str:
        """Generates a unique identifier for the relationship."""
        return f"{self.person1}|{self.person2}|{self.relation_type.value}"

    def to_dict(self) -> Dict[str, str]:
        """Converts the Relationship object to a dictionary."""
        return {
            "person1": self.person1,
            "person2": self.person2,
            "relation_type": self.relation_type.value,
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'Relationship':
        """Creates a Relationship object from a dictionary."""
        return Relationship(
            person1=data["person1"],
            person2=data["person2"],
            relation_type=RelationType(data["relation_type"]),
        )
