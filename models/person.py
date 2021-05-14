from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"